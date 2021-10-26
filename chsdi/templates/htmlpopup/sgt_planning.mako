<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['pmarea_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    pmname = 'pmname_%s' % lang
    pmkind = 'pmkind_%s' % lang
    coordlevel = 'coordlevel_%s' % lang
    planningstatus = 'planningstatus_%s' % lang
    web = 'web_%s' % lang
%>
    <tr><td class="cell-left">${_('tt_sachplan_pmname')}</td>                    <td>${c['attributes'][pmname] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_typ')}</td>              <td>${c['attributes'][pmkind] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_coordstand')}</td>       <td>${c['attributes'][coordlevel] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_planungstand')}</td>     <td>${c['attributes'][planningstatus] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>              <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>              <td>${c['attributes']['validuntil'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>              <td>${c['attributes']['description'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_weitereinfo')}</td>
    % if c['attributes'][web]:
        <td><a href="${c['attributes'][web]}" target="_blank">${_('tt_sachplan_objektblatt')}</a></td></tr>
    % else:
        <td> - </td></tr>
    %endif
</%def>
