<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.inventar_nr')}</td>
        <td>${c['attributes']['inventar_nr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.kanton')}</td>
        <td>${c['attributes']['kanton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.standort')}</td>
        <td>${c['attributes']['standort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.bezeichnung')}</td>
        <td>${c['attributes']['bezeichnung'] or '-'}</td></tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.kategorie')}</td>
        <td>${c['attributes']['kategorie'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.thema')}</td>
        <td>${c['attributes']['thema'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.zeitraum')}</td>
        <td>${c['attributes']['zeitraum'] or '-'}</td></tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.form')}</td>
        <td>${c['attributes']['form'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.baujahr')}</td>
        <td>${c['attributes']['baujahr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.link_zum_objekt')}</td>
    % if c['attributes']['link_zum_objekt']:
        <td><a href="${c['attributes']['link_zum_objekt']}" target="_blank">${_('link')}</a></td>
    % else:
        <td>-</td>
    % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId']+'.link_zum_gesamtinventar')}</td>
    % if c['attributes']['link_zum_gesamtinventar']:
        <td><a href="${c['attributes']['link_zum_gesamtinventar']}" target="_blank">${_('link')}</a></td>
    % else:
        <td>-</td>
    % endif
    </tr>
</%def>

