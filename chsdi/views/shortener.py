# -*- coding: utf-8 -*-
import logging

from pyramid.view import view_config
import pyramid.httpexceptions as exc

import boto3.exceptions as boto_exc
from boto3.dynamodb.conditions import Key

import time

from chsdi.models.clientdata_dynamodb import get_dynamodb_table
from chsdi.lib.helpers import check_url, make_api_url


def _add_item(table, url):
    logging.debug("ENTRY IN ADD ITEM")
    logging.debug(table)
    logging.debug(url)
    url_short = _get_url_short(table, url)
    if url_short is None:  # pragma: no cover
        # Create a new short url if url not in DB
        # Magic number relates to the initial epoch
        t = int(time.time() * 1000) - 1000000000000
        url_short = '%x' % t
        try:
            table.put_item(
                Item={
                    'url_short': url_short,
                    'url': url,
                    'timestamp': time.strftime('%Y-%m-%d %X', time.localtime())
                }
            )
        except boto_exc.Boto3Error as e:
            # TODO : find boto3 equivalent for ProvisionedThroughputExceededException
            raise exc.HTTPInternalServerError('Write units exceeded: %s' % e)
        except Exception as e:
            raise exc.HTTPInternalServerError('Error during put item %s' % e)
        return url_short
    else:
        return url_short


def _get_url_short(table, url):
    logging.debug("in to get url short ------")
    logging.debug(table)
    logging.debug(url)

    response  = table.query(
        IndexName="UrlIndex",
        KeyConditionExpression=Key('url').eq(url),
    )
    try:
        logging.debug("INSIDE TRY")
        logging.debug(response)
        return response['Items'][0]['url_short']
    except Exception:
        return None


@view_config(route_name='shorten', renderer='jsonp')
def shortener(request):
    logging.debug("ENTRY IN SHORTENER -- -- --")
    logging.debug(request)
    logging.debug(request.params)
    url = request.params.get('url')
    logging.debug(url)
    logging.debug(request.host)
    if len(url) >= 2046:
        # we only accept URL shorter or equal to 2046 characters
        # Index restriction in DynamoDB
        url_short = 'toolong'
    else:  # pragma: no cover
        logging.debug("CHECK URL")
        url_short = check_url(url, request.registry.settings)
        logging.debug("URL CHECKED")
        # DynamoDB v2 high-level abstraction
        try:
            logging.debug("GETTING A TABLE NAME SHORTURL")
            table = get_dynamodb_table(table_name='shorturl')
        except Exception as e:
            raise exc.HTTPInternalServerError('Error during connection %s' % e)
        logging.debug("IN SHORTENER")
        logging.debug(request)
        logging.debug(url)
        url_short = _add_item(table, url)
        logging.debug(" AFTER URL_SHORT -------------")
        logging.debug(url_short)
        logging.debug(" IS THERE A PROBLEM HERE ?")

    # Use env specific URLs
    if request.host not in ('api.geo.admin.ch', 'api3.geo.admin.ch'):
        host_url = make_api_url(request) + '/shorten/'
    else:
        host_url = ''.join((request.scheme, '://s.geo.admin.ch/'))
    return {
        'shorturl': host_url + url_short
    }


@view_config(route_name='shorten_redirect')
def shorten_redirect(request):
    url_short = request.matchdict.get('id')

    if url_short == 'toolong':
        raise exc.HTTPFound(location='http://map.geo.admin.ch')

    table = get_dynamodb_table(table_name='shorturl')

    try:
        url_match = table.get_item(Key={
            'url_short': url_short
        })
        url = url_match['Item']['url']
    except boto_exc.ResourceNotExistsError as e:
        raise exc.HTTPNotFound('This short url doesn\'t exist: s.geo.admin.ch/%s Error is: %s' % (url_short, e))
    except boto_exc.Boto3Error as e:  # pragma: no cover
        # TODO: same as above
        raise exc.HTTPInternalServerError('Read units exceeded: %s' % e)
    except Exception as e:  # pragma: no cover
        raise exc.HTTPInternalServerError('Unexpected internal server error: %s' % e)

    raise exc.HTTPMovedPermanently(location=url)
