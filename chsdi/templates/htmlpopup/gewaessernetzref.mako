<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = 'fr' if lang == 'it' else lang
    lang = 'de' if lang != 'fr' else lang
    objectval = 'objectval_%s' % lang

%>

    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.vec25-gewaessernetz_referenz.name', lang)}</td>                <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.vec25-gewaessernetz_referenz.gewissnr', lang)}</td>            <td>${c['attributes']['gewissnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.vec25-gewaessernetz_referenz.gwlnr', lang)}</td>               <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.vec25-gewaessernetz_referenz.objectval', lang)}</td>           <td>${c['attributes'][objectval] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.vec25-gewaessernetz_referenz.objectid', lang)}</td>            <td>${c['attributes']['objectid'] or '-'}</td></tr>
</%def>
