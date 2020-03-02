<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
	<tr><td class="cell-left">${Translator.translate('geocover_basisdatensatz', lang)}</td><td>${c['attributes']['basisdatensatz'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('geocover_description', lang)}</td><td>${c['attributes']['description'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('geocover_spec_description', lang)}</td><td>${c['attributes']['spec_description'] or '-'}</td></tr>
    <tr><td class="cell-left"></td><td><a href="${c['attributes']['url_legend']}" target="_blank">${Translator.translate('linkzurlegende', lang)}</a></td></tr>
</%def>
