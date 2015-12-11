# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
% if 'name' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.transformation-bezugsrahmen_hoehe.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
% endif
% if 'y' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.transformation-bezugsrahmen_hoehe.y')}</td><td>${c['attributes']['y'] or '-'}</td></tr>
% endif
% if 'x' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.transformation-bezugsrahmen_hoehe.x')}</td><td>${c['attributes']['x'] or '-'}</td></tr>
% endif
% if 'or_ln02_cm' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.transformation-bezugsrahmen_hoehe.or_ln02_cm')}</td><td>${c['attributes']['or_ln02_cm'] or '-'}</td></tr>
% endif
% if 'contour' in c['attributes']:
    <tr><td class="cell-left">${_('ch.swisstopo.transformation-bezugsrahmen_hoehe.contour')}</td><td>${str(int(c['attributes']['contour'])) or '-'}</td></tr>
% endif
</%def>


