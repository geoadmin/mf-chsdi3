<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_flussgebiete.name')}</td>
    <td>${c['attributes']['flussgb'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('flaeche_km2')}</td>
    <td>${c['attributes']['flaeche'] or '-'}</td>
  </tr>
</%def>
