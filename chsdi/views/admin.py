# -*- coding: utf-8 -*-

import datetime
import requests
import logging
from requests.exceptions import RequestException
from pyramid.view import view_config
from pyramid.renderers import render_to_response
from chsdi.models.clientdata_dynamodb import get_dynamodb_table
from boto3.dynamodb.conditions import Key

LIMIT = 50


@view_config(route_name='adminkml', renderer='json')
def admin_kml(context, request):
    settings = request.registry.settings
    bucket_name = settings.get('geoadmin_file_storage_bucket')
    table_name = settings.get('geoadmin_file_storage_table')
    api_url = settings.get('api_url')
    logging.debug("-----------------------------------------------------------------------")
    logging.debug(bucket_name)
    logging.debug(table_name)
    logging.debug(api_url)
    logging.debug("-----------------------------------------------------------------------")
    files = kml_load(api_url=api_url, bucket_name=bucket_name, table_name=table_name)
    kmls = {'files': files, 'count': len(files), 'bucket': api_url, 'host': settings.get('geoadminhost')}

    response = render_to_response(
        'chsdi:templates/adminkml.mako',
        kmls)
    response.content_type = 'text/html'
    return response


def kml_load(api_url='//api3.geo.admin.ch', bucket_name=None, table_name=None):
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    table = get_dynamodb_table(table_name=table_name)
    fileids = []
    logging.debug("--------------------------------------------------------------------------------")
    logging.debug(date)
    logging.debug(bucket_name)
    logging.debug(table_name)
    logging.debug("--------------------------------------------------------------------------------")
    logging.debug(table.load())
    logging.debug("-------------------::::::::::::::::::::::::::::::::::::-------------------------")
    results = table.query(Limit=LIMIT * 4,
                          IndexName='bucketTimestampIndex',
                          KeyConditionExpression=Key('bucket').eq(bucket_name) & Key('timestamp').begins_with('2'),
                          ScanIndexForward=False)
    logging.debug("----------------------- ! ! ! ---------------------")
    logging.debug(results['Items'])
    logging.debug("----------------------- ! ! ! ---------------------")
    for f in results['Items']:
        try:
            resp = requests.head("http:" + api_url + "/files/" + f['fileId'], headers={'User-Agent': 'mf-geoadmin/python'})
            if int(resp.status_code) == 200:
                fileids.append((f['fileId'], f['adminId'], f['timestamp']))
        except RequestException as e:
            logging.error(e)
        if len(fileids) >= LIMIT:
            return fileids
    return fileids
