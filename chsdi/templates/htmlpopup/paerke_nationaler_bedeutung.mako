<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<%
status = '%s_%s' % ('status',c['attributes']['status'])
kategorie = '%s_%s' % ('kategorie',c['attributes']['kategorie'])
zone = '%s_%s' % ('zone',c['attributes']['zone'])
rechtsgrundlage = '%s_%s' % ('rechtsgrundlage',c['attributes']['rechtsgrundlage'])
%>
    <tr><td class="cell-left">${_('name')}</td>                 <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('objnummer')}</td>            <td>${int(c['attributes']['objektnummer']) or '-'}</td></tr>
    <tr><td class="cell-left">${_('status')}</td>               <td>${_(status)}</td></tr>
    <tr><td class="cell-left">${_('kategorie')}</td>            <td>${_(kategorie)}</td></tr>
    <tr><td class="cell-left">${_('rechtsgrundlage')}</td>      <td>${_(rechtsgrundlage)}</td></tr>
    <tr><td class="cell-left">${_('teilobjnummer')}</td>        <td>${c['attributes']['teil_nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('zone')}</td>                 <td>${_(zone)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-moorlandschaften.shape_area')}</td>         <td>${round(c['attributes']['shape_area']/10000,1) or '-'}</td></tr>
</%def>
