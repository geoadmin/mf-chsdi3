<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        arr_rn_118 = c['attributes']['rn_118'].split(',')
        arr_len = len(arr_rn_118)
        str_output = ''
        for i in range(arr_len):
            str_output = str_output + arr_rn_118[i] + '<br />' if  i < (arr_len-1) else str_output + arr_rn_118[i]
        endfor
    %>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-118_zentral.alarmzentrale')}</td>
        <td>${c['attributes']['alarmzentrale'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-118_zentral.strasse')}</td>
        <td>${c['attributes']['strasse'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-118_zentral.nummer')}</td>
        <td>${c['attributes']['nummer'] or '-'}</td>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-118_zentral.plz')}</td>
        <td>${c['attributes']['plz'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-118_zentral.ort')}</td>
        <td>${c['attributes']['ort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-118_zentral.rn_118')}</td>
        <td>${_(str_output)|n}</td>
    </tr>
</%def>

