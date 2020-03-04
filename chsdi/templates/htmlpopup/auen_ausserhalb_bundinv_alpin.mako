<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr', 'it') else 'de'
  biobedeutung = '%s_biobedeutung' % lang
  geobedeutung = '%s_geobedeutung' % lang
  qualitaet = '%s_qualitaet' % lang
%>
    <tr>
        <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.auen-ausserhalb_bundesinventar_alpin.name', lang)}</td>
        <td>${c['attributes']['name'] or '-'}<td>
    </tr>
    <tr>
        <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.auen-ausserhalb_bundesinventar_alpin.objnummer', lang)}</td>
        <td>${c['id']}</td>
    </tr>
    <tr>
        <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.auen-ausserhalb_bundesinventar_alpin.auentyp', lang)}</td>
        <td>${c['attributes']['auentyp'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.auen-ausserhalb_bundesinventar_alpin.biobedeutung', lang)}</td>
        <td>${c['attributes'][biobedeutung] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.auen-ausserhalb_bundesinventar_alpin.geobedeutung', lang)}</td>
        <td>${c['attributes'][geobedeutung] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.auen-ausserhalb_bundesinventar_alpin.qualitaet', lang)}</td>
        <td>${c['attributes'][qualitaet] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.auen-ausserhalb_bundesinventar_alpin.shape_area', lang)}</td>
        <td>${round(c['attributes']['shape_area'], 1) or '-'}</td>
    </tr>

</%def>

