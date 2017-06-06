# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left">${_('ch.bafu.bundesinventare-bln.bln_obj')}</td>
    <td>${c['attributes']['bln_obj'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.bundesinventare-bln.bln_name')}</td>
    <td>${c['attributes']['bln_name']}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.bundesinventare-bln.subareanumber')}</td>
    <td>${c['attributes']['subareanumber'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.bundesinventare-bln.subareaname')}</td>
    <td>${c['attributes']['subareaname'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.bundesinventare-bln.bln_fl')}</td>
    <td>${round(c['attributes']['bln_fl'],2) or '-'}</td>
  </tr>
  <tr>
      <td class="cell-left">${_('ch.bafu.bundesinventare-bln.linkurldescription')}</td>
      <td><a target="_blank" href="${c['attributes']['linkurldescription']}">Link</a></td>
  </tr>
</%def>
