<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_mo_addresse_145 = c['attributes']['mo_addresse_145'].split('\n')
    arr_len = len(arr_mo_addresse_145)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_mo_addresse_145[i] + '<br />' if  i < (arr_len-1) else str_output + arr_mo_addresse_145[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${_('ch.bakom.notruf-145_mobilnetz.145_mobil')}</td>         <td>${c['attributes']['mobile_145'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-145_mobilnetz.gemeinde')}</td>          <td>${c['attributes']['mo_gemeinde_145'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bakom.notruf-145_mobilnetz.adresse')}</td>           <td>${_(str_output)|n}</td></tr>
</%def>

