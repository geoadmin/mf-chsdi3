<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<tr>
  <td class="cell-left">${Translator.translate('Spital', lang)}</td>
  <td>${c['attributes']['name']}</td>
</tr>
<tr>
  <td class="cell-left">${Translator.translate('gemeinde', lang)}</td>
  <td>${c['attributes']['location']}</td>
</tr>
<tr>
  <td class="cell-left">${Translator.translate('canton', lang)}</td>
  <td>${c['attributes']['canton']}</td>
</tr>
<tr>
  <td class="cell-left">${Translator.translate('arp_east', lang)}</td>
  <td>${c['attributes']['arp_east']}</td>
</tr>
<tr>
  <td class="cell-left">${Translator.translate('arp_north', lang)}</td>
  <td>${c['attributes']['arp_north']}</td>
</tr>
</%def>
