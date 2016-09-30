<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<tr>
  <td class="cell-left">${_('Spital')}</td>
  <td>${c['attributes']['name']}</td>
</tr>
<tr>
  <td class="cell-left">${_('gemeinde')}</td>
  <td>${c['attributes']['location']}</td>
</tr>
<tr>
  <td class="cell-left">${_('canton')}</td>
  <td>${c['attributes']['canton']}</td>
</tr>
<tr>
  <td class="cell-left">${_('arp_east')}</td>
  <td>${c['attributes']['arp_east']}</td>
</tr>
<tr>
  <td class="cell-left">${_('arp_north')}</td>
  <td>${c['attributes']['arp_north']}</td>
</tr>
</%def>
