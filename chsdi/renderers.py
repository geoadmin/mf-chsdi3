# -*- coding: utf-8 -*-

import json
import decimal
import functools
import datetime
from sqlalchemy.ext.associationproxy import _AssociationList
from papyrus.renderers import GeoJSON
from geojson.codec import PyGFPEncoder


class EsriJSONEncoder(PyGFPEncoder):

    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        if isinstance(obj, _AssociationList):
            return list(obj)
        if isinstance(obj, decimal.Decimal):
            # The decimal is converted to a lossy float
            return float(obj)
        return PyGFPEncoder.default(self, obj)


dumps = functools.partial(json.dumps, cls=EsriJSONEncoder, allow_nan=False, use_decimal=True)


class EsriJSON(GeoJSON):

    def __init__(self, jsonp_param_name='callback'):
        GeoJSON.__init__(self)
        self.jsonp_param_name = jsonp_param_name

    def __call__(self, info):
        def _render(value, system):
            if isinstance(value, (list, tuple)):
                value = self.collection_type(value)
            ret = dumps(value)
            request = system.get('request')
            if request is not None:
                response = request.response
                ct = response.content_type
                if ct == response.default_content_type:
                    callback = request.params.get(self.jsonp_param_name)
                    if callback is None:
                        response.content_type = 'application/json'
                    else:
                        response.content_type = 'text/javascript'
                        ret = '%(callback)s(%(json)s);' % {'callback': callback,
                                                           'json': ret}
            return ret
        return _render

    def collection_type(self, value):
        return {'features': value}


class CSVRenderer(object):

    def __init__(self, info):
        pass

    def __call__(self, value, system):
        import csv
        import StringIO
        fout = StringIO.StringIO()
        writer = csv.writer(fout, delimiter=';', quoting=csv.QUOTE_ALL)

        writer.writerow(value['headers'])
        writer.writerows(value['rows'])

        resp = system['request'].response
        resp.content_type = 'text/csv'
        resp.content_disposition = 'attachment;filename="profile.csv"'
        return fout.getvalue()
