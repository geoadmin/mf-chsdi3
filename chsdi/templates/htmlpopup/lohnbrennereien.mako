<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<%
homepage = c['attributes']['homepage'] or None
%>
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.name')}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.adresse')}</td>        <td>${c['attributes']['adresse'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.ort')}</td>            <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.kanton')}</td>         <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.telefon')}</td>        <td>${c['attributes']['telefon'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.mobile')}</td>        <td>${c['attributes']['mobile'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.email')}</td>          <td>${c['attributes']['email'] or '-'}</td></tr>
% if homepage:
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.homepage')}</td>       <td><a href="http://${homepage}" target="_blank">Link</a></td></tr>
% else:
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.homepage')}</td>       <td>-</td></tr>
% endif
    <tr><td class="cell-left">${_('ch.ezv.lohnbrennereien.bemerkung')}</td>      <td>${c['attributes']['bemerkung'] or '-'}</td></tr>
</%def>

