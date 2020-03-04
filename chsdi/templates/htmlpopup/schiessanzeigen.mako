# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
lang = 'de' if lang == 'rm' else lang
info_url = 'url_%s' % lang
arr_wochentage = []
if c['attributes']['wochentag']:
  arr_wochentage     = str(c['attributes']['wochentag']).split(';')
  arr_belegungsdatum = str(c['attributes']['belegungsdatum']).split(';')
  arr_zeit_von       = str(c['attributes']['zeit_von']).split(';')
  arr_zeit_bis       = str(c['attributes']['zeit_bis']).split(';')
counter = 0
%>
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.bezeichnung')}</td>       <td>${c['attributes']['bezeichnung'] or '-'}</td></tr>
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
    % if c['attributes'][info_url]:
      <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.url')}</td>            <td><a href="${c['attributes'][info_url]}" target="_blank">${c['attributes'][info_url]}</a></td></tr>
    % else:
      <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.url')}</td>            <td>-</td></tr>
    % endif
    ## time data
    <tr><td class="cell-left">${_('ch.vbs.schiessanzeigen.belegung')}</td>        <td>
    ## # no information available
    % if len(arr_wochentage) == 0:
        ${_('ch.vbs.schiessanzeigen.keine_info')}
    ## # info available
    % else:
      <table>
    ## # iterating weekdays
      % for wochentag in arr_wochentage:
        <%
           zeit = '%s - %s' % (arr_zeit_von[counter], arr_zeit_bis[counter])
           wochentag = _('ch.vbs.schiessanzeigen.wochentag.%s' % wochentag)
        %>
    ## # spetial case 0 and 0 means no shooting
        % if zeit == '0 - 0':
          <tr><td><${wochentag}</td><td>${arr_belegungsdatum[counter]}</td><td>${_('ch.vbs.schiessanzeigen.kein_schiessen')}</td></tr>
        % else:
          <tr><td>${wochentag}</td><td>${arr_belegungsdatum[counter]}</td><td>${zeit}</td></tr>
        % endif
        <% counter += 1 %>
      % endfor
      </table>
    % endif
    </td></tr>
</%def>
