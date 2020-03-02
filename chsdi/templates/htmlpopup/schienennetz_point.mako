<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.schienennetz.xtf_id', lang)}</td>
	  <td>${c['attributes']['xtf_id_tooltip'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.schienennetz.numero', lang)}</td>
    <td>${c['attributes']['numero'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.schienennetz.nom_point', lang)}</td>
    <td>${c['attributes']['nom_point'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bav.schienennetz.abreviation', lang)}</td>
    <td>${c['attributes']['abreviation'] or '-'}</td></tr>
</%def>

