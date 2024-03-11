<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td class="cell-left">${_('geothermie')}</td><td>${int(c['attributes']['contour']) or '-'}</td></tr>
</%def>
