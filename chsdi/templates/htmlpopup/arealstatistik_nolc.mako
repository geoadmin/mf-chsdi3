# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
  <tr>
    <td class="cell-left-large">${_('survey')}</td><td>${c['attributes']['survey'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('lc_27')}</td><td>${c['attributes']['lc_27'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('fj')}</td><td>${c['attributes']['fj'] or '-'}</td>
  </tr>
</%def>
