<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    lang_significance = lang if lang in ('fr','it') else 'de'
    significance = '%s_bedeutung' % lang_significance
    lang_quality = 'fr' if lang in ('fr','it') else 'de'
    quality = '%s_qualitaet' % lang_quality
    %>

    <tr>
        <td class="cell-left">${t.translate('ch.bafu.auen-ausserhalb_bundesinventar.name', lang)}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bafu.auen-ausserhalb_bundesinventar.objnummer', lang)}</td>
        <td>${c['id']}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bafu.auen-ausserhalb_bundesinventar.code_qualitaet', lang)}</td>
        <td>${c['attributes'][quality] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bafu.auen-ausserhalb_bundesinventar.code_bedeutung', lang)}</td>
        <td>${c['attributes'][significance] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bafu.auen-ausserhalb_bundesinventar.shape_area', lang)}</td>
        <td>${round(c['attributes']['shape_area'], 1) or '-'}</td>
    </tr>

</%def>

