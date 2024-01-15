<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% 
    lang = lang if lang in ('fr','it') else 'de'
    facname = 'facname_%s' % lang
    measuretype_text = 'meastype_text_%s' % lang
    coordinationlevel_text = 'coordlevel_text_%s' % lang
    planningstatus_text = 'plstatus_text_%s' % lang
    description_text = 'description_%s' % lang
    gesamtbericht = 'ch.bav.sachplan-unterirdischer-guetertransport_kraft.obj_blatt_alt'
    objektblatt = 'tt_sachplan_objektblatt'
%>
    <tr><td class="cell-left">${_('tt_sachplan_planning_name')}</td>           <td>${c['attributes'][facname]}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_typ')}</td>            <td>${c['attributes'][measuretype_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_coordstand')}</td>     <td>${c['attributes'][coordinationlevel_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_planungstand')}</td>   <td>${c['attributes'][planningstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_beschreibung')}</td>            <td>${c['attributes'][description_text] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_von')}</td>            <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_sachplan_planning_bis')}</td>            <td>${c['attributes']['validuntil'] or '-'}</td></tr>
    <td class="cell-left">${_(gesamtbericht)}</td>
    <td>
% if c['attributes']['doc_gesamtbericht_web'] != None:
        <a href="${c['attributes']['doc_gesamtbericht_web']}" target="_balnk">${c['attributes']['doc_gesamtbericht_title'] or '-'}</a>
% else:
        ${c['attributes']['doc_gesamtbericht_title'] or '-'}
% endif
    </td>
</tr>
<tr>
    <td class="cell-left">${_(objektblatt)}</td>
    <td>
% if c['attributes']['doc_objektblatt_web'] != None:
        <a href="${c['attributes']['doc_objektblatt_web']}" target="_balnk">${c['attributes']['doc_objektblatt_title'] or '-'}</a>
% else:
        ${c['attributes']['doc_objektblatt_title'] or '-'}
% endif
    </td>
</tr>
</%def>
