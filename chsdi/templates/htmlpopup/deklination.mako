<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td class="cell-left">${mod_translate.Translator.translate('deklination', lang)}</td><td>${c['attributes']['magne'] or '-'}</td></tr>
</%def>
