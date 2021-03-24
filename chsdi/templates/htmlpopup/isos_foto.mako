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
    <tr><td class="cell-left">${_(c['layerBodId']+'.url')}</td>
    % if c['attributes']['url']:
      <td><a href="${c['attributes']['url']}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${'-'}</td></tr>
    % endif
</%def>
