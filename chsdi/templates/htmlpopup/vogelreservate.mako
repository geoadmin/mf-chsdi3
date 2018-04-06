<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it') else 'de'
    schutzkat = 'schutzkategorie_%s' % lang
    schutzeb = 'schutzebene_%s' % lang
%>

    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.name')}</td>         <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.objnummer')}</td>          <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.teilgebiet')}</td>         <td>${c['attributes']['teilgebiet'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.schutzkategorie')}</td>         <td>${c['attributes'][schutzkat] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.schutzebene')}</td>         <td>${c['attributes'][schutzeb] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.shape_area')}</td>          <td>${round(c['attributes']['shape_area']/10000) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.obj_gisflaeche')}</td>         <td>${round(c['attributes']['obj_gisflaeche']) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-vogelreservate.refobjblatt')}</td>        <td><a target="_blank" href="${c['attributes']['refobjblatt']}">${_('link') or '-'}</a></td></tr>
</%def>

