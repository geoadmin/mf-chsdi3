# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    surface_ha = round(c['attributes']['bgdi_surface'],2)
    zone = 'type_%s' % lang
    name = 'name_%s' % lang
%>

    <tr><td class="cell-left">${t.translate('bak_unesco_weltkulturerbe_name', lang)}</td>     <td>${c['attributes'][name] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bak.schutzgebiete-unesco_weltkulturerbe_type', lang)}</td>  <td>${c['attributes'][zone] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('bak_unesco_weltkulturerbe_flaeche', lang)}</td>  <td>${surface_ha}</td></tr>
</%def>
