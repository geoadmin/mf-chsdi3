<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    c['stable_id'] = True 
    %>

    <tr><td class="cell-left">${_('ch.bag.radioaktivitaet-atmosphaere.station')}</td>    <td>${c['id']}</td></tr>
    <tr><td class="cell-left">${_('ch.bag.radioaktivitaet-atmosphaere.period')}</td>     <td>${c['attributes']['period'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bag.radioaktivitaet-atmosphaere.nuc1')}</td>       <td>${c['attributes']['nuc1'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bag.radioaktivitaet-atmosphaere.nuc2')}</td>       <td>${c['attributes']['nuc2'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bag.radioaktivitaet-atmosphaere.nuc3')}</td>       <td>${c['attributes']['nuc3'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bag.radioaktivitaet-atmosphaere.nuc4')}</td>       <td>${c['attributes']['nuc4'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bag.radioaktivitaet-atmosphaere.nuc5')}</td>       <td>${c['attributes']['nuc5'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('link')}</td>            <td><a target="_blank" href="${c['attributes']['stationlink']}">${_('link') or '-'}</a></td></tr>
</%def>

