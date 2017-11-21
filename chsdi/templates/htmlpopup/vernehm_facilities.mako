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
    <tr><td class="cell-left">${_('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung.facptname')}</td>              <td>${c['attributes'][facptname] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung.fackind')}</td>         <td>${c['attributes'][fackind] or '-'}</td></tr>
	<tr><td class="cell-left">${_('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung.planningstatus')}</td>      <td>${c['attributes'][planningstatus] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung.validfrom')}</td>    <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung.description')}</td>               <td>${c['attributes']['description'] or '-'}</td></tr>
% if c['attributes'][web]:
    <tr><td class="cell-left">${_('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung.web')}</td>                <td><a href="${c['attributes'][web]}" target="_blank">${_('tt_sachplan_objektblatt')}</a></td></tr>
% else:
    <tr><td class="cell-left">${_('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung.web')}</td>                <td> - </td></tr>
%endif
</%def>
