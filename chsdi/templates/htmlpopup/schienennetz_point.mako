<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${_('ch.bav.schienennetz.xtf_id')}</td>                                            
	<td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.numero')}</td>
    <td>${c['attributes']['numero'] or '-'}</td></tr>    
    <tr><td class="cell-left">${_('ch.bav.schienennetz.nom_point')}</td>
    <td>${c['attributes']['nom_point'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.abreviation')}</td>
    <td>${c['attributes']['abreviation'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.respdonneesabreviation')}</td>
    <td>${c['attributes']['respdonneesabreviation'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.debutvalidite')}</td>
    <td>${c['attributes']['debutvalidite'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.schienennetz.finvalidite')}</td>
    <td>${c['attributes']['finvalidite'] or '-'}</td></tr>
   
</%def>

