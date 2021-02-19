<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${_('ch.vbs.panzerverschiebungsrouten.tonnage')}</td>                                            
	<td>${c['attributes']['tonnage'] or '-'}</td></tr>

</%def>

