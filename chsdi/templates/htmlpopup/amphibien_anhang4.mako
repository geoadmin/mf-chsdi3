<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.bundesinventare-amphibien_anhang4.objnummer', lang)}</td>          <td>${c['attributes']['obnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.bundesinventare-amphibien_anhang4.name', lang)}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.bundesinventare-amphibien_anhang4.refobjblat', lang)}</td>        <td><a target ="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

