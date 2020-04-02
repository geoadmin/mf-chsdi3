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
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag.lr_day')}</td> <td>${c['attributes']['lr_day']}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag.de_es')}</td><td>${c['attributes'][es] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag.floor')}</td><td>${c['attributes']['floor'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag.de_pointofdetermination')}</td><td>${c['attributes'][pointofdetermination] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag.de_operation_status')}</td><td>${c['attributes'][operation_status] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag.receptor')}</td> <td>${c['attributes']['receptor']}</td></tr>
</%def>

