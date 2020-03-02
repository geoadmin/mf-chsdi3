<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geomol-temperatur_top_omalm.elev', lang)}</td>    	<td>${c['attributes']['elev'] or '-'}</td></tr>
</%def>

