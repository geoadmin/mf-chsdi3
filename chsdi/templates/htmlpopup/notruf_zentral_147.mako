<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_fn_zentrale_147 = c['attributes']['fn_zentrale_147'].split('\n')
    arr_len = len(arr_fn_zentrale_147)
    str_output_fn = ''
    for i in range(arr_len):
        str_output_fn = str_output_fn + arr_fn_zentrale_147[i] + '<br />' if  i < (arr_len-1) else str_output_fn + arr_fn_zentrale_147[i]
    endfor
    
    arr_mo_zentrale_147 = c['attributes']['mo_zentrale_147'].split('\n')
    arr_len = len(arr_mo_zentrale_147)
    str_output_mo = ''
    for i in range(arr_len):
        str_output_mo = str_output_mo + arr_mo_zentrale_147[i] + '<br />' if  i < (arr_len-1) else str_output_mo + arr_fn_zentrale_147[i]
    endfor

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${_('ch.bakom.notruf-147_zentral.festnetz_147')}</td>    	<td>${c['attributes']['festnetz_147'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-147_zentral.fn_zentrale_147')}</td>          <td>${_(str_output_fn)|n}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-147_zentral.mobile_147')}</td>           <td>${c['attributes']['mobile_147'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-147_zentral.mo_zentrale_147')}</td>     <td>${_(str_output_mo|n}</td></tr>

</%def>

