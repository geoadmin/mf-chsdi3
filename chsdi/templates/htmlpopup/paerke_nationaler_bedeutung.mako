<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<%
status = '%s_%s' % ('status',c['attributes']['status'])
kategorie = '%s_%s' % ('kategorie',c['attributes']['kategorie'])
zone = '%s_%s' % ('zone',c['attributes']['zone'])
rechtsgrundlage = '%s_%s' % ('rechtsgrundlage',c['attributes']['rechtsgrundlage'])
%>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.name')}</td>                 <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.objnummer')}</td>            <td>${int(c['attributes']['objektnummer']) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.status')}</td>               <td>${_(status)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.kategorie')}</td>            <td>${_(kategorie)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.rechtsgrundlage')}</td>      <td>${_(rechtsgrundlage)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.teilobjnummer')}</td>        <td>${c['attributes']['teil_nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.zone')}</td>                 <td>${_(zone)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.shape_area')}</td>         <td>${round(c['attributes']['shape_area']/10000,1) or '-'}</td></tr>
</%def>
