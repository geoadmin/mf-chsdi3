<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<%
status = '%s_%s' % ('status',c['attributes']['status'])
kategorie = '%s_%s' % ('kategorie',c['attributes']['kategorie'])
zone = '%s_%s' % ('zone',c['attributes']['zone'])
rechtsgrundlage = '%s_%s' % ('rechtsgrundlage',c['attributes']['rechtsgrundlage'])
%>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.name', lang)}</td>                 <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.objnummer', lang)}</td>            <td>${int(c['attributes']['objektnummer']) or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.status', lang)}</td>               <td>${_(status)}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.kategorie', lang)}</td>            <td>${_(kategorie)}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.rechtsgrundlage', lang)}</td>      <td>${_(rechtsgrundlage)}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.teilobjnummer', lang)}</td>        <td>${c['attributes']['teil_nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.zone', lang)}</td>                 <td>${_(zone)}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung.shape_area', lang)}</td>         <td>${round(c['attributes']['shape_area']/10000,1)}</td></tr>
</%def>
