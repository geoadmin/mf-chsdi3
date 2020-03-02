<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${t.Translator.translate('ch.vbs.patrouilledesglaciers-z_rennen.name', lang)}</td>
	<td>${c['attributes']['name'] or '-'}</td></tr>

</%def>

