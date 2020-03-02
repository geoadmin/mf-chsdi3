<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2.objnummer', lang)}</td>          <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2.name', lang)}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2.teilobjnummer', lang)}</td>          <td>${c['attributes']['teilobjnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2.shape_area', lang)}</td>          <td>${round(c['attributes']['shape_area']/10000,1) or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2.refobjblat', lang)}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

