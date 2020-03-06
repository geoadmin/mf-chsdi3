# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left">${h.translate('ch.bafu.bundesinventare-bln.bln_obj', lang)}</td>
    <td>${c['attributes']['bln_obj'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${h.translate('ch.bafu.bundesinventare-bln.bln_name', lang)}</td>
    <td>${c['attributes']['bln_name']}</td>
  </tr>
  <tr>
    <td class="cell-left">${h.translate('ch.bafu.bundesinventare-bln.subareanumber', lang)}</td>
    <td>${c['attributes']['subareanumber'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${h.translate('ch.bafu.bundesinventare-bln.subareaname', lang)}</td>
    <td>${c['attributes']['subareaname'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${h.translate('ch.bafu.bundesinventare-bln.bln_fl', lang)}</td>
    <td>${round(c['attributes']['bln_fl'],2) or '-'}</td>
  </tr>
  <tr>
      <td class="cell-left">${h.translate('ch.bafu.bundesinventare-bln.linkurldescription', lang)}</td>
      <td><a target="_blank" href="${c['attributes']['linkurldescription']}">Link</a></td>
  </tr>
</%def>
