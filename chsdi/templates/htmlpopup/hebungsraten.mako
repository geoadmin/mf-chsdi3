# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
% if 'ord_nr' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.ord_nr')}</td><td>${c['attributes']['ord_nr'] or '-'}</td></tr>
% endif
% if 'ort' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.ort')}</td><td>${c['attributes']['ort'] or '-'}</td></tr>
% endif
% if 'y' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.y')}</td><td>${c['attributes']['y'] or '-'}</td></tr>
% endif
% if 'x' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.x')}</td><td>${c['attributes']['x'] or '-'}</td></tr>
% endif
% if 'h' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.h')}</td><td>${c['attributes']['h'] or '-'}</td></tr>
% endif
% if 'v' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.v')}</td><td>${c['attributes']['v'] or '-'}</td></tr>
% endif
% if 'mfv' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.mfv')}</td><td>${c['attributes']['mfv'] or '-'}</td></tr>
% endif
% if 'klasse' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.klasse')}</td><td>${c['attributes']['klasse'] or '-'}</td></tr>
% endif
% if 'contour' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.hebungsraten.contour')}</td><td>${str(c['attributes']['contour']) or '-'}</td></tr>
% endif
</%def>


