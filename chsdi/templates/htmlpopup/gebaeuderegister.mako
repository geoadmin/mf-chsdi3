# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
c['stable_id'] = True
street_key = 'strname1'
if 'strname_de' in c['attributes']:
  lang = lang if lang not in ['fr', 'it', 'rm'] else 'de'
  if c['attributes']['strname_%s' % lang]:
    street_key = 'strname_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.egid')}</td>       <td>${c['attributes']['egid'] or '-'}</td></tr>
    % if c['attributes']['strname1'] <> '':
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.strname1')}</td>    <td>${c['attributes'][street_key]}</td></tr>
    % else:
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.strname1')}</td>    <td>${c['attributes']['deinr'] or '-'}</td></tr>
    % endif
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.deinr')}</td>         <td>${c['attributes']['deinr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.plz4')}</td>        <td>${c['attributes']['plz4'] or '-'}</td></tr>
    <tr><td class="cell-left">PLZ6</td><td>${c['attributes']['plz6'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.plzname')}</td>        <td>${c['attributes']['plzname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.gdename')}</td>   <td>${c['attributes']['gdename'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('bfsnr')}</td>      <td>${c['attributes']['gdenr'] or '-'}</td></tr>
</%def>
