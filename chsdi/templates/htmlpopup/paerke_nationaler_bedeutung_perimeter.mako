<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<% 
c['stable_id'] = True 
status = '%s_%s' % ('status',c['attributes']['status'])
kategorie = '%s_%s' % ('kategorie',c['attributes']['kategorie'])
rechtsgrundlage = '%s_%s' % ('rechtsgrundlage',c['attributes']['rechtsgrundlage'])
%>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.name', lang)}</td>                 <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.objnummer', lang)}</td>            <td>${c['featureId'] or '-'}</td>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.status', lang)}</td>               <td>${t.Translator.translate(status, lang)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.kategorie', lang)}</td>            <td>${t.Translator.translate(kategorie, lang)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.rechtsgrundlage', lang)}</td>      <td>${t.Translator.translate(rechtsgrundlage, lang)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter.shape_area', lang)}</td>         <td>${round(c['attributes']['shape_area']/10000,1)}</td></tr>
</%def>
