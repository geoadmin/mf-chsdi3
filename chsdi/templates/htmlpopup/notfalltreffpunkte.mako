<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.ntp_id')}</td>   <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.gebbezeichnung')}</td>   <td>${c['attributes']['gebbezeichnung']}</td></tr>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.strasse')}</td>   <td>${c['attributes']['strasse']}</td></tr>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.haus_nummer')}</td>   <td>${c['attributes']['haus_nummer'] or "-"}</td></tr>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.plz_ort')}</td><td>${c['attributes']['plz']}&nbsp;${c['attributes']['ort']}</td></tr>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.gemeinde')}</td><td>${c['attributes']['gemeinde']}</td></tr>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.kanton')}</td><td>${c['attributes']['kanton']}</td></tr>
    <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.koord')}</td><td>${c['attributes']['xkoord']},&nbsp;${c['attributes']['ykoord']}</td></tr>
    % if c['attributes']['linkkanton'] is not None:
        <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.linkkanton')}</td><td><a href="${c['attributes']['linkkanton']}" target="_blank">${_('link')}</a></td></tr>
    % else:
        <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.linkkanton')}</td><td>-</td></tr>
    % endif
    % if c['attributes']['linkbabs'] is not None:
        <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.linkbabs')}</td><td><a href="${c['attributes']['linkbabs']}" target="_blank">${_('link')}</a></td></tr>
    % else:
       <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.linkbabs')}</td><td>-</td></tr>
    % endif
   <tr><td class="cell-left">${_('ch.babs.notfalltreffpunkte.bemerkungen')}</td><td>${c['attributes']['bemerkungen'] or "-"}</td></tr>
   </%def>
