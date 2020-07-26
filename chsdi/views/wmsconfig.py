# -*- coding: utf-8 -*-


from collections import OrderedDict
from pyramid.view import view_config


from sqlalchemy import Unicode, Integer
from sqlalchemy import func

from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy.exc import SQLAlchemyError
import pyramid.httpexceptions as exc


from chsdi.models.bod  import WmsConfiguration


import logging

log = logging.getLogger(__name__)


class WmsConfig(object):
    """Service to return special WMS configuration for mostly the service-proxywms

    Replace the local DG query from the https://github.com/geoadmin/service-proxywms/blob/master/scripts/import-restrictions.py

    """

    def __init__(self, request):
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.cbName = request.params.get('callback')
        self.request = request
        self.lang = request.lang

    @view_config(route_name='wmsconfig', renderer='jsonp')
    def wmsconfig(self):

        model = WmsConfiguration

        try:
            query = self.request.db.query(
                model.datasetId,
                func.array_agg(model.timestamp, type_=ARRAY(Integer)).label('timestamp'),
                func.max(model.resolution_min).label("resolution_min"),
                func.min(model.resolution_max).label("resolution_max"),
                func.coalesce(func.min(model.s3_resolution_max), func.min(model.resolution_max)).label('s3_resolution_max'),
                func.array_agg(model.fmt, type_=ARRAY(Unicode)).label('fmt'),
                func.coalesce(model.cache_ttl, 1800).label('cache_ttl'),

                func.min(model.wms_gutter).label("wms_gutter")
            ).group_by(model.datasetId, model.fmt, model.cache_ttl).order_by(model.datasetId)
        except SQLAlchemyError as e:
            log.error("Error while requesting WMS restrictions:\n{}".format(e))
            raise exc.HTTPInternalServerError('Error while requesting for WMS restrictions')

        res = OrderedDict()
        for q in query:
            res[q.datasetId] = {'timestamp': list(set(q.timestamp)),
                                'resolution_min': q.resolution_min,
                                'resolution_max': q.resolution_max,
                                's3_max_resolution': q.s3_resolution_max,  # so much coherence
                                'format': q.fmt,
                                'cache_ttl': q.cache_ttl,

                                'wms_gutter': q.wms_gutter
                                }

        return res
