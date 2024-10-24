<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
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
        <td class="cell-left">${_('ch.bakom.notruf-143_zentral.rn_143')}</td>
        <td>${c['attributes']['rn_143'] or '-'}</td>
    </tr>
</%def>

