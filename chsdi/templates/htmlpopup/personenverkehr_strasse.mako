<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.nr')}</td>          <td>${c['attributes']['nr']}</td></tr>
    <tr><td class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dwv_fzg')}</td>     <td>${c['attributes']['dwv_fzg']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<table class="table-with-border kernkraftwerke-extended">
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.nr')}</th><td>${c['attributes']['nr'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dwv_fzg')}</th><td>${c['attributes']['dwv_fzg'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dwv_pw')}</th><td>${c['attributes']['dwv_pw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dwv_li')}</th><td>${c['attributes']['dwv_li'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dwv_lw')}</th><td>${c['attributes']['dwv_lw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dwv_lz')}</th><td>${c['attributes']['dwv_lz'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dtv_fzg')}</th><td>${c['attributes']['dtv_fzg'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dtv_pw')}</th><td>${c['attributes']['dtv_pw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dtv_li')}</th><td>${c['attributes']['dtv_li'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dtv_lw')}</th><td>${c['attributes']['dtv_lw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.dtv_lz')}</th><td>${c['attributes']['dtv_lz'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.msp_fzg')}</th><td>${c['attributes']['msp_fzg'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.msp_pw')}</th><td>${c['attributes']['msp_pw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.msp_li')}</th><td>${c['attributes']['msp_li'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.msp_lw')}</th><td>${c['attributes']['msp_lw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.msp_lz')}</th><td>${c['attributes']['msp_lz'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.asp_fzg')}</th><td>${c['attributes']['asp_fzg'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.asp_pw')}</th><td>${c['attributes']['asp_pw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.asp_li')}</th><td>${c['attributes']['asp_li'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.asp_lw')}</th><td>${c['attributes']['asp_lw'] or '-'}</td></tr>
 <tr><th class="cell-left">${_('ch.are.belastung-personenverkehr-strasse.asp_lz')}</th><td>${c['attributes']['asp_lz'] or '-'}</td></tr>
</table>
</%def>
