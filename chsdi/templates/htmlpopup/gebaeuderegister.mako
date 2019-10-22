# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
  c['stable_id'] = True
  street_key = 'strname1'
  lang = lang if lang in ('fr', 'it', 'rm') else 'de'
  topic = request.matchdict.get('map')
  datageoadminhost = request.registry.settings['datageoadminhost']
  canton = c['attributes']['gdekt']
  bfs_nr = c['attributes']['gdenr']
  url_canton = 'https://%s/ch.bfs.gebaeude_wohnungs_register/CSV/%s/%s.zip' % (datageoadminhost, canton, canton)
  url_municipality = 'https://%s/ch.bfs.gebaeude_wohnungs_register/CSV/%s/%s.zip' % (datageoadminhost, canton, bfs_nr)
  if 'strname_de' in c['attributes']:
    if c['attributes']['strname_%s' % lang]:
      street_key = 'strname_%s' % lang
  pdf_url = ' https://www.housing-stat.ch/regbl/resources/public/geb_public/%s?lang=%s' % (c['attributes']['egid'], lang)
%>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.egid')}</td>       <td>${c['attributes']['egid'] or '-'}</td></tr>
    % if c['attributes']['strname1'] != '':
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.strname1')} ${_('ch.bfs.gebaeude_wohnungs_register.deinr')}</td>    <td>${c['attributes'][street_key] or '-'} ${c['attributes']['deinr'] or ''}</td></tr>
    % else:
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.strname1')} ${_('ch.bfs.gebaeude_wohnungs_register.deinr')}</td>    <td>${c['attributes']['deinr'] or '-'}</td></tr>
    % endif
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.plz4')}/${_('ch.bfs.gebaeude_wohnungs_register.plz4')}6</td>        <td>${c['attributes']['plz4'] or '-'}/${c['attributes']['plz6'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.plzname')}</td>        <td>${c['attributes']['plzname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.gdename')}</td>   <td>${c['attributes']['gdename'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('bfsnr')}</td>      <td>${bfs_nr or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.pdf')}</td>      <td><a href="${pdf_url}">PDF</a></td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.download')}</td>     <td><a href="${url_canton}"> ${_('ch.bfs.gebaeude_wohnungs_register.canton_label')}</a></td></tr>
    <tr><td></td>      <td><a href="${url_municipality}">${_('ch.bfs.gebaeude_wohnungs_register.municipality_label')}</a></td></tr>
</%def>
