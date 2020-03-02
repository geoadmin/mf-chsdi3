<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    enmodelrailway = 'enmodelrailway_%s' % lang
%>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.kml_number', lang)}</td>                   <td>${c['attributes']['kml_number'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.km_from', lang)}</td>                      <td>${c['attributes']['km_from'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.km_to', lang)}</td>                        <td>${c['attributes']['km_to'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.lre_day', lang)}</td>                      <td>${c['attributes']['lre_day'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.enmodel_railway', lang)}</td>              <td>${c['attributes'][enmodelrailway] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.level_correction_day', lang)}</td>         <td>${c['attributes']['level_correction_day'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.train_number_day', lang)}</td>             <td>${c['attributes']['train_number_day'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.train_number_freight_d', lang)}</td>       <td>${c['attributes']['train_number_freight_d'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.lre_remark', lang)}</td>                   <td>${c['attributes']['lre_remark'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.year_evaluation', lang)}</td>              <td>${c['attributes']['year_evaluation'] or '-'}</td></tr>
</%def>
