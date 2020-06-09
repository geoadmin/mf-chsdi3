<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_fn_zentrale_143 = c['attributes']['fn_zentrale_143'].split('\n')
    arr_len = len(arr_fn_zentrale_143)
    str_output_fn = ''
    for i in range(arr_len):
        str_output_fn = str_output_fn + arr_fn_zentrale_143[i] + '<br />' if  i < (arr_len-1) else str_output_fn + arr_fn_zentrale_143[i]
    endfor
    
    arr_mo_zentrale_143 = c['attributes']['mo_zentrale_143'].split('\n')
    arr_len = len(arr_mo_zentrale_143)
    str_output_mo = ''
    for i in range(arr_len):
        str_output_mo = str_output_mo + arr_mo_zentrale_143[i] + '<br />' if  i < (arr_len-1) else str_output_mo + arr_mo_zentrale_143[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${_('ch.bakom.notruf-143_zentral.festnetz_143')}</td>    	<td>${c['attributes']['festnetz_143'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-143_zentral.fn_zentrale_143')}</td>          <td>${_(str_output_fn)|n}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-143_zentral.mobile_143')}</td>           <td>${c['attributes']['mobile_143'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-143_zentral.mo_zentrale_143')}</td>     <td>${_(str_output_mo)|n}</td></tr>

</%def>

