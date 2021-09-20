<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_(c['layerBodId']+'.name')}</td>                      <td>${c['attributes']['name']}</td></tr>
    %if c['attributes']['heat_extraction_gwha']:
    <tr><td class="cell-left">${_(c['layerBodId']+'.heat_extraction_gwha')}</td>      <td>${c['attributes']['heat_extraction_gwha'] or '-'}</td></tr>
    %endif
    <tr><td class="cell-left">${_(c['layerBodId']+'.heat_disposal_gwha')}</td>        <td>${c['attributes']['heat_disposal_gwha'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.further_information')}</td>       <td><a href="${c['attributes']['further_information'] or '-'}" target="_blank">${_(c['layerBodId']+'.link')}</a></td></tr>
</%def>
