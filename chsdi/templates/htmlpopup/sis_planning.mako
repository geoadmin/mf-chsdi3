<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    import datetime
    lang = lang if lang in ('fr','it') else 'de'
    plname = 'plname_%s' % lang
    measuretype_text = 'meastype_text_%s' % lang
    coordinationlevel_text = 'coordlevel_text_%s' % lang
    planningstatus_text = 'plstatus_text_%s' % lang
    description_text = 'description_%s' % lang
    dateto = '-'
    datefrom = datetime.datetime.strptime(c['attributes']['validfrom'].strip(), "%Y-%m-%d").strftime("%d.%m.%Y")
    if c['attributes']['validuntil']:
        dateto = datetime.datetime.strptime(c['attributes']['validuntil'].strip(), "%Y-%m-%d").strftime("%d.%m.%Y")
%>
    <tr><td class="cell-left">${_('tt_sachplan_facility_name')}</td>           <td>${c['attributes'][plname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_typ')}</td>            <td>${c['attributes'][measuretype_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_coordstand')}</td>     <td>${c['attributes'][coordinationlevel_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_planungstand')}</td>   <td>${c['attributes'][planningstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>            <td>${datefrom or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_bis')}</td>            <td>${dateto or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>            <td>${c['attributes'][description_text] or '-'}</td></tr>
    % if c['attributes']['doc_web'] and c['attributes']['doc_title']:
    <%
        document_web_part = c['attributes']['doc_web'].split('###')
        document_title_part = c['attributes']['doc_title'].split('###')
    %>
    %  for i in range(len(document_web_part)):
        <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>         <td><a href="${document_web_part[i] or '-'}" target="_blank">${document_title_part[i] or '-'}</a></td></tr>
    %endfor
    % else:
        <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>         <td> - </td></tr>
    %endif
</%def>
