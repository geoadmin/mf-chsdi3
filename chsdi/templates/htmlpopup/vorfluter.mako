<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    nebenarm = '%s_nebenarm' % lang
%>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-vorfluter.id'), lang}</td><td>${c['attributes']['id_2'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-vorfluter.ezgnr'), lang}</td><td>${c['attributes']['ezgnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-vorfluter.gewaessername'), lang}</td><td>${c['attributes']['gewaessername'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-vorfluter.gwlnr'), lang}</td><td>${c['attributes']['gwlnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-vorfluter.unteresende'), lang}</td><td>${c['attributes']['unteresende'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-vorfluter.oberesende'), lang}</td><td>${c['attributes']['oberesende'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-vorfluter.nebenarm'), lang}</td><td>${c['attributes'][nebenarm] or '-'}</td></tr>
</%def>


