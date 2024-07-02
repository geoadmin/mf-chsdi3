# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    desc_text = 'desc_lc09r_27_%s' % lang
%>
  <tr>
    <td class="cell-left">${_('ch.bfs.arealstatistik.survey')}</td><td>${c['attributes']['survey'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bfs.arealstatistik-bodenbedeckung.desc_lc09r_27')}</td><td>${c['attributes'][desc_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bfs.arealstatistik.fj')}</td><td>${c['attributes']['fj'] or '-'}</td>
  </tr>
</%def>
