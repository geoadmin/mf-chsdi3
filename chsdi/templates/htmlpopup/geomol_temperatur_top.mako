<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geomol-temperatur_top_omm.pixel_value')}</td>    	<td>${int(round(c['attributes']['pixel_value'])) or '-'}</td></tr>
</%def>

