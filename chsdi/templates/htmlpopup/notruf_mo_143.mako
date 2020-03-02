<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_mo_addresse_143 = c['attributes']['mo_addresse_143'].split('\n')
    arr_len = len(arr_mo_addresse_143)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_mo_addresse_143[i] + '<br />' if  i < (arr_len-1) else str_output + arr_mo_addresse_143[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${Translator.translate('ch.bakom.notruf-143_mobilnetz.143_mobil', lang)}</td>         <td>${c['attributes']['mobile_143'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bakom.notruf-143_mobilnetz.gemeinde', lang)}</td>          <td>${c['attributes']['mo_gemeinde_143'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bakom.notruf-143_mobilnetz.adresse', lang)}</td>           <td>${_(str_output)|n}</td></tr>
</%def>

