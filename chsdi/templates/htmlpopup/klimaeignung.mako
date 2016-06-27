# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
      <td class="cell-left">${_('klimaeignung_be')}</td>
      <td>${c['attributes']['klimeig_be'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('klimaeignung_zone')}</td>
      <td>${c['attributes']['zone'] or '-'}</td>
    </tr>
</%def>
