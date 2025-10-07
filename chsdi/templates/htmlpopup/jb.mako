<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
        typ_text = 'typ_%s' %lang
        layer = c['layerBodId']
    %>
  <tr><td class="cell-left">${_(layer + '.objektnummer')}</td><td>${c['attributes']['objektnummer'] or '-'}</td></tr>
  <tr><td class="cell-left">${_(layer + '.gebietsname')}</td><td>${c['attributes']['gebietsname'] or '-'}</td></tr>
  <tr><td class="cell-left">${_(layer + '.typ')}</td><td>${c['attributes'][typ_text] or '-'}</td></tr>
  <tr><td class="cell-left">${_(layer + '.jb_fl')}</td><td>${c['attributes']['flaeche_ha'] or '-'}</td></tr>
  <tr>
    <td class="cell-left">${_(layer + '.refobjblatt' )}</td>
    <td>
      <a href="${c['attributes']['refobjblatt'] or '-'.strip()}" target="_blank">Link</a>
    </td>
  </tr>
</%def>
