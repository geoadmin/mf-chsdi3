# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<% c[stable_id] = True %>
    <tr><td width="320">${_('gmde')}</td>                   <td>${c['attributes']['gmde'] or '-'}</td></tr>
    <tr><td width="320">${_('fj85')}</td>                   <td>${c['attributes']['fj85'] or '-'}</td></tr>
    <tr><td width="320">${_('id_arealstatistik_85')}</td>   <td>${c['attributes']['id_arealstatistik_85'] or '-'}</td></tr>
    <tr><td width="320">${_('fj97')}</td>                   <td>${c['attributes']['fj97'] or '-'}</td></tr>
    <tr><td width="320">${_('id_arealstatistik_97')}</td>   <td>${c['attributes']['id_arealstatistik'] or '-'}</td></tr>
</%def>
