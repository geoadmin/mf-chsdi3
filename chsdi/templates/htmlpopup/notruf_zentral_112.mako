<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    arr_fn_zentrale_112 = c['attributes']['fn_zentrale_112'].split('\n')
    arr_len = len(arr_fn_zentrale_112)
    str_output_fn = ''
    for i in range(arr_len):
        str_output_fn = str_output_fn + arr_fn_zentrale_112[i] + '<br />' if  i < (arr_len-1) else str_output_fn + arr_fn_zentrale_112[i]
    endfor
    
    arr_mo_zentrale_112 = c['attributes']['mo_zentrale_112'].split('\n')
    arr_len = len(arr_mo_zentrale_112)
    str_output_mo = ''
    for i in range(arr_len):
        str_output_mo = str_output_mo + arr_mo_zentrale_112[i] + '<br />' if  i < (arr_len-1) else str_output_mo + arr_mo_zentrale_112[i]
    endfor
%>
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('gemeinde')}</td>    	<td>${c['attributes']['gemeinde_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_zentral.festnetz_112')}</td>    	<td>${c['attributes']['festnetz_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_zentral.fn_zentrale_112')}</td>          <td>${_(str_output_fn)|n}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_zentral.mobile_112')}</td>           <td>${c['attributes']['mobile_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_zentral.mo_zentrale_112')}</td>     <td>${_(str_output_mo)|n}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_zentral.satellit_112')}</td>           <td>${c['attributes']['satellit_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_zentral.sa_zentrale_112')}</td>     <td>${_(str_output_mo)|n}</td></tr>
</%def>

