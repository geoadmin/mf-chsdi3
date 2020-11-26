<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  if lang in ('de', 'rm', 'en'):
    lang_text = 'de'
  else:
    lang_text = 'fr'
  bezeichnung_text = 'bezeichnung_%s' % lang_text
%>

<table>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.id')}</td>
    <td class="cell-meta">${c['attributes']['nummer_text'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.bezeichnung')}</td>
    <td class="cell-meta">${c['attributes'][bezeichnung_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.betrieblichebezeichnung')}</td>
    <td class="cell-meta">${c['attributes']['betrieblichebezeichnung'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.laenge')}</td>
    <td class="cell-meta">${c['attributes']['laenge'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.kantenhoehe')}</td>
    <td class="cell-meta">${c['attributes']['kantenhoehe'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.haltestelle')}</td>
    <td class="cell-meta">${c['attributes']['haltestelle'] or '-'}</td>
  </tr>
</table>

</%def>

