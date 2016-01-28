# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    surface_ha = round(c['attributes']['bgdi_surface'],2)
    zone = 'type_%s' % lang
    name = 'name_%s' % lang
%>

    <tr><td class="cell-left">${_('bak_unesco_weltkulturerbe_name')}</td>     <td>${c['attributes'][name] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bak.schutzgebiete-unesco_weltkulturerbe_type')}</td>  <td>${c['attributes'][zone] or '-'}</td></tr>
    <tr><td class="cell-left">${_('bak_unesco_weltkulturerbe_flaeche')}</td>  <td>${surface_ha}</td></tr>
</%def>
