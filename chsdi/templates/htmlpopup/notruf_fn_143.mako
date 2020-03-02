<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_fn_addresse_143 = c['attributes']['fn_addresse_143'].split('\n')
    arr_len = len(arr_fn_addresse_143)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_fn_addresse_143[i] + '<br />' if  i < (arr_len-1) else str_output + arr_fn_addresse_143[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${t.Translator.translate('ch.bakom.notruf-143_festnetz.143_festnetz', lang)}</td>    	<td>${c['attributes']['festnetz_143'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bakom.notruf-143_festnetz.gemeinde', lang)}</td>          <td>${c['attributes']['fn_gemeinde_143'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bakom.notruf-143_festnetz.adresse', lang)}</td>           <td>${_(str_output)|n}</td></tr>
</%def>

