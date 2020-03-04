<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_mo_addresse_117 = c['attributes']['mo_addresse_117'].split('\n')
    arr_len = len(arr_mo_addresse_117)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_mo_addresse_117[i] + '<br />' if  i < (arr_len-1) else str_output + arr_mo_addresse_117[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.notruf-117_mobilnetz.117_mobil', lang)}</td>         <td>${c['attributes']['mobile_117'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.notruf-117_mobilnetz.gemeinde', lang)}</td>          <td>${c['attributes']['mo_gemeinde_117'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.notruf-117_mobilnetz.adresse', lang)}</td>           <td>${_(str_output)|n}</td></tr>
</%def>

