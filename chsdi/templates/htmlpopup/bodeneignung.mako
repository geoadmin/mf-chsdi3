# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
      <td class="cell-left">${_('bodeneignung_id')}</td>
      <td>${c['attributes']['farbe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('bodeneignung_eignungsei')}</td>
      <td>${c['attributes']['eignungsei'] or '-'}</td>
    </tr>
</%def>
