from shapely.geometry import Polygon
from shapely.geometry.polygon import orient


# For EsriJSON, exterior rings are oriented clockwise,
# while holes are oriented counter-clockwise.
# For GeoJSON, Polygons with multiple rings, the first must be the exterior
# ring and any others must be interior rings or holes.
def orient_polygon_coords(coords):
    oriented_esri_coords = []
    for i in range(0, len(coords)):
        poly = Polygon(coords[i])
        # Orient the first poly clock-wise (exterior ring)
        if i == 0:
            c = list(orient(poly, sign=-1.0).exterior.coords)
        else:
            c = list(orient(poly).exterior.coords)
        oriented_esri_coords.append(c)
    return oriented_esri_coords
