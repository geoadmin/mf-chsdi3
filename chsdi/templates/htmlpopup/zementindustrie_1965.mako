<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr><td class="cell-left">${mod_translate.Translator.translate('stoff', lang)}</td><td>${c['attributes']['stoff'] or '-'}</td></tr>
</%def>
