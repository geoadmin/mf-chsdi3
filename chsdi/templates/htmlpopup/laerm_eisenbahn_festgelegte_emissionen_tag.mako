<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.kml_number', lang)}</td>                   <td>${c['attributes']['kml_number'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.km_from', lang)}</td>                      <td>${c['attributes']['km_from'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.km_to', lang)}</td>                        <td>${c['attributes']['km_to'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.lre_max_day', lang)}</td>                  <td>${c['attributes']['lre_max_day'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.lre_max_remark', lang)}</td>               <td>${c['attributes']['lre_max_remark'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.lre_max_date', lang)}</td>                 <td>${c['attributes']['lre_max_date'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.lre_max_year', lang)}</td>                 <td>${c['attributes']['lre_max_year'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag.lre_remark', lang)}</td>                   <td>${c['attributes']['lre_remark'] or '-'}</td></tr>
</%def>
