# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
% if 'ord_nr' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.ord_nr')}</td><td>${c['attributes']['ord_nr'] or '-'}</td></tr>
% endif
% if 'ort' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.ort')}</td><td>${c['attributes']['ort'] or '-'}</td></tr>
% endif
% if 'v' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.v')}</td><td>${round(c['attributes']['v'],5) or '0.00'}</td></tr>
% endif
% if 'mfv' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.mfv')}</td><td>${"%.2f"%c['attributes']['mfv'] or '0'}</td></tr>
% endif
% if 'klasse' in c['attributes']:
   % if c['attributes']['klasse']== 'TYP1':
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ1')}</td></tr>
   % elif c['attributes']['klasse']== 'TYP2':
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ2')}</td></tr>
   % elif c['attributes']['klasse']== 'TYP3':
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ3')}</td></tr>
   % elif c['attributes']['klasse']== 'TYP4':
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ4')}</td></tr>
   % else :
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.klasse')}</td><td>${_('ch.swisstopo.hebungsraten.typ99')}</td></tr>
   %endif
% endif
% if 'contour' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.contour')}</td><td>${round(c['attributes']['contour'],1)}</td></tr>
% endif
</%def>


