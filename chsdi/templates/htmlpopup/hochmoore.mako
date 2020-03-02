<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    unit = 'unit_%s' % lang
    type = 'hochmoore_type_%s' % lang
%>

    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-hochmoore.objnummer', lang)}</td>           <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-hochmoore.name', lang)}</td>         <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-hochmoore.hochmoore_type', lang)}</td>                <td>${c['attributes'][type] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-hochmoore.unit', lang)}</td>     <td>${c['attributes'][unit] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-hochmoore.shape_area', lang)}</td>         <td>${round(c['attributes']['shape_area']/10000, 1) or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.bundesinventare-hochmoore.refobjblat', lang)}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

