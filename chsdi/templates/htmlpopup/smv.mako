<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('smv.scale', lang)}</td>   <td>${c['attributes']['scale'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('smv.price', lang)}</td>    <td>${c['attributes']['price'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('smv.release', lang)}</td>    <td>${c['attributes']['release'] or '-'}</td></tr>
</%def>
