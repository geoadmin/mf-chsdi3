<%def name="table_body_cadastral(c, lang, fallbackLang)">
    % if c['attributes']['ak'] in ['D','I','F','AUT']:
        <tr><td class="cell-left">${h.translate('No info outside CH and FL', lang)}</td><td></td></tr>
    % elif c['attributes']['ak'] == 'AG':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="https://www.ag.ch/app/agisviewer4/v1/html/agisviewer.htm?config=agis_geoportal_fs.json&basemap=base_landeskarten_sw&thema=176&xmin=${c['bboxlv03'][0]}&ymin=${c['bboxlv03'][1]}&xmax=${c['bboxlv03'][2]}&ymax=${c['bboxlv03'][3]}" target="_blank">AG</a></td></tr>
    % elif c['attributes']['ak'] == 'BS':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.stadtplan.bs.ch/geoviewer/index.php?theme=258&extent=${','.join(map(str,c['bboxlv03']))}&layers=parzplan_vektor_grau_1000,av_parzellen_labels" target="_blank">BS</a></td></tr>
    % elif c['attributes']['ak'] == 'BE':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://webmap.be-geo.ch/geodaten.php?lang=${lang}&recenter_bbox=${','.join(map(str,c['bboxlv03']))}" target="_blank">BE</a></td></tr>
    % elif c['attributes']['ak'] == 'FR':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://map.geo.fr.ch/?dataTheme=Mensuration officielle&extent=${','.join(map(str,c['bboxlv03']))}&lang=${fallbackLang}" target="_blank">FR</a></td></tr>
    % elif c['attributes']['ak'] == 'GE':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://ge.ch/carte/pro/?mapresources=CADASTRE&extent=${c['bboxlv95'][0]},${c['bboxlv95'][1]},${c['bboxlv95'][2]},${c['bboxlv95'][3]}" target="_blank">GE</a></td></tr>
    % elif c['attributes']['ak'] == 'GL':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="https://map.geo.gl.ch/Public?visibleLayers=CH-Rahmen,BBFlaechen_farbig,projektierte%20BBFlaechen,Flaechenelemente_farbig,Linienelemente,Punktelemente,Grundstuecke%20(Parzellen),Liegenschaftsnummern,Grenzpunkte,BB%20Namen,EO%20Namen,Grundbuecher,Hoheitsgrenzpunkte,Fixpunkte%20Kat%201%202%203,Flur-%20und%20Ortsnamen,Lokalisationen,Gebaeudeadressen&startExtent=${c['bboxlv03'][0]},${c['bboxlv03'][1]},${c['bboxlv03'][2]},${c['bboxlv03'][3]}" target="_blank">GL</a></td></tr>
    % elif c['attributes']['ak'] == 'JU':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="https://geo.jura.ch/theme/Cadastre?&map_x=${(c['bboxlv95'][0] + c['bboxlv95'][2])/2}&map_y=${(c['bboxlv95'][1] + c['bboxlv95'][3])/2}&map_zoom=8" target="_blank">JU</a></td></tr>
    % elif c['attributes']['ak'] == 'SH':
       <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.gis.sh.ch/GIS_SH/?idp=1&uid=1&pwd=&map=10&lan=de&typ=3&bmurl=Nav@g@98@u@West@g@2${c['clickCoordLv03'][0]}@u@Nord@g@1${c['clickCoordLv03'][1]}@u@B@g@600" target="_blank">SH</a></td></tr>
    % elif c['attributes']['ak'] == 'SZ':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="https://map.geo.sz.ch/?map_x=2${c['clickCoordLv03'][0]}&map_y=1${c['clickCoordLv03'][1]}&map_zoom=9&baselayer_opacity=70&baselayer_ref=ch.sz.ortsplan_farbig&tree_group_layers_grp_Geb_u_Anl_Gebaeude=&tree_group_layers_grp_Grenzen_Gemeindegrenzen=&tree_group_layers_grp_GS_Kat_Fixpunkte=ch.sz.a018.amtliche_vermessung.fixpunktkategorie3.hoeheposition,ch.sz.a018.amtliche_vermessung.fixpunktkategorie2.hoeheposition,ch.sz.a018.amtliche_vermessung.fixpunktkategorie1.hoeheposition,ch.sz.a018.amtliche_vermessung.fixpunktkategorie3.lageposition,ch.sz.a018.amtliche_vermessung.fixpunktkategorie2.lageposition,ch.sz.a018.amtliche_vermessung.fixpunktkategorie1.lageposition&tree_group_layers_grp_GS_Kat_Grenzpunkte=&tree_group_layers_grp_GS_Kat_Grundstuecke=ch.sz.a018.amtliche_vermessung.liegenschaften.liegenschaft&tree_enable_ch.swisstopo-vd.spannungsarme-gebiete=false&tree_group_layers_grp_GS_Kat_Toleranzstufen=&tree_group_layers_grp_GS_Kat_Vermessungsstandard=&tree_groups=grp_Geb_u_Anl_Gebaeude,grp_Grenzen_Gemeindegrenzen,grp_GS_Kat_Fixpunkte,grp_GS_Kat_Grenzpunkte,grp_GS_Kat_Grundstuecke,grp_GS_Kat_Spannungsarme_Gebiete_wmts,grp_GS_Kat_Toleranzstufen,grp_GS_Kat_Vermessungsstandard" target="_blank">SZ</a></td></tr>
    % elif c['attributes']['ak'] == 'SO':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://geoweb.so.ch/map/grundbuchplan-nf?startExtent=${','.join(map(str, c['bboxlv95']))}" target="_blank">SO</a></td></tr>
    % elif c['attributes']['ak'] == 'TI':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.sitmap.ti.ch/index.php?ct=mu95el" target="_blank">TI</a></td></tr>
    % elif c['attributes']['ak'] == 'VD':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.geo.vd.ch/theme/cadastre_thm?map_x=${c['clickCoordLv03'][0]}&map_y=${c['clickCoordLv03'][1]}&map_zoom=10" target="_blank">VD</a></td></tr>
    % elif c['attributes']['ak'] == 'TG':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://geo.tg.ch/mapbender/frames/login.php?gui_id=Amtliche%20Vermessung&mb_myBBOX=${','.join(map(str,c['bboxlv95']))}" target="_blank">TG</a></td></tr>
    % elif c['attributes']['ak'] == 'NE':
        <tr><td width="150">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://sitn.ne.ch/theme/cadastre?map_x=2${c['clickCoordLv03'][0]}&map_y=1${c['clickCoordLv03'][1]}&map_zoom=10" target="_blank">NE</a></td></tr>
    % elif c['attributes']['ak'] == 'LU':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.geo.lu.ch/map/grundbuchplan/?FOCUS=${c['clickCoordLv95'][0]}:${c['clickCoordLv95'][1]}:${c['scale']}" target="_blank">LU</a></td></tr>
    % elif c['attributes']['ak'] == 'OW':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://map.gis-daten.ch/ow_oereb?xmin=${c['bboxlv03'][0]}&ymin=${c['bboxlv03'][1]}&xmax=${c['bboxlv03'][2]}&ymax=${c['bboxlv03'][3]}" target="_blank">OW</a></td></tr>
    % elif c['attributes']['ak'] == 'NW':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://map.gis-daten.ch/nw_oereb?xmin=${c['bboxlv03'][0]}&ymin=${c['bboxlv03'][1]}&xmax=${c['bboxlv03'][2]}&ymax=${c['bboxlv03'][3]}" target="_blank">NW</a></td></tr>
    % elif c['attributes']['ak'] == 'UR':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://geo.ur.ch/" target="_blank">UR</a></td></tr>
    % elif c['attributes']['ak'] == 'GR':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://geogr.mapserver.ch/shop" target="_blank">GR</a></td></tr>
    % elif c['attributes']['ak'] == 'AI':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.ai.ch" target="_blank">AI</a></td></tr>
    % elif c['attributes']['ak'] == 'AR':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.ar.ch" target="_blank">AR</a></td></tr>
    % elif c['attributes']['ak'] == 'ZH':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://maps.zh.ch/?topic=AVfarbigwwwZH&scale=${c['scale']}&x=${c['clickCoordLv95'][0]}&y=${c['clickCoordLv95'][1]}&offlayers=LCOBJPROJ%2Cbezirkslabels" target="_blank">ZH</a></td></tr>
    % elif c['attributes']['ak'] == 'BL':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://geoview.bl.ch/?map_x=${c['clickCoordLv95'][0]}&map_y=${c['clickCoordLv95'][1]}&map_zoom=9" target="_blank">BL</a></td></tr>
    % elif c['attributes']['ak'] == 'ZG':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="http://www.zugmap.ch/zugmap/?idp=1&uid=1&pwd=&map=1&lan=de&typ=3&bmurl=Nav@g@22@u@West@g@${c['clickCoordLv03'][0]}@u@Nord@g@${c['clickCoordLv03'][1]}@u@B@g@${c['scale']}&dat=fs@g@0:371167b2bf7dfc4b,c7bfc487a7a729d3,9d1d191f82fb57e3,1fb440cdc612de80,4119ae2a85acc4b5,b7b8c26dbec351a9!!" target="_blank">ZG</a></td></tr>
    % elif c['attributes']['ak'] == 'SG':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="https://www.sg.ch/home/bauen__raum___umwelt/aktuelles_energie/Baugesuch/Geoportal.html" target="_blank">SG</a></td></tr>
    % elif c['attributes']['ak'] == 'VS':
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td><a href="https://sitonline.vs.ch/urbanisation/mo/${fallbackLang}/" target="_blnk">VS</a></td></br>
    % elif c['attributes']['ak'] == 'FL':
        <tr><td class="cell-left">${h.translate('link to geoportal', lang)}</td><td><a href="http://geodaten.llv.li/geoshop/public.html?zoombox=${c['bboxlv95'][0]},${c['bboxlv95'][1]},${c['bboxlv95'][2]},${c['bboxlv95'][3]}" target="_blank">${h.translate('FL', lang)}</a></td></tr>
    % else:
        <tr><td class="cell-left">${h.translate('link to canton geoportal', lang)}</td><td>${h.translate('Canton has provided no link to portal', lang)}</td></tr>
    % endif
    <tr><td class="cell-left">${h.translate('cwm_number', lang)}</td><td>${c['attributes']['number'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('cwm_egris_egrid', lang)}</td><td>${c['attributes']['egris_egrid'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('cwm_realestate_type'), lang}</td><td>${h.translate(('cwm_realestate_type_{}'.format(c['attributes']['realestate_type']) if c['attributes']['realestate_type'] >=0 else 'cwm_realestate_type_default'), lang)}</td></tr>
</%def>

