<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td class="cell-left">Value</td><td>${c['attributes']['properties'] or '-'}</td></tr>
</%def>

