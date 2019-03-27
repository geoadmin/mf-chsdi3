# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('de','fr','it','rm','en') else None
    verfahren_code = 'ch.are.wohnungsinventar-zweitwohnungsanteil.verfahren_' + str(c['attributes']['verfahren'])
    status = 'ch.are.wohnungsinventar-zweitwohnungsanteil.status_' + str(c['attributes']['status'])
%>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_gem_no')}</td>
      <td>${c['attributes']['gemeinde_nummer'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_gemeinde')}</td>
      <td>${c['attributes']['gemeinde_name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3150')}</td>
      <td>${c['attributes']['zwg_3150'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3010')}</td>
      <td>${c['attributes']['zwg_3010'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3100')}</td>
      <td>${c['attributes']['zwg_3100'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3110')}</td>
      <td>${round(c['attributes']['zwg_3110'],1) or '-'} %</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3120')}</td>
      <td>${round(c['attributes']['zwg_3120'],1) or '-'} %</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_zwg_3200')}</td>
      <td>${_(verfahren_code) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.are.wohnungsinventar-zweitwohnungsanteil_status')}</td>
      <td>${_(status) or '-'}</td>
    </tr>
</%def>
