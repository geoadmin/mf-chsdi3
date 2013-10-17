# -*- coding: utf-8 -*-


<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    % if c['attributes']['ak'] in ['D','I','F','AUT']:
        <tr><td width="150">${_('No info outside CH and FL')}</td><td></td></tr>
    % elif c['attributes']['ak'] == 'AG':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="https://www.ag.ch/app/agisviewer4/v1/html/agisviewer.htm?config=agis_geoportal_fs.json&basemap=base_landeskarten_sw&thema=176&xmin=${c['bbox'][0]}&ymin=${c['bbox'][1]}&xmax=${c['bbox'][2]}&ymax=${c['bbox'][3]}" target="_blank">AG</a></td></tr>
    % elif c['attributes']['ak'] == 'BS':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.stadtplan.bs.ch/geoviewer/index.php?theme=258&extent=${','.join(map(str,c['bbox']))}&layers=parzplan_vektor_grau_1000,av_parzellen_labels" target="_blank">BS</a></td></tr>
    % elif c['attributes']['ak'] == 'BE':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://webmap.be-geo.ch/geodaten.php?lang=${c.lang}&recenter_bbox=${','.join(map(str,c['bbox']))}" target="_blank">BE</a></td></tr>
    % elif c['attributes']['ak'] == 'FR':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.geo.fr.ch/index.php?reset_session&linkit=1&switch_id=switch_localisation&layer_select=Adresses,ParcVect,ParcVectnum,GrpMasque,GrpSituation,FondPlanContinu,copyright,Parcellaire,ParcScan&mapsize=0&recenter_bbox=${','.join(map(str,c['bbox']))}" target="_blank">FR</a></td></tr>
    % elif c['attributes']['ak'] == 'GE':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://etat.geneve.ch/geoportail/monsitg/?X=${c['bbox'][0] + 2000000}&Y=${c['bbox'][1] + 1000000}&SCALE=${c['scale']}" target="_blank">GE</a></td></tr>
    % elif c['attributes']['ak'] == 'GL':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://geo.gl.ch/maps/Public?visibleLayers=MOpublic" target="_blank">GL</a></td></tr>
    % elif c['attributes']['ak'] == 'JU':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://sitn.ne.ch/jura.php?Y=${c['bbox'][0]}&X=${c['bbox'][1]}&echelle=${c['scale'] if float(c['scale']) <=5000 else 5000}&theme=cadastre" target="_blank">JU</a></td></tr>
    % elif c['attributes']['ak'] == 'SH':   
       <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.gis.sh.ch/GIS_SH/?idp=1&uid=1&pwd=&map=10&lan=de&typ=3&bmurl=Nav@g@98@u@West@g@${c['bbox'][0]}@u@Nord@g@${c['bbox'][1]}@u@B@g@600" target="_blank">SH</a></td></tr>
    % elif c['attributes']['ak'] == 'SZ':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://webmap.sz.ch/bm31_webmap/?idp=1&uid=3&bmurl=Nav@g@129@u@West@g@${c['bbox'][0]}@u@Nord@g@${c['bbox'][1]}@u@B@g@${c['scale']}" target="_blank">SZ</a></td></tr>
    % elif c['attributes']['ak'] == 'SO':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.sogis1.so.ch/sogis/internet/pmapper/somap.php?karte=ortsplan&extent=${','.join(map(str,c['bbox']))}" target="_blank">SO</a></td></tr>
    % elif c['attributes']['ak'] == 'TI':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.sitinfo.ti.ch/WebsiteProd/htmlviewer/mu93pubblicoe?Box=${':'.join(map(str,c['bbox']))}" target="_blank">TI</a></td></tr>
    % elif c['attributes']['ak'] == 'VD':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.geoplanet.vd.ch/index.php?reset_session&linkit=1&switch_id=switch_cadastre&layer_select=complement_vd2,fond_continu_gris,canton_select,gc_mensuration_select,cad_parv_select,cad_parv_numero_select,ddp_select,ddp_npcs_select,cad_parv_plim_select,cad_bat_hs_cadastre_select,cad_bat_ss_select,npcs_bat_hs_select,npcs_bat_ss_select,couverture_sol,cad_cs_dur,cad_cs_vert,cad_cs_bois,cad_cs_eau,cad_cs_div&recenter_bbox=${','.join(map(str,c['bbox']))}&mapSize=4" target="_blank">VD</a></td></tr>
    % elif c['attributes']['ak'] == 'TG':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://geo.tg.ch/mapbender/frames/login.php?gui_id=Amtliche%20Vermessung&mb_myBBOX=${','.join(map(str,c['bbox']))}" target="_blank">TG</a></td></tr>
    % elif c['attributes']['ak'] == 'NE':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://sitn.ne.ch/mapfish/cadastre?map_x=${c['bbox'][0]}&map_y=${c['bbox'][1]}&map_zoom=12" target="_blank">NE</a></td></tr>
    % elif c['attributes']['ak'] == 'LU':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.geo.lu.ch/map/grundbuchplan/" target="_blank">LU</a></td></tr>
    % elif c['attributes']['ak'] == 'OW':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.gis-ow.ch" target="_blank">OW</a></td></tr>
    % elif c['attributes']['ak'] == 'NW':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.lis-nw.ch" target="_blank">NW</a></td></tr>
    % elif c['attributes']['ak'] == 'UR':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.lisag.ch/de/geoshop/geoshop-m458" target="_blank">UR</a></td></tr>
    % elif c['attributes']['ak'] == 'GR':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://geogr.mapserver.ch/shop" target="_blank">GR</a></td></tr>
    % elif c['attributes']['ak'] == 'AI':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.geoportal.ch" target="_blank">AI</a></td></tr>
    % elif c['attributes']['ak'] == 'AR':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.geoportal.ch" target="_blank">AR</a></td></tr>
    % elif c['attributes']['ak'] == 'ZH':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.gis.zh.ch/gb/gb.asp?app=GB-AV&vn=4$11&rn=7$8$12&start=${c['bbox'][0]}$${c['bbox'][1]}&Massstab=500" target="_blank">ZH</a></td></tr>
    % elif c['attributes']['ak'] == 'BL':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://geoview.bl.ch/?map_x=${2000000 + c['bbox'][0]}&map_y=${1000000 + c['bbox'][1]}&map_zoom=11" target="_blank">BL</a></td></tr>
    % elif c['attributes']['ak'] == 'ZG':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="http://www.zugmap.ch" target="_blank">ZG</a></td></tr>
    % elif c['attributes']['ak'] == 'FL':
        <tr><td width="150">${_('link to geoportal')}</td><td><a href="http://geodaten.llv.li/geoshop/public.html" target="_blank">${_('FL')}</a></td></tr>
    % else:
        <tr><td width="150">${_('link to canton geoportal')}</td><td>${_('Canton has provided no link to portal')}</td></tr>
    % endif
</%def>
