# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr><td class="cell-left">${t.translate('objektname', lang)}</td><td>${c['attributes']['jb_name']}</td></tr>
  <tr><td class="cell-left">${t.translate('objektnr', lang)}</td><td>${c['attributes']['jb_obj'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('kategorie', lang)}</td><td>${c['attributes']['jb_kat'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('flaeche_ha', lang)}</td><td>${c['attributes']['jb_fl'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('gesamtflaeche_ha', lang)}</td><td>${c['attributes']['jb_gf'] or '-'}</td></tr>
</%def>
