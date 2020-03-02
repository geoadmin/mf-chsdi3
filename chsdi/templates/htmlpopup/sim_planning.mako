<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% 
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    plname = 'plname_%s' % lang
    facname = 'facname_%s' % lang
    measuretype_text = 'meastype_text_%s' % lang
    coordinationlevel_text = 'coordlevel_text_%s' % lang
    planningstatus_text = 'plstatus_text_%s' % lang
    description_text = 'description_%s' % lang
%>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_planning_name', lang)}</td>
      <td>${c['attributes'][plname]}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_planning_typ', lang)}</td>
      <td>${c['attributes'][measuretype_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_planning_coordstand', lang)}</td>
      <td>${c['attributes'][coordinationlevel_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_planning_planungstand', lang)}</td>
      <td>${c['attributes'][planningstatus_text] or '-'}</td>
    </tr>
	  <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_planning_von', lang)}</td>
      <td>${c['attributes']['validfrom'] or '-'}</td>
    </tr>
	  <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_planning_bis', lang)}</td>
      <td>${c['attributes']['validuntil'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_beschreibung', lang)}</td>
      <td>${c['attributes'][description_text] or '-'}</td>
    </tr>
% if c['attributes']['doc_web']:
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_weitereinfo', lang)}</td>
      <td><a href="${c['attributes']['doc_web'] or '-'}" target="_blank">${t.Translator.translate('tt_sachplan_objektblatt', lang)}</a></td></tr>
% else:
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_sachplan_weitereinfo', lang)}</td>
      <td> - </td>
    </tr>
%endif
</%def>
