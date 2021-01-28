<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr><td class="cell-left" style="white-space:nowrap">${_('ch.bafu.mittlere-abfluesse_zukunft.place')}</td><td>${c['attributes']['place'] or '-'}</td></tr>
  <tr><td class="cell-left" style="white-space:nowrap">${_('ch.bafu.mittlere-abfluesse_zukunft.water_name')}</td><td>${c['attributes']['water_name'] or '-'}</td></tr>
  <tr><td class="cell-left" style="white-space:nowrap">${_('ch.bafu.mittlere-abfluesse_zukunft.area')}</td><td>${c['attributes']['area'] or '-'}</td></tr>
  <tr><td class="cell-left" style="white-space:nowrap">${_('ch.bafu.mittlere-abfluesse_zukunft.ezgheight')}</td><td>${c['attributes']['ezgheight'] or '-'}</td></tr>
  <tr><td class="cell-left" style="white-space:nowrap">${_('ch.bafu.mittlere-abfluesse_zukunft.glacier')}</td><td>${c['attributes']['glacier'] or '-'}</td></tr>
  <tr>
    <td class="cell-left" style="white-space:nowrap">${_('ch.bafu.mittlere-abfluesse_zukunft.url')}</td>
    <td><a href="${c['attributes']['url']}" target="_blank">${_('link')}</a></td>
  </tr>
</%def>


