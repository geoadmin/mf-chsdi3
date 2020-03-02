<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('sia_261_norm', lang)}</td>    <td>${c['attributes']['bgk'] or '-'}</td></tr>
</%def>

