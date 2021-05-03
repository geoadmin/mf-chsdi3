# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
c['stable_id'] = True

lang = 'de' if lang == 'rm' else lang
info_url = 'url_%s' % lang
pdf = 'pdf_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.belplan_id')}</td>       <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.bezeichnung')}</td>      <td>${c['attributes']['bezeichnung'] or '-'}</td></tr>
    ## auskunft
    <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.auskunft')}</td>
    <td>
    % for info in ['infobezeichnung', 'infotelefonnr', 'infoemail']:
      % if c['attributes'][info]:
        % if info == 'infoemail':
          <a href="mailto:${c['attributes'][info]}">${c['attributes'][info]}</a>
        % else:
          ${c['attributes'][info]}<br/>
        % endif
      % endif
    % endfor
    </td></tr>
    ## url
    <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.url')}</td> 
    % if c['attributes'][info_url]:
      <td><a href="${c['attributes'][info_url]}" target="_blank">${_('ch.vbs.schiessanzeigen.url')}</a></td></tr>
    % else:
      <td>-</td></tr>
    % endif
    ## time data
    <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.belegung')}</td>        <td>
    % if c['attributes']['wochentag']:
      <table>
    ## # iterating weekdays
      % for i in range(len(c['attributes']['wochentag'])):
        <tr><td>${_('ch.vbs.schiessanzeigen.wochentag.%s' % str(c['attributes']['wochentag'][i]%7+1))}</td>
        <td>${c['attributes']['belegungsdatum'][i].strftime("%d.%m.%Y")}</td>
    ## # special case no shooting
        % if c['attributes']['kein_schiessen'][i]:
        <td colspan="2">${_('ch.vbs.schiessanzeigen.kein_schiessen')}</td></tr>
        % else:
          <td>${'%s - %s' % (c['attributes']['zeit_von'][i], c['attributes']['zeit_bis'][i])}</td>
          <td><a href="${c['attributes'][pdf][i]}" target="_blank">PDF</a></td></tr>
        % endif
      % endfor
      </table>
    ## # no information available
    % else:
      ${_('ch.vbs.schiessanzeigen.keine_info')}
    % endif
    </td></tr>
</%def>
