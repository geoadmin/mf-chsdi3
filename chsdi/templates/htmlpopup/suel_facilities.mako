<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    facname = 'facname_%s' % lang
    fackind_text = 'fackind_text_%s' % lang
    facstatus_text = 'facstatus_text_%s' % lang
    description_text = 'description_%s' % lang
%>
    <tr><td class="cell-left">${_('tt_sachplan_facility_name')}</td>            <td>${c['attributes'][facname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_anlageart')}</td>       <td>${c['attributes'][fackind_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_anlagestatus')}</td>    <td>${c['attributes'][facstatus_text] or '-'}</td></tr>
    %if c['layerBodId'].endswith('kraft'):
    <tr><td class="cell-left">${_('tt_sachplan_facility_beschlussdatum')}</td>  <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    %endif
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>             <td>${c['attributes'][description_text] or '-' | n}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>
    % if c['attributes']['doc_web']:
        <td><a href="${c['attributes']['doc_web']}" target="_blank">${c['attributes']['doc_title'] or '-'}</a></td></tr>
    % else:
        <td> - </td></tr>
    %endif
</%def>
