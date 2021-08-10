<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_(c['layerBodId']+'.name')}</td>                   <td>${c['attributes']['name']}</td></tr>
    %if c['attributes']['extraction_spring']:
    <tr><td class="cell-left">${_(c['layerBodId']+'.extraction_spring')}</td>      <td>${c['attributes']['extraction_spring'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.extraction_summer')}</td>      <td>${c['attributes']['extraction_summer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.extraction_fall')}</td>        <td>${c['attributes']['extraction_fall'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.extraction_winter')}</td>      <td>${c['attributes']['extraction_winter'] or '-'}</td></tr>
    %endif
    <tr><td class="cell-left">${_(c['layerBodId']+'.disposal_spring')}</td>        <td>${c['attributes']['disposal_spring'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.disposal_summer')}</td>        <td>${c['attributes']['disposal_summer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.disposal_fall')}</td>          <td>${c['attributes']['disposal_fall'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.disposal_winter')}</td>        <td>${c['attributes']['disposal_winter'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.further_information')}</td>    <td><a href="${c['attributes']['further_information'] or '-'}" target="_blank">${_(c['layerBodId']+'.link')}</a></td></tr>
</%def>
