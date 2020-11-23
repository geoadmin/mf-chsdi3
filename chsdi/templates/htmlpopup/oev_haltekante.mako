<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    if lang in ('de', 'rm', 'en'):
      lang = 'de'
    else:
      lang = 'fr'
    bezeichnung_text = 'bezeichnung_%s' % lang
%>

<table>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.nummer')}</td>
    <td class="cell-meta">${c['attributes']['nummer'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.bezeichnung')}</td>
    <td class="cell-meta">${c['attributes'][bezeichung_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.betrieblichebezeichnung')}</td>
    <td class="cell-meta">${c['attributes']['betrieblichebezeichung'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.laenge')}</td>
    <td class="cell-meta">${c['attributes']['laenge'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.kantenhoehe')}</td>
    <td class="cell-meta">${c['attributes']['kantenhoehe] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.haltestelle')}</td>
    <td class="cell-meta">${c['attributes']['haltestelle'] or '-'}</td>
  </tr>
</table>

</%def>

