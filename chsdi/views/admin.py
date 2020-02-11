# -*- coding: utf-8 -*-

import datetime
import requests
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
    api_url = settings.get('api_url')
    files = kml_load(api_url=api_url, bucket_name=bucket_name)
    kmls = {'files': files, 'count': len(files), 'bucket': api_url, 'host': settings.get('geoadminhost')}

    response = render_to_response(
        'chsdi:templates/adminkml.mako',
        kmls)
    response.content_type = 'text/html'
    return response


def kml_load(api_url='//api3.geo.admin.ch', bucket_name=None):
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    table = get_dynamodb_table(table_name='geoadmin-file-storage')
    fileids = []
    results = table.query(Limit=LIMIT * 4,
                          IndexName='bucketTimestampIndex',
                          KeyConditionExpression=Key('bucket').eq(bucket_name) & Key('timestamp').begins_with(date),
                          ScanIndexForward=False)
    for f in results['Items']:
        try:
            resp = requests.head("http:" + api_url + "/files/" + f['fileId'], headers={'User-Agent': 'mf-geoadmin/python'})
            if int(resp.status_code) == 200:
                fileids.append((f['fileId'], f['adminId'], f['timestamp']))
        except RequestException:
            pass
        if len(fileids) >= LIMIT:
            return fileids
    return fileids
