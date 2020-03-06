<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    facname = 'facname_%s' % lang
    fackind_text = 'fackind_text_%s' % lang
    facstatus_text = 'facstatus_text_%s' % lang
    description = 'description_%s' % lang
    objname = 'objname_%s' % lang

%>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_name', lang)}</td>                  <td>${c['attributes'][facname] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_anlageart', lang)}</td>             <td>${c['attributes'][fackind_text] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_anlagestatus', lang)}</td>          <td>${c['attributes'][facstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_facility_beschlussdatum', lang)}</td>        <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_sachplan_beschreibung', lang)}</td>                   <td>${c['attributes'][description] or '-'}</td></tr>
%  if c['attributes']['doc_web'] and c['attributes']['doc_title']:
<%
    doc_web_part = c['attributes']['doc_web'].split('###')
    doc_title_part = c['attributes']['doc_title'].split('###')
%>
%  for i in range(len(doc_web_part)):
     <tr><td class="cell-left">${h.translate('tt_sachplan_weitereinfo', lang)}</td>                   <td><a href="${doc_web_part[i] or '-'}" target="_blank">${doc_title_part[i] or '-'}</a></td></tr>
%endfor
%else:
    <tr><td class="cell-left">${h.translate('tt_sachplan_weitereinfo', lang)}</td>                    <td> - </td></tr>
%endif
</%def>
