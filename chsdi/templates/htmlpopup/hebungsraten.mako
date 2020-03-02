# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
% if 'ord_nr' in c['attributes']:
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.ord_nr', lang)}</td><td>${c['attributes']['ord_nr'] or '-'}</td></tr>
% endif
% if 'ort' in c['attributes']:
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.ort', lang)}</td><td>${c['attributes']['ort'] or '-'}</td></tr>
% endif
% if 'v' in c['attributes']:
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.v', lang)}</td><td>${round(c['attributes']['v'],5) or '0.00'}</td></tr>
% endif
% if 'mfv' in c['attributes']:
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.mfv', lang)}</td><td>${"%.2f"%c['attributes']['mfv'] or '0'}</td></tr>
% endif
% if 'klasse' in c['attributes']:
   % if c['attributes']['klasse']== 'TYP1':
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ1', lang)}</td></tr>
   % elif c['attributes']['klasse']== 'TYP2':
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ2', lang)}</td></tr>
   % elif c['attributes']['klasse']== 'TYP3':
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ3', lang)}</td></tr>
   % elif c['attributes']['klasse']== 'TYP4':
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ4', lang)}</td></tr>
   % else :
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ99', lang)}</td></tr>
   %endif
% endif
% if 'contour' in c['attributes']:
    <tr><td class="cell-left">${t.translate('ch.swisstopo.hebungsraten.contour', lang)}</td><td>${round(c['attributes']['contour'],1)}</td></tr>
% endif
</%def>


