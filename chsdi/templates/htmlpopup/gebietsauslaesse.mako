<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    de_nebenarm = '%s_nebenarm' % lang
%>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-gebietsauslaesse.id', lang)}</td><td>${c['attributes']['id_2'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-gebietsauslaesse.ezgnr', lang)}</td><td>${c['attributes']['ezgnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-gebietsauslaesse.gewaessername', lang)}</td><td>${c['attributes']['gewaessername'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-gebietsauslaesse.gwlnr', lang)}</td><td>${c['attributes']['gwlnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-gebietsauslaesse.adresse', lang)}</td><td>${c['attributes']['adresse'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wasser-gebietsauslaesse.de_nebenarm', lang)}</td><td>${c['attributes'][de_nebenarm] or '-'}</td></tr>
</%def>
