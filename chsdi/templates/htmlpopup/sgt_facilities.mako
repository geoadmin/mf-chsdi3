<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% 
    c['stable_id'] = True 
    lang = lang if lang in ('fr','it') else 'de'
    facname = 'facname_%s' % lang
    fackind_text = 'fackind_text_%s' % lang
    facstatus_text = 'facstatus_text_%s' % lang
    objname_text = 'objname_text_%s' % lang
%>
    <tr><td width="150">${_('tt_sachplan_facility_name')}</td>              <td>${c['attributes'][facname] or '-'}</td></tr>
    <tr><td width="150">${_('tt_sachplan_facility_anlageart')}</td>         <td>${c['attributes'][fackind_text] or '-'}</td></tr>
	<tr><td width="150">${_('tt_sachplan_facility_anlagestatus')}</td>      <td>${c['attributes'][facstatus_text] or '-'}</td></tr>
    <tr><td width="150">${_('tt_sachplan_facility_beschlussdatum')}</td>    <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td width="150">${_('tt_sachplan_beschreibung')}</td>               <td>${c['attributes']['description'] or '-'}</td></tr>
% if 'web' in c['attributes']:
    <tr><td width="150">${_('tt_sachplan_weitereinfo')}</td>                <td><a href="${c['attributes']['web'] or '-'}" target="_blank">${_('tt_sachplan_objektblatt')}</a></td></tr>
% else:
    <tr><td width="150">${_('tt_sachplan_weitereinfo')}</td>                <td> - </td></tr>
%endif
    <tr><td width="150">${_('tt_sachplan_facility_uberobjekt')}</td>    <td>${c['attributes'][objname_text] or '-'}</td></tr>
</%def>
