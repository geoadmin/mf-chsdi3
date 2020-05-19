<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.are.belastung-personenverkehr-bahn.nr')}</td>          <td>${c['attributes']['nr']}</td></tr>
    <tr><td class="cell-left">${_('ch.are.belastung-personenverkehr-bahn.dwv_oev')}</td>     <td>${c['attributes']['dwv_oev']}</td></tr>
    <tr><td class="cell-left">${_('ch.are.belastung-personenverkehr-bahn.dtv_oev')}</td>          <td>${c['attributes']['dtv_oev']}</td></tr>
    <tr><td class="cell-left">${_('ch.are.belastung-personenverkehr-bahn.msp_oev')}</td>          <td>${c['attributes']['msp_oev']}</td></tr>
    <tr><td class="cell-left">${_('ch.are.belastung-personenverkehr-bahn.asp_oev')}</td>          <td>${c['attributes']['asp_oev']}</td></tr>
</%def>
