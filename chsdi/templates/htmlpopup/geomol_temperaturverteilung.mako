<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-geomol-temperaturverteilung_500.pixel_value', lang)}</td>    	<td>${int(round(c['attributes']['pixel_value'])) or '-'}</td></tr>
</%def>

