<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geomol-temperaturmodell_eingangsdaten.name')}</td>    	<td>${c['attributes']['name'] or '-'}</td></tr>
</%def>

