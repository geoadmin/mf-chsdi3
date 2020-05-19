<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it') else 'de'
  lang = lang if lang != 'it' else 'fr'
  es = '%s_es' % lang
  pointofdetermination_t = '%s_pointofdetermination_t' % lang
%>

<% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht.lr_max_night')}</td> <td>${int(round(c['attributes']['lr_max_night'], 1)) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht.de_es')}</td><td>${c['attributes'][es] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht.floor')}</td><td>${c['attributes']['floor'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht.de_pointofdetermination_t')}</td><td>${c['attributes'][pointofdetermination_t] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht.lr_max_year')}</td> <td>${c['attributes']['lr_max_year']}</td></tr>
</%def>
