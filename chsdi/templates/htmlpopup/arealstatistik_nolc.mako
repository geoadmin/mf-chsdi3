# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
  <tr>
    <td class="cell-left-large">${_('fj')}</td>
    <td>${c['attributes']['fj'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('as_27')}</td>
    <td>${c['attributes']['fj'] or '-'}</td>
  </tr>
</%def>
