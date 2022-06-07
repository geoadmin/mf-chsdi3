<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_bilanzgebiete.nummer')}</td>         <td>${c['attributes']['nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_bilanzgebiete.name')}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_bilanzgebiete.flussgebiet')}</td>    <td>${c['attributes']['flussgebiet'] or '-'}</td></tr>
    % if c['attributes']['shape_area'] is not None:
        <tr><td class="cell-left">${_('flaeche_km2')}</td><td>${round(c['attributes']['shape_area'] / 1000000, 1)}</td></tr>
    % else:
        <tr><td class="cell-left">${_('flaeche_km2')}</td><td>-</td></tr>
    % endif
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_bilanzgebiete.umfang')}</td>         <td>${c['attributes']['umfang'] or '-'}</td></tr>
</%def>
