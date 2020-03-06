<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
	  <tr><td class="cell-left">${h.translate('tilenumber', lang)}</td><td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${h.translate('sheetname', lang)}</td><td>${c['attributes']['lk_name']}</td></tr>
    <tr><td class="cell-left">${h.translate('Datenstand', lang)}</td><td>${c['attributes']['release'] or '-'}</td></tr>
	  <tr><td class="cell-left">${h.translate('Datenbezug', lang)}</td><td><a href="http://www.toposhop.admin.ch/shop/products/maps/national/digital/pixelWizardEntryPoint?wizardMap=Pixel500" target="_blank">${h.translate('Toposhop', lang)}</a></td></tr>
</%def>

