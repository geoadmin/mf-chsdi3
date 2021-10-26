<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['facpt_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    facptname = 'facptname_%s' % lang
    fackind = 'fackind_%s' % lang
    planningstatus = 'planningstatus_%s' % lang
    web = 'web_%s' % lang
%>
    <tr><td class="cell-left">${_('tt_sachplan_facptname')}</td>                 <td>${c['attributes'][facptname] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_facility_anlageart')}</td>        <td>${c['attributes'][fackind] or '-'}</td></tr>
	<tr><td class="cell-left">${_('tt_sachplan_planning_planungstand')}</td>     <td>${c['attributes'][planningstatus] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>              <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>              <td>${c['attributes']['description'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>
    % if c['attributes'][web]:
        <td><a href="${c['attributes'][web]}" target="_blank">${_('tt_sachplan_objektblatt')}</a></td></tr>
    % else:
        <td> - </td></tr>
    %endif
</%def>
