<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">


    <tr><td class="cell-left">${_('ch.bav.schienennetz.xtf_id')}</td>                                            
	<td>${c['attributes']['xtf_id'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.nom_segment')}</td>
    <td>${c['attributes']['nom_segment'] or '-'}</td></tr>    
    <tr><td class="cell-left">${_('ch.bav.schienennetz.kmdebut')}</td>
    <td>${c['attributes']['kmdebut'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.kmfin')}</td>
    <td>${c['attributes']['kmfin'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.numeroet')}</td>
    <td>${c['attributes']['numeroet'] or '-'}</td></tr>
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
    <tr><td class="cell-left">${_('ch.bav.schienennetz.debutvalidite')}</td>
    <td>${c['attributes']['debutvalidite'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.finvalidite')}</td>
    <td>${c['attributes']['finvalidite'] or '-'}</td></tr>
   
</%def>

