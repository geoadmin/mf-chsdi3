<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    enmodelrailway = 'enmodelrailway_%s' % lang
%>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.kml_number', lang)}</td>                     <td>${c['attributes']['kml_number'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.km_from', lang)}</td>                        <td>${c['attributes']['km_from'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.km_to', lang)}</td>                          <td>${c['attributes']['km_to'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.lre_night', lang)}</td>                      <td>${c['attributes']['lre_night'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.enmodel_railway', lang)}</td>                <td>${c['attributes'][enmodelrailway] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.level_correction_night', lang)}</td>         <td>${c['attributes']['level_correction_night'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.train_number_night', lang)}</td>             <td>${c['attributes']['train_number_night'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.train_number_freight_n', lang)}</td>         <td>${c['attributes']['train_number_freight_n'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.lre_remark', lang)}</td>                     <td>${c['attributes']['lre_remark'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht.year_evaluation', lang)}</td>                <td>${c['attributes']['year_evaluation'] or '-'}</td></tr>
</%def>
