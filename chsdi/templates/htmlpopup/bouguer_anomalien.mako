<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td class="cell-left">${t.translate('et_fromatt_bouguer', lang)}</td><td>${c['attributes']['et_fromatt'] or '-'}</td></tr>
</%def>
