import json

from chsdi.lib.esrijson.base import EsriJSON


def to_mapping(obj):

    if isinstance(obj, EsriJSON):
        return obj

    return json.loads(json.dumps(obj))
