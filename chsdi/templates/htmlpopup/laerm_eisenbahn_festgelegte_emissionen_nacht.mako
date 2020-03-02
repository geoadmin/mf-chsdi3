<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.kml_number', lang)}</td>                   <td>${c['attributes']['kml_number'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.km_from', lang)}</td>                      <td>${c['attributes']['km_from'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.km_to', lang)}</td>                        <td>${c['attributes']['km_to'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.lre_max_night', lang)}</td>                <td>${c['attributes']['lre_max_night'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.lre_max_remark', lang)}</td>               <td>${c['attributes']['lre_max_remark'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.lre_max_date', lang)}</td>                 <td>${c['attributes']['lre_max_date'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.lre_max_year', lang)}</td>                 <td>${c['attributes']['lre_max_year'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht.lre_remark', lang)}</td>                   <td>${c['attributes']['lre_remark'] or '-'}</td></tr>
</%def>
