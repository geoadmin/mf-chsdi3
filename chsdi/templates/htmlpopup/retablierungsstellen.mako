<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.retablierungsstellen.name', lang)}</td>
	<td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.retablierungsstellen.url', lang)}</td>
    <td><a href="${c['attributes']['url'] or '-'}" target="_blank">${mod_translate.Translator.translate('ch.vbs.retablierungsstellen.url', lang)}</a></td></tr>
</%def>

