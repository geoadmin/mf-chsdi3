<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    facname = 'facname_%s' % lang
    fackind_text = 'fackind_text_%s' % lang
    facstatus_text = 'facstatus_text_%s' % lang
    description_text = 'description_%s' % lang
    objectname = 'objectname_%s' % lang
%>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_number', lang)}</td>                <td>${c['attributes']['facility']}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_name', lang)}</td>                  <td>${c['attributes'][facname]}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_anlageart', lang)}</td>             <td>${c['attributes'][fackind_text] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_anlagestatus', lang)}</td>          <td>${c['attributes'][facstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_beschlussdatum', lang)}</td>        <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_beschreibung', lang)}</td>                   <td>${c['attributes'][description_text] or '-'}</td></tr>
% if c['attributes']['doc_web']:
    <tr><td class="cell-left">${h.translate('tt_sachplan_weitereinfo', lang)}</td>                    <td><a href="${c['attributes']['doc_web'] or '-'}" target="_blank">${h.translate('tt_sachplan_objektblatt', lang)}</a></td></tr>
% else:
    <tr><td class="cell-left">${h.translate('tt_sachplan_weitereinfo', lang)}</td>                    <td> - </td></tr>
%endif
</%def>
