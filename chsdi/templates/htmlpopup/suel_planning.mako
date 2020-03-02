<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    name = c['layerBodId'] + '.' + 'plname_%s' % lang
    doc_title = c['layerBodId'] + '.' + 'doc_title'
%>

<%
import datetime
lang = lang if lang in ('fr','it') else 'de'
plname = 'plname_%s' % lang
facname = 'facname_%s' % lang
measuretype_text = 'meastype_text_%s' % lang
coordinationlevel_text = 'coordlevel_text_%s' % lang
planningstatus_text = 'plstatus_text_%s' % lang
description_text = 'description_%s' % lang
dateto = '-'
datefrom = c['attributes']['validfrom']
if c['attributes']['validuntil']:
    dateto = c['attributes']['validuntil']
endif
%>
    <tr>
      <td class="cell-left">${_(name)}</td>
      <td>${c['attributes'][plname]}</td>
    </tr>
    <tr>
      <td class="cell-left">${Translator.translate('tt_sachplan_planning_typ', lang)}</td>
      <td>${c['attributes'][measuretype_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${Translator.translate('tt_sachplan_planning_coordstand', lang)}</td>
      <td>${c['attributes'][coordinationlevel_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${Translator.translate('tt_sachplan_planning_planungstand', lang)}</td>
      <td>${c['attributes'][planningstatus_text] or '-'}</td>
    </tr>
	  <tr>
      <td class="cell-left">${Translator.translate('tt_sachplan_planning_von', lang)}</td>
      <td>${datefrom or '-'}</td>
    </tr>
	  <tr>
      <td class="cell-left">${Translator.translate('tt_sachplan_planning_bis', lang)}</td>
      <td>${dateto or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${Translator.translate('tt_sachplan_beschreibung', lang)}</td>
      <td>${c['attributes'][description_text] or '-' | n}</td>
    </tr>
% if c['attributes']['doc_web']:
    <tr>
      <td class="cell-left">${_(doc_title)}</td>
      <td><a href="${c['attributes']['doc_web']}" target="_blank">${c['attributes']['doc_title'] or '-'}</a></td></tr>
% else:
    <tr>
      <td class="cell-left">${Translator.translate('tt_sachplan_weitereinfo', lang)}</td>
      <td> - </td>
    </tr>
%endif
</%def>
