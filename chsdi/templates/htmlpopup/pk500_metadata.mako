<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
	  <tr><td class="cell-left">${mod_translate.Translator.translate('tilenumber', lang)}</td><td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('sheetname', lang)}</td><td>${c['attributes']['lk_name']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('Datenstand', lang)}</td><td>${c['attributes']['release'] or '-'}</td></tr>
	  <tr><td class="cell-left">${mod_translate.Translator.translate('Datenbezug', lang)}</td><td><a href="http://www.toposhop.admin.ch/shop/products/maps/national/digital/pixelWizardEntryPoint?wizardMap=Pixel500" target="_blank">${mod_translate.Translator.translate('Toposhop', lang)}</a></td></tr>
</%def>

