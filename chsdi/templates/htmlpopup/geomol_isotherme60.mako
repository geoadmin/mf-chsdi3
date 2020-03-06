<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-geomol-isotherme_60.elev', lang)}</td>    	<td>${c['attributes']['elev'] or '-'}</td></tr>
</%def>

