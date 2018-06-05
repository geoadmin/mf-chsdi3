<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_fn_addresse_112 = c['attributes']['fn_addresse_112'].split('\n')
    arr_len = len(arr_fn_addresse_112)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_fn_addresse_112[i] + '<br />' if  i < (arr_len-1) else str_output + arr_fn_addresse_112[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${_('ch.bakom.notruf-112_festnetz.112_festnetz')}</td>    	<td>${c['attributes']['festnetz_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_festnetz.gemeinde')}</td>          <td>${c['attributes']['fn_gemeinde_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-112_festnetz.adresse')}</td>           <td>${_(str_output)|n}</td></tr>
</%def>

