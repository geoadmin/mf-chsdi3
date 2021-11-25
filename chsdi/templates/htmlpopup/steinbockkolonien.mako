<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

  <%
    lang = lang if lang in ('fr','it') else 'de'
    gebietstyp_text = 'gebietstyp_%s' % lang
  %>

  <tr><td class="cell-left">${_('objektname')}</td>     <td>${c['attributes']['name'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('objektnr')}</td>       <td>${c['attributes']['objnummer'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('kanton')}</td>         <td>${c['attributes']['kantone'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('gebietstyp')}</td>     <td>${c['attributes'][gebietstyp_text] or '-'}</td></tr>
  <tr><td class="cell-left">${_('gesamtflaeche')}</td>  <td>${c['attributes']['shape_area'] / 10000 or '-'}</td></tr>

</%def>
