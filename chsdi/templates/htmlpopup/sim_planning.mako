<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% 
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    plname = 'plname_%s' % lang
    measuretype_text = 'meastype_text_%s' % lang
    coordinationlevel_text = 'coordlevel_text_%s' % lang
    planningstatus_text = 'plstatus_text_%s' % lang
    description_text = 'description_%s' % lang
%>
    <tr><td class="cell-left">${_('tt_sachplan_planning_name')}</td>           <td>${c['attributes'][plname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_typ')}</td>            <td>${c['attributes'][measuretype_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_coordstand')}</td>     <td>${c['attributes'][coordinationlevel_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_planungstand')}</td>   <td>${c['attributes'][planningstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>            <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_bis')}</td>            <td>${c['attributes']['validuntil'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>            <td>${c['attributes'][description_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>
    % if c['attributes']['doc_web']:
        <td><a href="${c['attributes']['doc_web'] or '-'}" target="_blank">${_('tt_sachplan_objektblatt')}</a></td></tr>
    % else:
        <td> - </td></tr>
    %endif
</%def>
