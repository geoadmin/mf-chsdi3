<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_mo_addresse_118 = c['attributes']['mo_addresse_118'].split('\n')
    arr_len = len(arr_mo_addresse_118)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_mo_addresse_118[i] + '<br />' if  i < (arr_len-1) else str_output + arr_mo_addresse_118[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.notruf-118_mobilnetz.118_mobil', lang)}</td>         <td>${c['attributes']['mobile_118'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.notruf-118_mobilnetz.gemeinde', lang)}</td>          <td>${c['attributes']['mo_gemeinde_118'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.notruf-118_mobilnetz.adresse', lang)}</td>           <td>${_(str_output)|n}</td></tr>
</%def>

