<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    nebenarm = '%s_nebenarm' % lang
%>

    <tr><td class="cell-left">${_('ch.bafu.wasser-vorfluter.id')}</td><td>${c['attributes']['id_2'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-vorfluter.ezgnr')}</td><td>${c['attributes']['ezgnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-vorfluter.gwlnr')}</td><td>${c['attributes']['gwlnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-vorfluter.unteresende')}</td><td>${c['attributes']['unteresende'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-vorfluter.oberesende')}</td><td>${c['attributes']['oberesende'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-vorfluter.gewaessername')}</td><td>${c['attributes']['gewaessername'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-vorfluter.nebenarm')}</td><td>${c['attributes'][nebenarm] or '-'}</td></tr>
</%def>


