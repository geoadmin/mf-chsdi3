<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<% 
c['stable_id'] = True 
status = '%s_%s' % ('status',c['attributes']['status'])
kategorie = '%s_%s' % ('kategorie',c['attributes']['kategorie'])
rechtsgrundlage = '%s_%s' % ('rechtsgrundlage',c['attributes']['rechtsgrundlage'])
%>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.name')}</td>                 <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.objnummer')}</td>            <td>${c['featureId'] or '-'}</td>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.status')}</td>               <td>${_(status)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.kategorie')}</td>            <td>${_(kategorie)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.rechtsgrundlage')}</td>      <td>${_(rechtsgrundlage)}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.shape_area')}</td>         <td>${round(c['attributes']['shape_area']/10000,1) or '-'}</td></tr>
</%def>
