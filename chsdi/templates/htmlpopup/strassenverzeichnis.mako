<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    validated = 'yesText' if c['attributes']['validated'] == 1 else 'noText'
    official = 'yesText' if c['attributes']['official'] == 1 else 'noText'
    %>

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.esid', lang)}</td>                 <td>${c['attributes']['esid'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.label', lang)}</td>                 <td>${c['attributes']['label'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.plzo', lang)}</td>                 <td>${c['attributes']['plzo'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.gdenr', lang)}</td>                 <td>${c['attributes']['gdenr'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.gdename', lang)}</td>                 <td>${c['attributes']['gdename'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.type', lang)}</td>                 <td>${mod_translate.Translator.translate(c['attributes']['type'] or '-', lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.status', lang)}</td>                 <td>${mod_translate.Translator.translate(c['attributes']['status'] or '-', lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.official', lang)}</td>                 <td>${mod_translate.Translator.translate(official, lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.validated', lang)}</td>                 <td>${mod_translate.Translator.translate(validated, lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.modified', lang)}</td>                 <td>${mod_translate.Translator.translate(c['attributes']['modified'] or '-', lang)}</td></tr>
</%def>
