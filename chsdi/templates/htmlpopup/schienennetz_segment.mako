<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bav.schienennetz-kilometrierungslinien.xtf_id')}</td>
  	<td>${c['attributes']['xtf_id'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.nom_segment')}</td>
    <td>${c['attributes']['nom_segment'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.no_debut')}</td>
    <td>${c['attributes']['point_debut_nummero'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.nom_debut')}</td>
    <td>${c['attributes']['point_debut_nom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.no_fin')}</td>
    <td>${c['attributes']['point_fin_nummero'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.nom_fin')}</td>
    <td>${c['attributes']['point_fin_nom'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz-kilometrierungslinien.numero')}</td>
    <td>${c['attributes']['kmnummero'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz-kilometrierungslinien.nom')}</td>
    <td>${c['attributes']['kmtext'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.kmdebut')}</td>
    <td>${c['attributes']['kmdebut'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.kmfin')}</td>
    <td>${c['attributes']['kmfin'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.abreviationet')}</td>
    <td>${c['attributes']['abreviationet'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.nombrevoies')}</td>
    <td>${c['attributes']['nombrevoies'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.ecartement')}</td>
    <td>${c['attributes']['ecartement'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.electrification')}</td>
% if lang == 'de' or lang == "rm"  or lang == "en":
    <td>${c['attributes']['electrification_de'] or '-'}</td></tr>
% else :
    <td>${c['attributes']['electrification_fr'] or '-'}</td></tr>
% endif
</%def>

