<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it') else 'de'
  produkt_text = 'produkt_%s' % lang
  hinweis_text = 'hinweis_%s' % lang
%>

  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.standort')}</td>
    <td class="cell-left">${c['attributes']['standort'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.adresse')}</td>
    <td class="cell-left">${c['attributes']['adresse'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.plz')}</td>
    <td class="cell-left">${c['attributes']['plz'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.ort')}</td>
    <td class="cell-left">${c['attributes']['ort'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.oeffnungszeiten')}</td>
    <td class="cell-left">${c['attributes']['oeffnungszeiten'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.produkt')}</td>
    <td class="cell-left">${c['attributes'][produkt_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.hinweis')}</td>
    <td class="cell-left">${c['attributes'][hinweis_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.kontakt')}</td>
    <td class="cell-left">${c['attributes']['kontakt'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.x_koord')}</td>
    <td class="cell-left">${c['attributes']['x'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.y_koord')}</td>
    <td class="cell-left">${c['attributes']['y'] or '-'}</td>
  </tr>
</%def>
