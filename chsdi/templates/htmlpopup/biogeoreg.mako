<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr','it','en') else 'de'
    regionname_text = 'regionname_%s' % lang
    unterregionname_text = 'unterregionname_%s' % lang
  %>
  <tr><td class="cell-left">${_('objnummer')}</td><td>${c['attributes']['objnummer'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('regionname')}</td><td>${c['attributes'][regionname_text] or '-'}</td></tr>
  <tr><td class="cell-left">${_('unterregionname')}</td><td>${c['attributes'][unterregionname_text] or '-'}</td></tr>
  <tr><td class="cell-left">${_('area')}</td><td>${c['attributes']['area'] or '-'}</td></tr>
</%def>

