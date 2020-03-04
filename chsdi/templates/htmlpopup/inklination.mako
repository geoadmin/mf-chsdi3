<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td class="cell-left">${mod_translate.Translator.translate('contour', lang)}</td><td>${c['attributes']['contour'] or '-'}</td></tr>
</%def>
