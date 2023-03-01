<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    nummer = c['layerBodId'] + '.' + 'id'
%>

    <% c['stable_id'] = True %>
	<tr><td class="cell-left">${_(c['layerBodId']+'.id')}</td>						<td>${c['featureId']}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.status')}</td>      			<td>${c['attributes']['status'] or '-'}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.koordinate')}</td>      		<td>${c['attributes']['koordinate'] or '-'}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.hoehe_geom_m')}</td>      		<td>${c['attributes']['hoehe_geom_m'] or '-'}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.url_punktprotokoll')}</td>      <td><a href="${c['attributes']['url_punktprotokoll'] or '-'}" target="_blank">${_(c['layerBodId']+'.url_punktprotokoll')}</a></td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.punktzeichen')}</td>      		<td>${c['attributes']['punktzeichen'] or '-'}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.kanton')}</td>      			<td>${c['attributes']['kanton'] or '-'}</td></tr>
	<tr><td class="cell-left">${_(c['layerBodId']+'.zust_name')}</td>      			<td>${c['attributes']['zust_name'] or '-'}</td></tr>
</%def>
