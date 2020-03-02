<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
  <% c['stable_id'] = True %>
	<tr><td class="cell-left">${Translator.translate('tilenumber', lang)}</td><td>${c['featureId']}</td></tr>
  <tr><td class="cell-left">${Translator.translate('sheetname', lang)}</td><td>${c['attributes']['lk25_name']}</td></tr>
  <tr><td class="cell-left">${Translator.translate('Datenstand', lang)}</td><td>${c['attributes']['datenstand'] or '-'}</td></tr>
	<tr><td class="cell-left">${Translator.translate('Datenbezug')}</td><td><a href="http://www.toposhop.admin.ch/de/shop/products/images/ortho/swissimage/index" target="_blank">${_('Toposhop', lang)}</a></td></tr>
</%def> 
