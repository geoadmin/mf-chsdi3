# -*- coding: utf-8 -*-


<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    % if c['attributes']['ak'] in ['D','I','F','AUT']:
        <tr><td class="cell-left">${_('No info outside CH and FL')}</td><td></td></tr>
    % elif c['attributes']['ak'] == 'AG':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?config=agis_geoportal_fs.json&basemap=base_landeskarten_sw&thema=176&xmin=${c['bbox'][0]}&ymin=${c['bbox'][1]}&xmax=${c['bbox'][2]}&ymax=${c['bbox'][3]}" target="_blank">AG</a></td></tr>
    % elif c['attributes']['ak'] == 'BS':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?theme=258&extent=${','.join(map(str,c['bbox']))}&layers=parzplan_vektor_grau_1000,av_parzellen_labels" target="_blank">BS</a></td></tr>
    % elif c['attributes']['ak'] == 'BE':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?lang=${lang}&recenter_bbox=${','.join(map(str,c['bbox']))}" target="_blank">BE</a></td></tr>
    % elif c['attributes']['ak'] == 'FR':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?reset_session&linkit=1&switch_id=switch_localisation&layer_select=Adresses,ParcVect,ParcVectnum,GrpMasque,GrpSituation,FondPlanContinu,copyright,Parcellaire,ParcScan&mapsize=0&recenter_bbox=${','.join(map(str,c['bbox']))}" target="_blank">FR</a></td></tr>
    % elif c['attributes']['ak'] == 'GE':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?X=${c['bbox'][0] + 2000000}&Y=${c['bbox'][1] + 1000000}&SCALE=${c['scale']}" target="_blank">GE</a></td></tr>
    % elif c['attributes']['ak'] == 'GL':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?visibleLayers=MOpublic" target="_blank">GL</a></td></tr>
    % elif c['attributes']['ak'] == 'JU':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?&map_x=${(c['bbox'][0] + c['bbox'][2])/2}&map_y=${(c['bbox'][1] + c['bbox'][3])/2}&map_zoom=11" target="_blank">JU</a></td></tr>
    % elif c['attributes']['ak'] == 'SH':   
       <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?idp=1&uid=1&pwd=&map=10&lan=de&typ=3&bmurl=Nav@g@98@u@West@g@${c['bbox'][0]}@u@Nord@g@${c['bbox'][1]}@u@B@g@600" target="_blank">SH</a></td></tr>
    % elif c['attributes']['ak'] == 'SZ':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?idp=1&uid=3&bmurl=Nav@g@129@u@West@g@${c['bbox'][0]}@u@Nord@g@${c['bbox'][1]}@u@B@g@${c['scale']}" target="_blank">SZ</a></td></tr>
    % elif c['attributes']['ak'] == 'SO':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?karte=ortsplan&extent=${','.join(map(str,c['bbox']))}" target="_blank">SO</a></td></tr>
    % elif c['attributes']['ak'] == 'TI':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?ct=mue&extent=${','.join(map(str,c['bbox']))}" target="_blank">TI</a></td></tr>
    % elif c['attributes']['ak'] == 'VD':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?reset_session&linkit=1&switch_id=switch_cadastre&layer_select=complement_vd2,fond_continu_gris,canton_select,gc_mensuration_select,cad_parv_select,cad_parv_numero_select,ddp_select,ddp_npcs_select,cad_parv_plim_select,cad_bat_hs_cadastre_select,cad_bat_ss_select,npcs_bat_hs_select,npcs_bat_ss_select,couverture_sol,cad_cs_dur,cad_cs_vert,cad_cs_bois,cad_cs_eau,cad_cs_div&recenter_bbox=${','.join(map(str,c['bbox']))}&mapSize=4" target="_blank">VD</a></td></tr>
    % elif c['attributes']['ak'] == 'TG':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?gui_id=Amtliche%20Vermessung&mb_myBBOX=${','.join(map(str,c['bbox']))}" target="_blank">TG</a></td></tr>
    % elif c['attributes']['ak'] == 'NE':
        <tr><td width="150">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?map_x=${(c['bbox'][0] + c['bbox'][2])/2}&map_y=${(c['bbox'][1] + c['bbox'][3])/2}&map_zoom=12" target="_blank">NE</a></td></tr>
    % elif c['attributes']['ak'] == 'LU':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">LU</a></td></tr>
    % elif c['attributes']['ak'] == 'OW':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">OW</a></td></tr>
    % elif c['attributes']['ak'] == 'NW':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">NW</a></td></tr>
    % elif c['attributes']['ak'] == 'UR':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">UR</a></td></tr>
    % elif c['attributes']['ak'] == 'GR':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">GR</a></td></tr>
    % elif c['attributes']['ak'] == 'AI':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">AI</a></td></tr>
    % elif c['attributes']['ak'] == 'AR':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">AR</a></td></tr>
    % elif c['attributes']['ak'] == 'ZH':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?app=GB-AV&vn=4$11&rn=7$8$12&start=${c['bbox'][0]}$${c['bbox'][1]}&Massstab=500" target="_blank">ZH</a></td></tr>
    % elif c['attributes']['ak'] == 'BL':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}?map_x=${2000000 + c['bbox'][0]}&map_y=${1000000 + c['bbox'][1]}&map_zoom=11" target="_blank">BL</a></td></tr>
    % elif c['attributes']['ak'] == 'ZG':
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">ZG</a></td></tr>
    % elif c['attributes']['ak'] == 'FL':
        <tr><td class="cell-left">${_('link to geoportal')}</td><td><a href="${c['attributes']['url_geoportal']}" target="_blank">${_('FL')}</a></td></tr>
    % else:
        <tr><td class="cell-left">${_('link to canton geoportal')}</td><td>${_('Canton has provided no link to portal')}</td></tr>
    % endif
</%def>
