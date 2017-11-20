<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<%
  lang = lang if lang in ('fr', 'it' ) else 'de'
  site = 'site_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien.objnummer')}</td>          <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien.name')}</td>              <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien.site')}</td>           <td>${c['attributes'][site] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien.shape_area')}</td>        <td>${round(c['attributes']['shape_area']/10000,1 ) or '-'} ha</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien.refobjblat')}</td>  <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>

</%def>

