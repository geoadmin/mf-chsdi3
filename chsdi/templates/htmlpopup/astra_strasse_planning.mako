<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    plname = 'plname_%s' % lang
    meastype_text = 'meastype_text_%s' % lang
    coordlevel_text = 'coordlevel_text_%s' % lang
    plstatus_text = 'plstatus_text_%s' % lang
    description = 'description_%s' % lang
%>
    <tr><td class="cell-left">${_('tt_sachplan_planning_name')}</td>             <td>${c['attributes'][plname] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_typ')}</td>              <td>${c['attributes'][meastype_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_coordstand')}</td>       <td>${c['attributes'][coordlevel_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_planungstand')}</td>     <td>${c['attributes'][plstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>              <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_bis')}</td>              <td>${c['attributes']['validuntil'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>              <td>${c['attributes'][description] or '-'}</td></tr>
    %  if c['attributes']['doc_web'] and c['attributes']['doc_title']:
    <%
        doc_web_part = c['attributes']['doc_web'].split('###')
        doc_title_part = c['attributes']['doc_title'].split('###')
    %>
    %  for i in range(len(doc_web_part)):
        <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>           <td><a href="${doc_web_part[i] or '-'}" target="_blank">${doc_title_part[i] or '-'}</a></td></tr>
    %endfor
    % else:
        <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>           <td> - </td></tr>
    %endif
</%def>
