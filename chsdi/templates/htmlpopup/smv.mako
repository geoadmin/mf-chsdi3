<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('smv.scale')}</td>   <td>${c['attributes']['scale'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('smv.price')}</td>    <td>${c['attributes']['price'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('smv.release')}</td>    <td>${c['attributes']['release'] or '-'}</td></tr>
</%def>
