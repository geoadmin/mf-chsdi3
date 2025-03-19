<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        arr_routing_nr = c['attributes']['routing_nr'].split(',')
        arr_len = len(arr_routing_nr)
        str_output = ''
        for i in range(arr_len):
            str_output = str_output + arr_routing_nr[i] + '<br />' if  i < (arr_len-1) else str_output + arr_routing_nr[i]
        endfor
    %>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.alarmzentrale')}</td>
        <td>${c['attributes']['alarmzentrale'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.strasse')}</td>
        <td>${c['attributes']['strasse'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.nummer')}</td>
        <td>${c['attributes']['nummer'] or '-'}</td>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.plz')}</td>
        <td>${c['attributes']['plz'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.ort')}</td>
        <td>${c['attributes']['ort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.ktn')}</td>
        <td>${c['attributes']['kt'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.routing_nr')}</td>
        <td>${_(str_output)|n}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_zentral.chg_date')}</td>
        <td>${c['attributes']['chg_date'] or '-'}</td>
    </tr>
</%def>

