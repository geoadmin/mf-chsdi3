<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    facname = 'facname_%s' % lang
    fackind_text = 'fackind_text_%s' % lang
    facstatus_text = 'facstatus_text_%s' % lang
    description_text = 'description_%s' % lang
    static_url = 'static_url_%s' % lang
    objektblatt = 'ch.bav.sachplan-unterirdischer-guetertransport_kraft.obj_blatt_alt'
    objektblatt = objektblatt if c['attributes']['doc_tid'] == '226-D-90-001_0' else 'tt_sachplan_objektblatt'
%>
    <tr><td class="cell-left">${_('tt_sachplan_facility_name')}</td>                  <td>${c['attributes'][facname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_anlageart')}</td>             <td>${c['attributes'][fackind_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_anlagestatus')}</td>          <td>${c['attributes'][facstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_beschlussdatum')}</td>        <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>                   <td>${c['attributes'][description_text] or '-'}</td></tr>
    <td class="cell-left">${_(objektblatt)}</td>
    <td>
% if c['attributes']['doc_web'] != None:
        <a href="${c['attributes']['doc_web']}" target="_balnk">${c['attributes']['doc_title'] or '-'}</a>
% else:
        ${c['attributes']['doc_title'] or '-'}
% endif
    </td>
</%def>
