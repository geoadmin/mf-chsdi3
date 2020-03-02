<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    validated = 'yesText' if c['attributes']['validated'] == 1 else 'noText'
    official = 'yesText' if c['attributes']['official'] == 1 else 'noText'
    %>

    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.esid', lang)}</td>                 <td>${c['attributes']['esid'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.label', lang)}</td>                 <td>${c['attributes']['label'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.plzo', lang)}</td>                 <td>${c['attributes']['plzo'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.gdenr', lang)}</td>                 <td>${c['attributes']['gdenr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.gdename', lang)}</td>                 <td>${c['attributes']['gdename'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.type')}</td>                 <td>${_(c['attributes']['type'] or '-', lang)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.status')}</td>                 <td>${_(c['attributes']['status'] or '-', lang)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.official', lang)}</td>                 <td>${_(official)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.validated', lang)}</td>                 <td>${_(validated)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.amtliches-strassenverzeichnis.modified')}</td>                 <td>${_(c['attributes']['modified'] or '-', lang)}</td></tr>
</%def>
