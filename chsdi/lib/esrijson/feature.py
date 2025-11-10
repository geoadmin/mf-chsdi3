from chsdi.lib.esrijson.base import EsriJSON
from chsdi.lib.esrijson.geometry import from_shape
from chsdi.lib.esrijson.mapping import to_mapping


class Feature(EsriJSON):

    def __init__(self, geometry=None, wkid=None, attributes=None, id=None,
                 **extra):

        """
        Initialises a Feature object with the given parameters.

        :param geometry: Geometry corresponding to the feature.
        :param wkid: well-know ID of the spatial reference.
        :param attributes: Dict containing the attributes of the feature.
        :type attributes: dict
        :param id: Feature identifier, such as a sequential number.
        :type id: str, int (not comp. in esri spec)
        """
        super(Feature, self).__init__(**extra)
        if id is not None:
            self["id"] = id
        geom = from_shape(geometry, wkid=wkid)
        if geom:
            self['geometry'] = geom
        elif geometry:
            self['geometry'] = self.to_instance(to_mapping(geometry), wkid)
        else:
            self['geometry'] = None
        self['attributes'] = attributes or {}
