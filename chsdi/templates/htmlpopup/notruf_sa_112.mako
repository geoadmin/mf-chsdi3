<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    arr_sa_addresse_112 = c['attributes']['sa_addresse_112'].split('\n')
    arr_len = len(arr_sa_addresse_112)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_sa_addresse_112[i] + '<br />' if  i < (arr_len-1) else str_output + arr_sa_addresse_112[i]
    endfor
%>

<% c['stable_id'] = True %>

    <tr><td class="cell-left">${Translator.translate('ch.bakom.notruf-112_satellit.112_satellit', lang)}</td>    	<td>${c['attributes']['satellit_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bakom.notruf-112_satellit.gemeinde', lang)}</td>          <td>${c['attributes']['sa_gemeinde_112'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bakom.notruf-112_satellit.adresse', lang)}</td>           <td>${_(str_output)|n}</td></tr>
</%def>

