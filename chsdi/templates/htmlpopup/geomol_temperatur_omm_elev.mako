<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-geomol-temperatur_top_omm.elev', lang)}</td>    	<td>${c['attributes']['elev'] or '-'}</td></tr>
</%def>

