# -*- coding: utf-8 -*-

import re

from pyramid.view import view_config
import pyramid.httpexceptions as exc

from shapely.geometry import box, Point

from chsdi.lib.validation.search import SearchValidation
from chsdi.lib.helpers import format_search_text, transformCoordinate
from chsdi.lib.sphinxapi import sphinxapi
from chsdi.lib import mortonspacekey as msk


class Search(SearchValidation):

    LIMIT = 50
    LAYER_LIMIT = 30
    FEATURE_LIMIT = 20
    FEATURE_GEO_LIMIT = 200

    def __init__(self, request):
        super(Search, self).__init__()
        self.quadtree = msk.QuadTree(
            msk.BBox(420000, 30000, 900000, 510000), 20)
        self.sphinx = sphinxapi.SphinxClient()
        self.sphinx.SetServer(request.registry.settings['sphinxhost'], 9312)
        self.sphinx.SetMatchMode(sphinxapi.SPH_MATCH_EXTENDED)

        self.mapName = request.matchdict.get('map')
        self.hasMap(request.db, self.mapName)
        self.lang = request.lang
        self.cbName = request.params.get('callback')
        self.bbox = request.params.get('bbox')
        self.returnGeometry = request.params.get('returnGeometry', 'true').lower() == 'true'
        self.quadindex = None
        self.origins = request.params.get('origins')
        self.featureIndexes = request.params.get('features')
        self.timeInstant = request.params.get('timeInstant')
        self.timeEnabled = request.params.get('timeEnabled')
        self.timeStamps = request.params.get('timeStamps')
        self.typeInfo = request.params.get('type')
        self.varnish_authorized = request.headers.get('X-SearchServer-Authorized', 'false').lower() == 'true'

        self.geodataStaging = request.registry.settings['geodata_staging']
        self.results = {'results': []}
        self.request = request

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
        elif self.typeInfo in ('features', 'featureidentify'):
            # search all features within bounding box
            self._feature_bbox_search()
        elif self.typeInfo == 'featuresearch':
            # search all features using searchText
            self.searchText = format_search_text(
                self.request.params.get('searchText')
            )
            self._feature_search()
        elif self.typeInfo == 'locations':
            self.searchText = format_search_text(
                self.request.params.get('searchText', '')
            )
            # swiss search
            self._swiss_search()
        return self.results

    def _swiss_search(self):
        if len(self.searchText) < 1 and self.bbox is None:
            raise exc.HTTPBadRequest('You must at least provide a bbox or a searchText parameter')

        self.sphinx.SetLimits(0, self.LIMIT)

        # Define ranking mode
        if self.bbox is not None:
            geoAnchor = self._get_geoanchor_from_bbox()
            self.sphinx.SetGeoAnchor('lat', 'lon', geoAnchor.GetY(), geoAnchor.GetX())
            self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, '@geodist ASC')
        else:
            self.sphinx.SetRankingMode(sphinxapi.SPH_RANK_WORDCOUNT)
            self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, 'rank ASC, @weight DESC, num ASC')

        # Filter by origins if needed
        if self.origins is None:
            self._detect_keywords()
        else:
            self._filter_locations_by_origins()

        searchList = []
        if len(self.searchText) >= 1:
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
                temp = self.sphinx.Query(searchTextFinal, index='swisssearch')
            except IOError:
                raise exc.HTTPGatewayTimeout()
            temp = temp['matches'] if temp is not None else temp

            # if standard index did not find anything, use soundex/metaphon indices
            # which should be more fuzzy in its results
            if temp is None or len(temp) <= 0:
                try:
                    temp = self.sphinx.Query(searchTextFinal, index='swisssearch_fuzzy')
                except IOError:
                    raise exc.HTTPGatewayTimeout()
                temp = temp['matches'] if temp is not None else temp
        else:
            temp = []
        if temp is not None and len(temp) != 0:
            self._parse_location_results(temp)

    def _layer_search(self):
        # 10 features per layer are returned at max
        self.sphinx.SetLimits(0, self.LAYER_LIMIT)
        self.sphinx.SetRankingMode(sphinxapi.SPH_RANK_WORDCOUNT)
        self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, '@weight DESC')
        index_name = 'layers_%s' % self.lang
        mapName = self.mapName if self.mapName != 'all' else ''
        # Whitelist hack
        if mapName in ('api'):
            topicFilter = 'api'
        else:
            topicFilter = '(%s | ech)' % mapName
        searchText = ' '.join((
            self._query_fields('@(detail,layer)'),
            '& @topics %s' % (topicFilter),  # Filter by to topic if string not empty, ech whitelist hack
            '& @staging prod'                  # Only layers in prod are searched
        ))
        try:
            temp = self.sphinx.Query(searchText, index=index_name)
        except IOError:
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
            return
        self.sphinx.SetLimits(0, self.FEATURE_LIMIT)
        self.sphinx.SetRankingMode(sphinxapi.SPH_RANK_WORDCOUNT)
        if self.bbox:
            geoAnchor = self._get_geoanchor_from_bbox()
            self.sphinx.SetGeoAnchor('lat', 'lon', geoAnchor.GetY(), geoAnchor.GetX())
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
        except IOError:
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
        centerX = (self.bbox[2] + self.bbox[0]) / 2
        centerY = (self.bbox[3] + self.bbox[1]) / 2
        wkt = 'POINT(%s %s)' % (centerX, centerY)
        return transformCoordinate(wkt, 21781, 4326)

    def _feature_bbox_search(self):
        self._check_timeparameters()

        timeFilter = {
            'type': None,
            'years': []
        }
        if self.quadindex is None:
            raise exc.HTTPBadRequest('Please provide a bbox parameter')

        if self.featureIndexes is None:
            raise exc.HTTPBadRequest('Please provide a parameter features')

        self.sphinx.SetLimits(0, self.FEATURE_GEO_LIMIT)

        if self.timeInstant is not None:
            timeFilter['type'] = 'instant'
            timeFilter['years'] = [self.timeInstant]
        elif self.timeStamps is not None:
            timeFilter['type'] = 'layers'
            timeFilter['years'] = self.timeStamps
        geoAnchor = self._get_geoanchor_from_bbox()
        self.sphinx.SetGeoAnchor('lat', 'lon', geoAnchor.GetY(), geoAnchor.GetX())
        self.sphinx.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, '@geodist ASC')

        geomFilter = self._get_quadindex_string()
        self._add_feature_queries(geomFilter, timeFilter)
        temp = self.sphinx.RunQueries()
        self._parse_feature_results(temp)

    def _query_fields(self, fields):
        exact_nondigit_prefix_digit = lambda x: ''.join((x, '*')) if x.isdigit() else x
        prefix_nondigit_exact_digit = lambda x: x if x.isdigit() else ''.join((x, '*'))
        prefix_match_all = lambda x: ''.join((x, '*'))
        infix_nondigit_prefix_digit = lambda x: ''.join((x, '*')) if x.isdigit() else ''.join(('*', x, '*'))

        exactAll = ' '.join(self.searchText)
        exactNonDigitPreDigit = ' '.join(
            map(exact_nondigit_prefix_digit, self.searchText))
        preNonDigitExactDigit = ' '.join(
            map(prefix_nondigit_exact_digit, self.searchText))
        preNonDigitPreDigit = ' '.join(
            map(prefix_match_all, self.searchText))
        infNonDigitPreDigit = ' '.join(
            map(infix_nondigit_prefix_digit, self.searchText))

        finalQuery = ' | '.join((
            '%s "^%s"' % (fields, exactAll),
            '%s "%s"' % (fields, exactAll),
            '%s "%s"~5' % (fields, exactAll),
            '%s "%s"' % (fields, exactNonDigitPreDigit),
            '%s "%s"~5' % (fields, exactNonDigitPreDigit),
            '%s "%s"' % (fields, preNonDigitExactDigit),
            '%s "%s"~5' % (fields, preNonDigitExactDigit),
            '%s "^%s"' % (fields, preNonDigitPreDigit),
            '%s "%s"' % (fields, preNonDigitPreDigit),
            '%s "%s"~5' % (fields, preNonDigitPreDigit),
            '%s "%s"' % (fields, infNonDigitPreDigit),
            '%s "%s"~5' % (fields, infNonDigitPreDigit)
        ))

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
        else:
            return None

    def _origins_to_ranks(self, origins):
        origin2Rank = {
            'zipcode': 1,
            'gg25': 2,
            'district': 3,
            'kantone': 4,
            'sn25': 5,
            'address': 6,
            'parcel': 10
        }
        buildRanksList = lambda x: origin2Rank[x]
        try:
            ranks = map(buildRanksList, origins)
        except KeyError:
            raise exc.HTTPBadRequest('Bad value(s) in parameter origins')
        return ranks

    def _detect_keywords(self):
        if len(self.searchText) > 0:
            PARCEL_KEYWORDS = ['parzelle:', 'parcelle:', 'parcella:', 'parcel:']
            ADDRESS_KEYWORDS = ['addresse:', 'adresse:', 'indirizzo:', 'address:']
            if any(x.lower() in (str.lower() for str in self.searchText) for x in PARCEL_KEYWORDS):
                # As one cannot apply filters on string attributes, we use the rank information
                self.sphinx.SetFilter('rank', self._origins_to_ranks(['parcel']))
                for i in reversed([i for i, x in enumerate(self.searchText) if x.lower() in (x.lower() for x in PARCEL_KEYWORDS)]):
                    del self.searchText[i]
            elif any(x.lower() in (str.lower() for str in self.searchText) for x in ADDRESS_KEYWORDS):
                self.sphinx.SetFilter('rank', self._origins_to_ranks(['address']))
                for i in reversed([i for i, x in enumerate(self.searchText) if x.lower() in (x.lower() for x in ADDRESS_KEYWORDS)]):
                    del self.searchText[i]

    def _filter_locations_by_origins(self):
        ranks = self._origins_to_ranks(self.origins)
        self.sphinx.SetFilter('rank', ranks)

    def _add_feature_queries(self, queryText, timeFilter):
        i = 0
        for index in self.featureIndexes:
            self.sphinx.ResetFiltersOnly()
            if timeFilter and self.timeEnabled is not None and self.timeEnabled[i]:
                if timeFilter['type'] == 'instant':
                    self.sphinx.SetFilter('year', timeFilter['years'])
                elif timeFilter['type'] == 'layers' and timeFilter['years'][i] is not None:
                    self.sphinx.SetFilter('year', [timeFilter['years'][i]])
                elif timeFilter['type'] == 'range':
                    self.sphinx.SetFilterRange('year', int(min(timeFilter['years'])), int(max(timeFilter['years'])))
            i += 1
            self.sphinx.AddQuery(queryText, index=str(index))

    def _parse_address(self, res):
        if not (self.varnish_authorized and self.returnGeometry):
            attrs2Del = ['x', 'y', 'lon', 'lat', 'geom_st_box2d']
            popAtrrs = lambda x: res.pop(x) if x in res else x
            map(popAtrrs, attrs2Del)
            return res
        return res

    def _parse_location_results(self, results):
        nb_address = 0
        for res in results:
            origin = res['attrs']['origin']
            layerBodId = self._origin_to_layerbodid(origin)
            if layerBodId is not None:
                res['attrs']['layerBodId'] = layerBodId
                res['attrs']['featureId'] = res['attrs']['feature_id']
            else:
                res['attrs'].pop('layerBodId', None)
            res['attrs'].pop('feature_id', None)
            if origin == 'address':
                if nb_address < 20:
                    if not self.bbox or self._bbox_intersection(self.bbox, res['attrs']['geom_st_box2d']):
                        res['attrs'] = self._parse_address(res['attrs'])
                        self.results['results'].append(res)
                        nb_address += 1
            else:
                if not self.bbox or self._bbox_intersection(self.bbox, res['attrs']['geom_st_box2d']):
                    self.results['results'].append(res)

    def _parse_feature_results(self, results):
        for i in range(0, len(results)):
            if 'error' in results[i]:
                if results[i]['error'] != '':
                    raise exc.HTTPNotFound(results[i]['error'])
            if results[i] is not None and 'matches' in results[i]:
                # Add results to the list
                for res in results[i]['matches']:
                    if 'feature_id' in res['attrs']:
                        res['attrs']['featureId'] = res['attrs']['feature_id']
                    if self.typeInfo == 'featuresearch' or not self.bbox or \
                            self._bbox_intersection(self.bbox, res['attrs']['geom_st_box2d']):
                        if res['attrs']['layer'] == 'ch.bfs.gebaeude_wohnungs_register':
                            res['attrs'] = self._parse_address(res['attrs'])
                        self.results['results'].append(res)

    def _get_quad_index(self):
        try:
            quadindex = self.quadtree\
                .bbox_to_morton(
                    msk.BBox(self.bbox[0],
                             self.bbox[1],
                             self.bbox[2],
                             self.bbox[3]))
            self.quadindex = quadindex if quadindex != '' else None
        except ValueError:
            self.quadindex = None

    def _bbox_intersection(self, ref, result):
        def _is_point(bbox):
            if bbox[0] == bbox[2] and bbox[1] == bbox[3]:
                return True
            else:
                return False
        try:
            refbox = box(ref[0], ref[1], ref[2], ref[3]) if not _is_point(ref) else Point(ref[0], ref[1])
            arr = map(float, result.replace('BOX(', '').replace(')', '')
                      .replace(',', ' ').split(' '))
            resbox = box(arr[0], arr[1], arr[2], arr[3]) if not _is_point(arr) else Point(arr[0], arr[1])
        except:
            # We bail with True to be conservative and
            # not exclude this geometry from the result
            # set. Only happens if result does not
            # have a bbox
            return True
        return refbox.intersects(resbox)
