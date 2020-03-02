# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left-large">${Translator.translate('gmde', lang)}</td>                   <td>${c['attributes']['gmde'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${Translator.translate('fj85', lang)}</td>                   <td>${c['attributes']['fj85'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${Translator.translate('id_arealstatistik_85', lang)}</td>   <td>${c['attributes']['id_arealstatistik_85'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${Translator.translate('fj97', lang)}</td>                   <td>${c['attributes']['fj97'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${Translator.translate('id_arealstatistik_97', lang)}</td>   <td>${c['attributes']['id_arealstatistik'] or '-'}</td></tr>
</%def>
