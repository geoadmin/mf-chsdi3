<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    de_nebenarm = '%s_nebenarm' % lang
%>
    <tr><td class="cell-left">${_('ch.bafu.wasser-gebietsauslaesse.id')}</td><td>${c['attributes']['id_2'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-gebietsauslaesse.ezgnr')}</td><td>${c['attributes']['ezgnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-gebietsauslaesse.gewaessername')}</td><td>${c['attributes']['gewaessername'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-gebietsauslaesse.gwlnr')}</td><td>${c['attributes']['gwlnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-gebietsauslaesse.adresse')}</td><td>${c['attributes']['adresse'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wasser-gebietsauslaesse.de_nebenarm')}</td><td>${c['attributes'][de_nebenarm] or '-'}</td></tr>
</%def>

