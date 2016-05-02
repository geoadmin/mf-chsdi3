<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.ort')}</td>                                            
	<td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.plz')}</td>
    <td>${c['attributes']['plz'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.bundestankstellen-bebeco.strasse')}</td>
    <td>${c['attributes']['strasse'] or '-'}</td></tr>
</%def>

