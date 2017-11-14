<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    facname = 'facname_%s' % lang
    fackind_text = 'fackind_text_%s' % lang
    facstatus_text = 'facstatus_text_%s' % lang
    description_text = 'description_text_%s' % lang
    objectname = 'objectname_%s' % lang

%>
    <tr><td class="cell-left">${_('tt_sachplan_facility_name')}</td>                  <td>${c['attributes'][facname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_anlageart')}</td>             <td>${c['attributes'][fackind_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_anlagestatus')}</td>          <td>${c['attributes'][facstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_beschlussdatum')}</td>        <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>                   <td>${c['attributes'][description_text] or '-'}</td></tr>
%  if c['attributes']['document_web'] and c['attributes']['document_title']:
<%
    document_web_part = c['attributes']['document_web'].split('###')
    document_title_part = c['attributes']['document_title'].split('###')
%>
%  for i in range(len(document_web_part)):
     <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>                   <td><a href="${document_web_part[i] or '-'}" target="_blank">${document_title_part[i] or '-'}</a></td></tr>
%endfor
%else:
    <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>                    <td> - </td></tr>
%endif
</%def>
