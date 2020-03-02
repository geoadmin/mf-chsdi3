<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    nummer = c['layerBodId'] + '.' + 'id'
%>
    <% c['stable_id'] = True %>
	<tr><td class="cell-left">${_(nummer)}</td>         <td>${c['featureId']}</td></tr>
<!--	
    <tr><td class="cell-left">${Translator.translate('name', lang)}</td>           <td>${c['attributes']['punktname'] or '-'}</td></tr>
-->
	<tr><td class="cell-left">${Translator.translate('status_fp', lang)}</td>      <td>${c['attributes']['status'] or '-'}</td></tr>
	<tr><td class="cell-left">${Translator.translate('fp_Y03_X03', lang)}</td>     <td>${c['attributes']['y03'] or '-'} / ${c['attributes']['x03'] or '-'}</td></tr>
	<tr><td class="cell-left">${Translator.translate('fp_E95_N95', lang)}</td>     <td>${c['attributes']['e95'] or '-'} / ${c['attributes']['n95'] or '-'}</td></tr>
	<tr><td class="cell-left">${Translator.translate('fp_H02', lang)}</td>         <td>${c['attributes']['h02'] or '-'}</td></tr>
<!--	
    <tr><td class="cell-left">${Translator.translate('zugang', lang)}</td>         <td>${c['attributes']['zugang'] or '-'}</td></tr>
-->
	<tr><td class="cell-left">${Translator.translate('protokoll')}</td>      <td><a href="${c['attributes']['url'] or '-'}" target="_blank">${_('protokoll', lang)}</a></td></tr>
</%def>
