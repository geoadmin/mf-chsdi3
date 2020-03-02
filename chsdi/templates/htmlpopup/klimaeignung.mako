# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
      <td class="cell-left">${t.Translator.translate('klimaeignung_be', lang)}</td>
      <td>${c['attributes']['klimeig_be'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('klimaeignung_zone', lang)}</td>
      <td>${c['attributes']['zone'] or '-'}</td>
    </tr>
</%def>
