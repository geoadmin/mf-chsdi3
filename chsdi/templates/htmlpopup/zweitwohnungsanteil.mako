# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('fr','it','rm','en') else 'de'
    zwg_3200 = 'zwg_3200_%s' % lang
%>
    <tr><td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3150')}</td>                   <td>${c['attributes']['zwg_3150'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3010')}</td>                   <td>${c['attributes']['zwg_3010'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3100')}</td>                   <td>${c['attributes']['zwg_3100'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3110')}</td>                   <td>${c['attributes']['zwg_3110'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3120')}</td>                   <td>${c['attributes']['zwg_3120'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3200')}</td>                   <td>${c['attributes'][zwg_3200] or '-'}</td></tr>
</%def>
