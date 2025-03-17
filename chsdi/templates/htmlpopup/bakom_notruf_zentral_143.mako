<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        arr_rn_143 = c['attributes']['rn_143'].split(',')
        arr_len = len(arr_rn_143)
        str_output = ''
        for i in range(arr_len):
            str_output = str_output + arr_rn_143[i] + '<br />' if  i < (arr_len-1) else str_output + arr_rn_143[i]
        endfor
    %>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.alarmzentrale')}</td>
        <td>${c['attributes']['alarmzentrale'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.strasse')}</td>
        <td>${c['attributes']['strasse'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.nummer')}</td>
        <td>${c['attributes']['nummer'] or '-'}</td>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.plz')}</td>
        <td>${c['attributes']['plz'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.ort')}</td>
        <td>${c['attributes']['ort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.ktn')}</td>
        <td>${c['attributes']['kt'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.chg_date')}</td>
        <td>${c['attributes']['chg_date'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.rn_143')}</td>
        <td>${_(str_output)|n}</td>
    </tr>
</%def>

