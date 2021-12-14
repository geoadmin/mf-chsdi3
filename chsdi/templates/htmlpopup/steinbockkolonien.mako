<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

  <%
    lang = lang if lang in ('fr','it') else 'de'
    gebietstyp_text = 'gebietstyp_%s' % lang
  %>

  <tr><td class="cell-left">${_('ch.bafu.fauna-steinbockkolonien.name')}</td>     <td>${c['attributes']['name'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bafu.fauna-steinbockkolonien.objnummer')}</td>       <td>${c['attributes']['objnummer'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bafu.fauna-steinbockkolonien.kantone')}</td>         <td>${c['attributes']['kantone'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bafu.fauna-steinbockkolonien.gebietstyp')}</td>     <td>${c['attributes'][gebietstyp_text] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bafu.fauna-steinbockkolonien.gesamtflaeche')}</td>  <td>${round(c['attributes']['shape_area'] / 10000, 1) or '-'}</td></tr>

</%def>
