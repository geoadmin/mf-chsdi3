# -*- coding: utf-8 -*-

import re
import six
import pyramid.httpexceptions as exc
from pyramid.view import view_config

from shapely.geometry import box, Point, mapping

from chsdi.lib.validation.search import SearchValidation
from chsdi.lib.helpers import format_search_text, format_locations_search_text
from chsdi.lib.helpers import _transform_point as transform_coordinate, parse_box2d, shift_to, ilen
from chsdi.lib.helpers import center_from_box2d, transform_round_geometry as transform_shape
from chsdi.lib.sphinxapi import sphinxapi
from chsdi.lib import mortonspacekey as msk


class Search(SearchValidation):

    LOCATION_LIMIT = 50
    LAYER_LIMIT = 30
    FEATURE_LIMIT = 20
    DEFAULT_SRID = 21781
    BBOX_SEARCH_LIMIT = 150

    def __init__(self, request):
        super(Search, self).__init__(request)

        self.mapName = request.matchdict.get('map')
        self.hasMap(request.db, self.mapName)
        self.lang = request.lang
        self.searchLang = request.params.get('searchLang')
        self.cbName = request.params.get('callback')
        # Order matters define srid first
        self.srid = request.params.get('sr', str(self.DEFAULT_SRID))
        self.bbox = request.params.get('bbox')
        self.sortbbox = request.params.get('sortbbox', 'true').lower() == 'true'
        self.returnGeometry = request.params.get('returnGeometry', 'true').lower() == 'true'
        self.quadindex = None
        self.origins = request.params.get('origins')
        self.featureIndexes = request.params.get('features')
        self.timeInstant = request.params.get('timeInstant')
        self.timeEnabled = request.params.get('timeEnabled')
        self.timeStamps = request.params.get('timeStamps')
        self.typeInfo = request.params.get('type')
        self.limit = request.params.get('limit')

        self.geodataStaging = request.registry.settings['geodata_staging']
        self.results = {'results': []}
        self.request = request

        morton_box = [420000, 30000, 900000, 510000]
        self.quadtree = msk.QuadTree(
            msk.BBox(*morton_box), 20)
        self.sphinx = sphinxapi.SphinxClient()
        self.sphinx.SetServer(request.registry.settings['sphinxhost'], 9312)
        self.sphinx.SetMatchMode(sphinxapi.SPH_MATCH_EXTENDED)

    @view_config(route_name='search', renderer='geojson',
                 request_param='geometryFormat=geojson')
    def view_find_geojson(self):
        (features, bbox) = self._find_geojson()
        bounds = bbox.bounds if bbox is not None else None
        return {"type": "FeatureCollection", "bbox": bounds, "features": features}

    @view_config(route_name='search', renderer='esrijson',
                 request_param='geometryFormat=esrijson')
    def view_find_esrijson(self):
        raise exc.HTTPBadRequest("Param 'geometryFormat=esrijson' is not supported")

    def _find_geojson(self):
        features = []
        features_bbox = None
        for item in self.search()['results']:
            if 'attrs' in item and 'id' in item and 'weight' in item:
                attributes = item['attrs']
                attributes['id'] = item['id']
                attributes['weight'] = item['weight']
                if attributes['origin'] != 'layer':
                    # Already reprojected
                    bounds = parse_box2d(attributes['geom_st_box2d'])
                else:
                    try:
                        # TODO: This is the requested QuadTree, because sphinx layer indices do not have extent
                        bounds = self.quadtree.bbox.bounds
                        bounds = transform_shape(bounds, self.DEFAULT_SRID, self.srid)
                    except ValueError:
                        raise exc.HTTPInternalServerError("Search error: cannot reproject result to SRID: {}".format(self.srid))
                bbox = box(*bounds)
                if features_bbox is None:
                    features_bbox = bbox
                else:
                    features_bbox.union(bbox)
                if 'x' in attributes.keys() and 'y' in attributes.keys():
                    feature = {'type': 'Feature',
                               'id': item['id'],
                               'bbox': bbox.bounds,
                               'geometry': {'type': 'Point', 'coordinates': [attributes['x'], attributes['y']]},
                               'properties': attributes}
                else:
                    feature = {'type': 'Feature',
                               'id': item['id'],
                               'bbox': bbox.bounds,
                               'geometry': mapping(bbox),
                               'properties': attributes}

                features.append(feature)
        return (features, features_bbox)

    @view_config(route_name='search', renderer='jsonp')
    def search(self):
        self.sphinx.SetConnectTimeout(10.0)
        # create a quadindex if the bbox is defined
        if self.bbox is not None and self.typeInfo not in ('layers', 'featuresearch'):
            self._get_quad_index()
        if self.typeInfo == 'layers':
            # search all layers
            self.searchText = format_search_text(
                self.request.params.get('searchText')
            )
            self._layer_search()
        elif self.typeInfo == 'featuresearch':
            # search all features using searchText
            self.searchText = format_search_text(
                self.request.params.get('searchText')
            )
            self._feature_search()
        elif self.typeInfo in ('locations'):
            self.searchText = format_locations_search_text(
                self.request.params.get('searchText', '')
            )
            # swiss search
            self._swiss_search()
            # translate some gazetteer categories from swissnames3 tagged with <i>...</i> in the label attribute of the response
        return self.results

    def _fuzzy_search(self, searchTextFinal):
        # We use different ranking for fuzzy search
        # For ranking modes, see http://sphinxsearch.com/docs/current.html#weighting
        self.sphinx.SetRankingMode(sphinxapi.SPH_RANK_SPH04)
        # Only include results with a certain weight. This might need tweaking
        self.sphinx.SetFilterRange('@weight', 5000, 2 ** 32 - 1)
        try:
            if self.typeInfo in ('locations'):
                temp = self.sphinx.Query(searchTextFinal, index='swisssearch_fuzzy')
        except IOError:  # pragma: no cover
            raise exc.HTTPGatewayTimeout()
        temp = temp['matches'] if temp is not None else temp
        self.results['fuzzy'] = 'true'
        return temp

    def _swiss_search(self):
        limit = self.limit if self.limit and self.limit <= self.LOCATION_LIMIT else self.LOCATION_LIMIT
        # Define ranking mode
        if self.bbox is not None and self.sortbbox:
            coords = self._get_geoanchor_from_bbox()
            self.sphinx.SetGeoAnchor('lat', 'lon', coords[1], coords[0])
            self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, '@geodist ASC')
            limit = self.BBOX_SEARCH_LIMIT
        else:
            self.sphinx.SetRankingMode(sphinxapi.SPH_RANK_WORDCOUNT)
            self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, 'rank ASC, @weight DESC, num ASC')

        self.sphinx.SetLimits(0, limit)

        # Filter by origins if needed
        if self.origins is None:
            self._detect_keywords()
        else:
            self._filter_locations_by_origins()

        searchList = []
        if ilen(self.searchText) >= 1:
            searchText = self._query_fields('@detail')
            searchList.append(searchText)

        if self.bbox is not None:
            geomFilter = self._get_quadindex_string()
            searchList.append(geomFilter)

        if len(searchList) == 2:
            searchTextFinal = '(' + searchList[0] + ') & (' + searchList[1] + ')'
        elif len(searchList) == 1:
            searchTextFinal = searchList[0]

        if len(searchList) != 0:
            try:
                # wildcard search only if more than one character in searchtext
                if len(' '.join(self.searchText)) > 1 or self.bbox:
                    # standard wildcard search
                    self.sphinx.AddQuery(searchTextFinal, index='swisssearch')

                # exact search, first 10 results
                searchText = '@detail ^%s' % ' '.join(self.searchText)
                self.sphinx.AddQuery(searchText, index='swisssearch')

                # reset settings
                temp = self.sphinx.RunQueries()

                # In case RunQueries doesn't return results (reason unknown)
                # related to issue
                if temp is None:
                    raise exc.HTTPServiceUnavailable('no results from sphinx service (%s)' % self.sphinx._error)

            except IOError:  # pragma: no cover
                raise exc.HTTPGatewayTimeout()

            temp_merged = temp[0].get('matches', []) + temp[1].get('matches', []) if len(temp) == 2 else temp[0].get('matches', [])

            # remove duplicate results, exact search results have priority over wildcard search results
            temp = []
            seen = []
            for d in temp_merged:
                if d['id'] not in seen:
                    temp.append(d)
                    seen.append(d['id'])

            # reduce number of elements in result to limit
            temp = temp[:limit]

            # if standard index did not find anything, use soundex/metaphon indices
            # which should be more fuzzy in its results
            if temp is None or len(temp) <= 0:
                temp = self._fuzzy_search(searchTextFinal)
        else:
            temp = []
        if temp is not None and len(temp) != 0:
            self._parse_location_results(temp, limit)

    def _layer_search(self):

        def staging_filter(staging):
            ret = '@staging prod'
            if staging == 'integration' or staging == 'test':
                ret += ' | @staging integration'
                if staging == 'test':
                    ret += ' | @staging test'
            return ret

        # 10 features per layer are returned at max
        layerLimit = self.limit if self.limit and self.limit <= self.LAYER_LIMIT else self.LAYER_LIMIT
        self.sphinx.SetLimits(0, layerLimit)
        self.sphinx.SetRankingMode(sphinxapi.SPH_RANK_WORDCOUNT)
        self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, '@weight DESC')
        # Weights defaults to 1
        self.sphinx.SetFieldWeights({
            '@title': 4,
            '@detail': 2,
            '@layer': 1
        })

        index_name = 'layers_%s' % self.lang
        mapName = self.mapName if self.mapName != 'all' else ''
        # Whitelist hack
        if mapName in ('api'):
            topicFilter = 'api'
        else:
            topicFilter = '(%s | ech)' % mapName
        searchText = ' '.join((
            self._query_fields('@(title,detail,layer)'),
            '& @topics %s' % (topicFilter),  # Filter by to topic if string not empty, ech whitelist hack
            '& %s' % (staging_filter(self.geodataStaging))  # Only layers in correct staging are searched
        ))
        try:
            temp = self.sphinx.Query(searchText, index=index_name)
        except IOError:  # pragma: no cover
            raise exc.HTTPGatewayTimeout()
        temp = temp['matches'] if temp is not None else temp
        if temp is not None and len(temp) != 0:
            self.results['results'] += temp

    def _get_quadindex_string(self):
        ''' Recursive and inclusive search through
            quadindex windows. '''
        if self.quadindex is not None:
            buildQuadQuery = lambda x: ''.join(('@geom_quadindex ', x, ' | '))
            if len(self.quadindex) == 1:
                quadSearch = ''.join(('@geom_quadindex ', self.quadindex, '*'))
            else:
                quadSearch = ''.join(('@geom_quadindex ', self.quadindex, '* | '))
                quadSearch += ''.join(
                    buildQuadQuery(self.quadindex[:-x])
                    for x in range(1, len(self.quadindex))
                )[:-len(' | ')]
            return quadSearch
        return ''

    def _feature_search(self):

        # all features in given bounding box
        if self.featureIndexes is None:
            # we need bounding box and layernames. FIXME: this should be error
            raise exc.HTTPBadRequest('Bad request: no layername given')
        featureLimit = self.limit if self.limit and self.limit <= self.FEATURE_LIMIT else self.FEATURE_LIMIT
        self.sphinx.SetLimits(0, featureLimit)
        self.sphinx.SetRankingMode(sphinxapi.SPH_RANK_WORDCOUNT)
        if self.bbox and self.sortbbox:
            coords = self._get_geoanchor_from_bbox()
            self.sphinx.SetGeoAnchor('lat', 'lon', coords[1], coords[0])
            self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, '@weight DESC, @geodist ASC')
        else:
            self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, '@weight DESC')

        timeFilter = self._get_time_filter()
        if self.searchText:
            searchdText = self._query_fields('@detail')
        else:
            searchdText = ''
        self._add_feature_queries(searchdText, timeFilter)
        try:
            temp = self.sphinx.RunQueries()
        except IOError:  # pragma: no cover
            raise exc.HTTPGatewayTimeout()
        self.sphinx.ResetFilters()
        self._parse_feature_results(temp)

    def _get_time_filter(self):
        self._check_timeparameters()
        years = []
        t = None
        timeInterval = re.search(r'((\b\d{4})-(\d{4}\b))', ' '.join(self.searchText)) or False
        # search for year with getparameter timeInstant=2010
        if self.timeInstant is not None:
            years = [self.timeInstant]
            t = 'instant'
        elif self.timeStamps is not None:
            years = self.timeStamps
            t = 'layers'
        # search for year interval with searchText Pattern .*YYYY-YYYY.*
        elif timeInterval:
            numbers = [timeInterval.group(2), timeInterval.group(3)]
            start = min(numbers)
            stop = max(numbers)
            # remove time intervall from searchtext
            self.searchText.remove(timeInterval.group(1))
            if min != max:
                t = 'range'
                years = [start, stop]
        return {
            'type': t,
            'years': years
        }

    def _check_timeparameters(self):
        if self.timeInstant is not None and self.timeStamps is not None:
            raise exc.HTTPBadRequest('You are not allowed to mix timeStamps and timeInstant parameters')

    def _get_geoanchor_from_bbox(self):
        center = center_from_box2d(self.bbox)
        return transform_coordinate(center, self.DEFAULT_SRID, 4326)

    def _query_fields(self, fields):
        # 10a, 10b needs to be interpreted as digit
        q = []
        isdigit = lambda x: bool(re.match('^[0-9]', x))
        hasDigit = bool(len([x for x in self.searchText if isdigit(x)]) > 0)
        hasNonDigit = bool(len([x for x in self.searchText if not isdigit(x)]) > 0)

        prefix_non_digit = lambda x: x if isdigit(x) else ''.join((x, '*'))
        infix_non_digit = lambda x: x if isdigit(x) else ''.join(('*', x, '*'))

        if hasNonDigit:
            exactAll = ' '.join(self.searchText)
            preNonDigit = ' '.join([prefix_non_digit(w) for w in self.searchText])
            infNonDigit = ' '.join([infix_non_digit(w) for w in self.searchText])
            q = [
                '%s "%s"'    % (fields, exactAll),
                '%s "^%s"'   % (fields, exactAll),
                '%s "%s$"'   % (fields, exactAll),
                '%s "^%s$"'  % (fields, exactAll),
                '%s "%s"~5'  % (fields, exactAll),
                '%s "%s"'    % (fields, preNonDigit),
                '%s "^%s"'   % (fields, preNonDigit),
                '%s "%s"~5'  % (fields, preNonDigit),
                '%s "%s"'    % (fields, infNonDigit),
                '%s "^%s"'   % (fields, infNonDigit),
                '%s "%s"~5'  % (fields, infNonDigit)
            ]

        if hasDigit:
            prefix_digit = lambda x: x if not isdigit(x) else ''.join((x, '*'))
            prefix_all = lambda x: ''.join((x, '*'))
            preDigit = ' '.join([prefix_digit(w) for w in self.searchText])
            preNonDigitAndPreDigit = ' '.join([prefix_all(w) for w in self.searchText])
            infNonDigitAndPreDigit = ' '.join([prefix_digit(infix_non_digit(w)) for w in self.searchText])
            q = q + [
                '%s "%s"'   % (fields, preDigit),
                '%s "^%s"'  % (fields, preDigit),
                '%s "%s"'   % (fields, preNonDigitAndPreDigit),
                '%s "%s"~5' % (fields, preNonDigitAndPreDigit),
                '%s "%s"'   % (fields, infNonDigitAndPreDigit)
            ]
        finalQuery = ' | '.join(q)
        return finalQuery

    def _origin_to_layerbodid(self, origin):
        origins2LayerBodId = {
            'zipcode': 'ch.swisstopo-vd.ortschaftenverzeichnis_plz',
            'gg25': 'ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill',
            'district': 'ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill',
            'kantone': 'ch.swisstopo.swissboundaries3d-kanton-flaeche.fill',
            'address': 'ch.bfs.gebaeude_wohnungs_register'
        }
        if origin in origins2LayerBodId:
            return origins2LayerBodId[origin]
        return None

    def _origins_to_ranks(self, origins):
        origin2Rank = {
            'zipcode': [1],
            'gg25': [2],
            'district': [3],
            'kantone': [4],
            'gazetteer': [5, 6],  # Not used, also 7
            'address': [7],
            'hatestellen': [8],
            'parcel': [10]
        }
        ranks = []
        try:
            for origin in origins:
                ranks += origin2Rank[origin]
        except KeyError:  # pragma: no cover
            raise exc.HTTPBadRequest('Bad value(s) in parameter origins')
        return ranks

    def _search_lang_to_filter(self):
        return {
            'de': [1],
            'fr': [2],
            'it': [3],
            'rm': [4]
        }[self.searchLang]

    def _detect_keywords(self):
        if ilen(self.searchText) > 0:
            PARCEL_KEYWORDS = ('parzelle', 'parcelle', 'parcella', 'parcel')
            ADDRESS_KEYWORDS = ('addresse', 'adresse', 'indirizzo', 'address')
            firstWord = self.searchText[0].lower()
            if firstWord in PARCEL_KEYWORDS:
                # As one cannot apply filters on string attributes, we use the rank information
                self.sphinx.SetFilter('rank', self._origins_to_ranks(['parcel']))
                del self.searchText[0]
            elif firstWord in ADDRESS_KEYWORDS:
                self.sphinx.SetFilter('rank', self._origins_to_ranks(['address']))
                del self.searchText[0]

    def _filter_locations_by_origins(self):
        ranks = self._origins_to_ranks(self.origins)
        self.sphinx.SetFilter('rank', ranks)

    def _add_feature_queries(self, queryText, timeFilter):
        translated_layer = 'ch_bfs_gebaeude_wohnungs_register'
        for i, index in enumerate(self.featureIndexes):
            self.sphinx.ResetFiltersOnly()
            if timeFilter and self.timeEnabled is not None and self.timeEnabled[i]:
                if timeFilter['type'] == 'instant':
                    self.sphinx.SetFilter('year', timeFilter['years'])
                elif timeFilter['type'] == 'layers' and timeFilter['years'][i] is not None:
                    self.sphinx.SetFilter('year', [timeFilter['years'][i]])
                elif timeFilter['type'] == 'range':
                    self.sphinx.SetFilterRange('year', int(min(timeFilter['years'])), int(max(timeFilter['years'])))
            if index.startswith(translated_layer):
                if self.searchLang:
                    self.sphinx.SetFilter('lang', self._search_lang_to_filter())
                else:
                    self.sphinx.SetFilter('agnostic', [1])
                self.sphinx.AddQuery(queryText, index=translated_layer)
            else:
                if self.searchLang:
                    raise exc.HTTPBadRequest('Parameter seachLang is not supported for %s' % index)
                self.sphinx.AddQuery(queryText, index=str(index))

    def _box2d_transform(self, res):
        """Reproject a ST_BOX2 from EPSG:21781 to SRID"""
        try:
            box2d = res['geom_st_box2d']
            box_str = box2d[4:-1]
            b = map(float, re.split(' |,', box_str))
            shape = box(*b)
            bbox = transform_shape(shape, self.DEFAULT_SRID, self.srid).bounds
            res['geom_st_box2d'] = "BOX({} {},{} {})".format(*bbox)
        except Exception:
            raise exc.HTTPInternalServerError('Error while converting BOX2D to EPSG:{}'.format(self.srid))
        return res

    def _parse_locations(self, res):

        if not self.returnGeometry:
            attrs2Del = ['x', 'y', 'lon', 'lat', 'geom_st_box2d']
            popAtrrs = lambda x: res.pop(x) if x in res else x
            # Python2/3
            if six.PY2:
                map(popAtrrs, attrs2Del)
            else:
                list(map(popAtrrs, attrs2Del))
        elif int(self.srid) not in (21781, 2056):
            self._box2d_transform(res)
            if int(self.srid) == 4326:
                try:
                    res['x'] = res['lon']
                    res['y'] = res['lat']
                except KeyError:
                    raise exc.HTTPInternalServerError('Sphinx location has no lat/long defined')
            else:
                try:
                    pnt = (res['y'], res['x'])
                    x, y = transform_coordinate(pnt, self.DEFAULT_SRID, self.srid)
                    res['x'] = x
                    res['y'] = y
                except Exception:
                    raise exc.HTTPInternalServerError('Error while converting point(x, y) to EPSG:{}'.format(self.srid))
        return res

    def _parse_location_results(self, results, limit):
        nb_address = 0
        for result in self._yield_matches(results):
            origin = result['attrs']['origin']
            layer_bod_id = self._origin_to_layerbodid(origin)
            if layer_bod_id is not None:
                result['attrs']['layerBodId'] = layer_bod_id
                # Backward compatible
                result['attrs']['featureId'] = result['attrs']['feature_id']
                result['attrs'].pop('layerBodId', None)
            result['attrs'].pop('feature_id', None)
            result['attrs']['label'] = self._translate_label(result['attrs']['label'])
            if (origin == 'address'
                and nb_address < self.LOCATION_LIMIT
                and (not self.bbox or self._bbox_intersection(self.bbox,
                                                         result['attrs']['geom_st_box2d']))):
                result['attrs'] = self._parse_locations(result['attrs'])
                self.results['results'].append(result)
                nb_address += 1
            else:
                if not self.bbox or self._bbox_intersection(self.bbox,
                                                            result['attrs']['geom_st_box2d']):
                    self._parse_locations(result['attrs'])
                    self.results['results'].append(result)
        if len(self.results['results']) > 0:
            self.results['results'] = self.results['results'][:limit]

    def _parse_feature_results(self, results):
        for idx, result in self._yield_results(results):
            if 'error' in result:
                if result['error'] != '':
                    raise exc.HTTPNotFound(result['error'])  # pragma: no cover
            if result is not None and 'matches' in result:
                for match in self._yield_matches(result['matches']):
                    # Backward compatible
                    if 'feature_id' in match['attrs']:
                        match['attrs']['featureId'] = match['attrs']['feature_id']
                    # lang and agnostic in combination with searchLang
                    if 'lang' in match['attrs']:
                        del match['attrs']['lang']
                    if 'agnostic' in match['attrs']:
                        del match['attrs']['agnostic']
                    if not self.bbox or self._bbox_intersection(self.bbox, match['attrs']['geom_st_box2d']):
                        self.results['results'].append(match)

    def _yield_results(self, results):
        for idx, result in enumerate(results):
            yield idx, result

    def _yield_matches(self, matches):
        for match in matches:
            yield self._choose_srid(match)

    def _choose_srid(self, match):
        geom_entries = ['geom_st_box2d', 'x', 'y']
        if self.srid == 2056:
            for geom_entry in geom_entries:
                match = self._choose_lv95_coords(match, geom_entry)
        else:
            for geom_entry in geom_entries:
                geom_entry = '%s_lv95' % geom_entry
                if geom_entry in match['attrs']:
                    del match['attrs'][geom_entry]
        return match

    def _choose_lv95_coords(self, match, prefix):
        attr = '%s_lv95' % prefix
        if attr in match['attrs']:
            match['attrs'][prefix] = match['attrs'][attr]
            del match['attrs'][attr]
        return match

    def _translate_label(self, label):
        translation = re.search(r'.*(<i>[\s\S]*?<\/i>).*', label) or False
        if translation:
            translated = self.request.translate(translation.group(1))
            label = label.replace(translation.group(1),
                                  u'<i>{}</i>'.format(translated))

        return label

    def _get_quad_index(self):
        try:
            quadindex = self.quadtree\
                .bbox_to_morton(
                    msk.BBox(self.bbox[0],
                             self.bbox[1],
                             self.bbox[2],
                             self.bbox[3]))
            self.quadindex = quadindex if quadindex != '' else None
        except ValueError:  # pragma: no cover
            self.quadindex = None

    def _bbox_intersection(self, ref, result):
        def _is_point(bbox):
            return bbox[0] == bbox[2] and bbox[1] == bbox[3]
        # We always keep the bbox in 21781
        if self.srid == 2056:
            ref = shift_to(ref, 2056)
        try:
            refbox = box(ref[0], ref[1], ref[2], ref[3]) if not _is_point(ref) else Point(ref[0], ref[1])
            arr = parse_box2d(result)
            resbox = box(arr[0], arr[1], arr[2], arr[3]) if not _is_point(arr) else Point(arr[0], arr[1])
        except Exception:  # pragma: no cover
            # We bail with True to be conservative and
            # not exclude this geometry from the result
            # set. Only happens if result does not
            # have a bbox
            return True
        return refbox.intersects(resbox)
