<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td class="cell-left">${h.translate('geothermie', lang)}</td><td>${c['attributes']['contour'] or '-'}</td></tr>
</%def>
