<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr','it') else 'de'
    sanierungastra_text = 'sanierungastra_%s' %lang
  %>
  <tr>
    <td class="cell-left">${_('ch.bafu.fauna-wildtierpassagen.name')}</td>    
    <td>${c['attributes']['name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.fauna-wildtierpassagen.verkehrsinfrastrukturtyp')}</td>
    <td>${c['attributes']['verkehrsinfrastrukturtyp'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.fauna-wildtierpassagen.sanierungastra')}</td>
    <td>${c['attributes'][sanierungastra_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.fauna-wildtierpassagen.realisierungsjahr')}</td>
    <td>${c['attributes']['realisierungsjahr'] or '-'}</td>
  </tr>
</%def>
