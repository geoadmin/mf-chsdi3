<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    arr_fn_zentrale_117 = c['attributes']['fn_zentrale_117'].split('\n')
    arr_len = len(arr_fn_zentrale_117)
    str_output_fn = ''
    for i in range(arr_len):
        str_output_fn = str_output_fn + arr_fn_zentrale_117[i] + '<br />' if  i < (arr_len-1) else str_output_fn + arr_fn_zentrale_117[i]
    endfor
    
    arr_mo_zentrale_117 = c['attributes']['mo_zentrale_117'].split('\n')
    arr_len = len(arr_mo_zentrale_117)
    str_output_mo = ''
    for i in range(arr_len):
        str_output_mo = str_output_mo + arr_mo_zentrale_117[i] + '<br />' if  i < (arr_len-1) else str_output_mo + arr_mo_zentrale_117[i]
    endfor
%>
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.bakom.notruf-117_zentral.gemeinde_117')}</td>    	<td>${c['attributes']['gemeinde_117'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-117_zentral.festnetz_117')}</td>    	<td>${c['attributes']['festnetz_117'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-117_zentral.fn_zentrale_117')}</td>          <td>${_(str_output_fn)|n}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-117_zentral.mobile_117')}</td>           <td>${c['attributes']['mobile_117'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-117_zentral.mo_zentrale_117')}</td>     <td>${_(str_output_mo)|n}</td></tr>
</%def>

