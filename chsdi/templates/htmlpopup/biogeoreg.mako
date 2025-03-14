<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr','it') else 'de'
    regionname_text = 'regionname_%s' % lang
    unterregionname_text = 'unterregionname_%s' % lang
  %>
  <tr><td class="cell-left">${_('ch.bafu.biogeographische_regionen.objnummer')}</td><td>${c['attributes']['objnummer'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bafu.biogeographische_regionen.regionname')}</td><td>${c['attributes'][regionname_text] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bafu.biogeographische_regionen.unterregionname')}</td><td>${c['attributes'][unterregionname_text] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bafu.biogeographische_regionen.area')}</td><td>${c['attributes']['area'] or '-'}</td></tr>
</%def>

