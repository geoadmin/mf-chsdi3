<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it') else 'de'
    schutzkat = 'schutzkategorie_%s' % lang
    schutzeb = 'schutzebene_%s' % lang
%>

    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.name', lang)}</td>         <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.objnummer', lang)}</td>          <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.teilgebiet', lang)}</td>         <td>${c['attributes']['teilgebiet'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.schutzkategorie', lang)}</td>         <td>${c['attributes'][schutzkat] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.schutzebene', lang)}</td>         <td>${c['attributes'][schutzeb] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.shape_area', lang)}</td>          <td>${round(c['attributes']['shape_area']/10000) or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.obj_gisflaeche', lang)}</td>         <td>${round(c['attributes']['obj_gisflaeche']) or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-vogelreservate.refobjblatt', lang)}</td>        <td><a target="_blank" href="${c['attributes']['refobjblatt']}">${_('link') or '-'}</a></td></tr>
</%def>

