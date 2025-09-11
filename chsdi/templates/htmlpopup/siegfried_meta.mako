<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_(c['layerBodId'] + '.gdwh_mapsheetnumber')}</td>  <td>${c['attributes']['number']}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.gdwh_mapsheetname')}</td>    <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.gdwh_releasekey')}</td>      <td>${c['attributes']['releasekey']}</td></tr>
</%def>
