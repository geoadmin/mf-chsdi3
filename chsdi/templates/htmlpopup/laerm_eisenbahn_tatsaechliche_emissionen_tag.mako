<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    enmodelrailway = 'enmodelrailway_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.kml_number')}</td>                   <td>${c['attributes']['kml_number'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.km_from')}</td>                      <td>${c['attributes']['km_from'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.km_to')}</td>                        <td>${c['attributes']['km_to'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.lre_day')}</td>                      <td>${c['attributes']['lre_day'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.enmodel_railway')}</td>              <td>${c['attributes'][enmodelrailway] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.level_correction_day')}</td>         <td>${c['attributes']['level_correction_day'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.train_number_day')}</td>             <td>${c['attributes']['train_number_day'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.train_number_freight_d')}</td>       <td>${c['attributes']['train_number_freight_d'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.lre_remark')}</td>                   <td>${c['attributes']['lre_remark'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag.year_evaluation')}</td>              <td>${c['attributes']['year_evaluation'] or '-'}</td></tr>
</%def>
