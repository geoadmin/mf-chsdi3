<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr><td class="cell-left">${t.Translator.translate('gesteinsgr', lang)}</td><td>${c['attributes']['gesteinsgr'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.Translator.translate('gestein', lang)}</td><td>${c['attributes']['gestein'] or '-'}</td></tr>
</%def>
