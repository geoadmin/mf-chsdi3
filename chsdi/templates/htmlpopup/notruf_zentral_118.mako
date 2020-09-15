<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    arr_fn_zentrale_118 = c['attributes']['fn_zentrale_118'].split('\n')
    arr_len = len(arr_fn_zentrale_118)
    str_output_fn = ''
    for i in range(arr_len):
        str_output_fn = str_output_fn + arr_fn_zentrale_118[i] + '<br />' if  i < (arr_len-1) else str_output_fn + arr_fn_zentrale_118[i]
    endfor
    
    arr_mo_zentrale_118 = c['attributes']['mo_zentrale_118'].split('\n')
    arr_len = len(arr_mo_zentrale_118)
    str_output_mo = ''
    for i in range(arr_len):
        str_output_mo = str_output_mo + arr_mo_zentrale_118[i] + '<br />' if  i < (arr_len-1) else str_output_mo + arr_mo_zentrale_118[i]
    endfor
%>
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.bakom.notruf-118_zentral.gemeinde_118')}</td>    	<td>${c['attributes']['gemeinde_118'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-118_zentral.festnetz_118')}</td>    	<td>${c['attributes']['festnetz_118'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-118_zentral.fn_zentrale_118')}</td>          <td>${_(str_output_fn)|n}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-118_zentral.mobile_118')}</td>           <td>${c['attributes']['mobile_118'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-118_zentral.mo_zentrale_118')}</td>     <td>${_(str_output_mo)|n}</td></tr>
</%def>

