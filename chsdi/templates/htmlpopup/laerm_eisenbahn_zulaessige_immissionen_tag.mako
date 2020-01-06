<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it') else 'de'
  lang = lang if lang != 'it' else 'fr'
  es = '%s_es' % lang
  pointofdetermination_t = '%s_pointofdetermination_t' % lang
%>

<% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag.lr_max_day')}</td> <td>${c['attributes']['lr_max_day']}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag.de_es')}</td><td>${c['attributes'][es] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag.floor')}</td><td>${c['attributes']['floor'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag.de_pointofdetermination_t')}</td><td>${c['attributes'][pointofdetermination_t] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag.lr_max_year')}</td> <td>${c['attributes']['lr_max_year']}</td></tr>
</%def>
