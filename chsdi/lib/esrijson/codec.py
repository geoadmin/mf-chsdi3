import json

from chsdi.lib.esrijson.base import EsriJSON
from chsdi.lib.esrijson.geometry import from_shape


class EsriJSONEncoder(json.JSONEncoder):

    def default(self, o):
        return EsriJSON.to_instance(o)


def _enforce_strict_numbers(obj):
    if isinstance(obj, (int, float)):
        raise ValueError("Number %r is not JSON compliant" % obj)


def dump(obj, fp, cls=EsriJSONEncoder, allow_nan=False, **kwargs):
    return json.dump(obj, fp, cls=cls, allow_nan=allow_nan, **kwargs)


def dumps(obj, cls=EsriJSONEncoder, allow_nan=False, **kwargs):
    ob = from_shape(obj)
    obj = obj if ob is None else ob
    return json.dumps(obj, cls=cls, allow_nan=allow_nan, **kwargs)


def load(fp,
         cls=json.JSONDecoder,
         parse_constant=_enforce_strict_numbers,
         object_hook=EsriJSON.to_instance,
         **kwargs):
    return json.load(fp,
                     cls=cls, object_hook=object_hook,
                     parse_constant=parse_constant,
                     **kwargs)


def loads(s,
          cls=json.JSONDecoder,
          parse_constant=_enforce_strict_numbers,
          object_hook=EsriJSON.to_instance,
          **kwargs):
    return json.loads(s,
                      cls=cls, object_hook=object_hook,
                      parse_constant=parse_constant,
                      **kwargs)
