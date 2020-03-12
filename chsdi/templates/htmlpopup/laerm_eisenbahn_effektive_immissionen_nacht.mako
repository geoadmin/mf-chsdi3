<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it') else 'de'
  lang = lang if lang != 'it' else 'fr'
  es = '%s_es' % lang
  pointofdetermination = '%s_pointofdetermination' % lang
  operation_status = '%s_operation_status' % lang
%>

<% c['stable_id'] = False %>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht.lr_night', lang)}</td> <td>${c['attributes']['lr_night']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht.de_es', lang)}</td><td>${c['attributes'][es] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht.floor', lang)}</td><td>${c['attributes']['floor'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht.de_pointofdetermination', lang)}</td><td>${c['attributes'][pointofdetermination] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht.de_operation_status', lang)}</td><td>${c['attributes'][operation_status] or '-'}</td></tr>
</%def>

