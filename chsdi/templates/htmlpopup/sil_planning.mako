<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% 
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    plname = 'plname_%s' % lang
    measuretype_text = 'measuretype_text_%s' % lang
    coordinationlevel_text = 'coordinationlevel_text_%s' % lang
    planningstatus_text = 'planningstatus_text_%s' % lang
    description_text = 'description_text_%s' % lang
%>
    <tr><td class="cell-left">${_('tt_sachplan_planning_name')}</td>           <td>${c['attributes'][plname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_typ')}</td>            <td>${c['attributes'][measuretype_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_coordstand')}</td>     <td>${c['attributes'][coordinationlevel_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_planungstand')}</td>   <td>${c['attributes'][planningstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>            <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_bis')}</td>            <td>${c['attributes']['validuntil'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>            <td>${c['attributes'][description_text] or '-'}</td></tr>
    %  if c['attributes']['document_web'] and c['attributes']['document_title']:
    <%
        document_web_part = c['attributes']['document_web'].split('###')
        document_title_part = c['attributes']['document_title'].split('###')
    %>
    %  for i in range(len(document_web_part)):
        <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>           <td><a href="${document_web_part[i] or '-'}" target="_blank">${document_title_part[i] or '-'}</a></td></tr>
    %endfor
    % else:
        <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>           <td> - </td></tr>
    %endif
</%def>
