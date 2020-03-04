<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
%>

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte.stationnam', lang)}</td>        <td>${c['attributes']['stationnam'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('coordinate_x', lang)}</td>                                                             <td>${c['attributes']['coordhor'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('coordinate_y', lang)}</td>                                                             <td>${c['attributes']['coordver'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte.altitude', lang)}</td>          <td>${c['attributes']['altitude'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('bouguer_anomalie', lang)}</td>                                                         <td>${c['attributes']['bouguerano'] or '-'}</td></tr>
</%def>
