<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.bundestankstellen-bebeco.ort', lang)}</td>
	<td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.bundestankstellen-bebeco.plz', lang)}</td>
    <td>${c['attributes']['plz'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.bundestankstellen-bebeco.strasse', lang)}</td>
    <td>${c['attributes']['strasse'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.bundestankstellen-bebeco.bezugszeit', lang)}</td>
    <td>${c['attributes']['bezugszeit'] or '-'}</td></tr>

</%def>

