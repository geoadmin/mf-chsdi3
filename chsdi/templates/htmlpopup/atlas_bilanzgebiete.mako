<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    shape_area_in_km2 = c['attributes']['shape_area']
    if shape_area_in_km2 is not None:
        shape_area_in_km2 = round(shape_area_in_km2 / 1000000,1)
    else:
        shape_area_in_km2 = 0

%>
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${t.translate('ch.bafu.hydrologischer-atlas_bilanzgebiete.nummer', lang)}</td>         <td>${c['attributes']['nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.hydrologischer-atlas_bilanzgebiete.name', lang)}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.hydrologischer-atlas_bilanzgebiete.flussgebiet', lang)}</td>    <td>${c['attributes']['flussgebiet'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('flaeche_km2', lang)}</td>                                              <td>${shape_area_in_km2 or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.hydrologischer-atlas_bilanzgebiete.umfang', lang)}</td>         <td>${c['attributes']['umfang'] or '-'}</td></tr>
</%def>
