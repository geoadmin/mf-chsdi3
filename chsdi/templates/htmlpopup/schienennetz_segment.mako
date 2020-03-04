<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.xtf_id_tooltip', lang)}</td>
  	<td>${c['attributes']['xtf_id_tooltip'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.nom_segment', lang)}</td>
    <td>${c['attributes']['nom_segment'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.no_debut', lang)}</td>
    <td>${c['attributes']['point_debut_nummero'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.nom_debut', lang)}</td>
    <td>${c['attributes']['point_debut_nom'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.no_fin', lang)}</td>
    <td>${c['attributes']['point_fin_nummero'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.nom_fin', lang)}</td>
    <td>${c['attributes']['point_fin_nom'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.kmnumero', lang)}</td>
    <td>${c['attributes']['kmnummero'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.kmtext', lang)}</td>
    <td>${c['attributes']['kmtext'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.kmdebut', lang)}</td>
    <td>${c['attributes']['kmdebut'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.kmfin', lang)}</td>
    <td>${c['attributes']['kmfin'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.abreviationet', lang)}</td>
    <td>${c['attributes']['abreviationet'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.nombrevoies', lang)}</td>
    <td>${c['attributes']['nombrevoies'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.ecartement', lang)}</td>
    <td>${c['attributes']['ecartement'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bav.schienennetz.electrification', lang)}</td>
% if lang == 'de' or lang == "rm"  or lang == "en":
    <td>${c['attributes']['electrification_de'] or '-'}</td></tr>
% else :
    <td>${c['attributes']['electrification_fr'] or '-'}</td></tr>
% endif
</%def>

