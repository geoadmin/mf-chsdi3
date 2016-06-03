<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.vbs.waldschadenkarte.lauf_nr')}</td>	         <td>${c['attributes']['lauf_nr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.waldschadenkarte.jahr_schad')}</td>            <td>${c['attributes']['jahr_schad'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.waldschadenkarte.gde_name')}</td>              <td>${c['attributes']['gde_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.waldschadenkarte.lokalname')}</td>            <td>${c['attributes']['lokalname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.waldschadenkarte.x_koord')}</td>               <td>${c['attributes']['x_koord'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.waldschadenkarte.y_koord')}</td>               <td>${c['attributes']['y_koord'] or '-'}</td></tr>
</%def>

