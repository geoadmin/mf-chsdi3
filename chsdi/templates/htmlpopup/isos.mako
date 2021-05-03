# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bak.bundesinventar-schuetzenswerte-ortsbilder.kanton')}</td>
    % if c['attributes']['kantone']:
      <td>${', '.join(c['attributes']['kantone'])}</td></tr>
    % else:
      <td>${'-'}</td></tr>
    % endif
    <tr><td class="cell-left">${_('ch.bak.bundesinventar-schuetzenswerte-ortsbilder.nummer')}</td>         <td>${c['attributes']['nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bak.bundesinventar-schuetzenswerte-ortsbilder.name')}</td>           <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.bak.bundesinventar-schuetzenswerte-ortsbilder.kategorie')}</td>      <td>${c['attributes']['siedlungskategorie'] or '-'}</td></tr>
    
    % if c['attributes'].get('hinweis_nummer'):
      <tr><td class="cell-left">${_(c['layerBodId']+'.hinweis_nummer')}</td>         <td>${c['attributes']['hinweis_nummer'] or '-'}</td></tr>
      <tr><td class="cell-left">${_(c['layerBodId']+'.hinweis_name')}</td>           <td>${c['attributes']['hinweis_name']}</td></tr>
    % endif
       
    % if c['attributes'].get('teil_nummer') :
      <tr><td class="cell-left">${_(c['layerBodId']+'.teil_nummer')}</td>         <td>${c['attributes']['teil_nummer'] or '-'}</td></tr>
      <tr><td class="cell-left">${_(c['layerBodId']+'.teil_name')}</td>           <td>${c['attributes']['teil_name']}</td></tr>
    % endif

    % if c['attributes'].get('hinweis_nummer'):
      <tr><td class="cell-left">${_(c['layerBodId']+'.siehe_auch')}</td>
      % if c['attributes']['siehe_auch']:
        <td>${', '.join(c['attributes']['siehe_auch'])}</td></tr>
      % else:
        <td>${'-'}</td></tr>
      % endif
    % endif
    
    <tr><td class="cell-left">${_(c['layerBodId']+'.url')}</td>
    % if c['attributes']['url']:
      <td><a href="${c['attributes']['url']}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${'-'}</td></tr>
    % endif
</%def>
