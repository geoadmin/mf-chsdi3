<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    typ = 'typ2_%s' % lang
    typ_supp = 'typ2_fr' if lang == 'it' else 'typ2_%s' % lang
    typ_supp = 'typ2_de' if lang == 'rm' else typ_supp 
    fluss = 'flussgb_%s' % lang
    fluss_supp = 'flussgb_fr' if lang == 'it' else 'flussgb_%s' % lang
    fluss_supp = 'flussgb_de' if lang == 'rm' else fluss_supp
%>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.wasser-teileinzugsgebiete_2.id', lang)}</td>
      <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.wasser-teileinzugsgebiete_2.gwlnr', lang)}</td>
      <td>${c['attributes']['gwlnr'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_measure_2', lang)}</td>
      <td>${c['attributes']['measure'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('teilezgfla', lang)}</td>
      <td>${c['attributes']['teilezgfla'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_ezgflaeche', lang)}</td>
      <td>${c['attributes']['ezgflaeche'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('typ', lang)}</td>
      <td>${c['attributes'][typ] or c['attributes'][typ_supp] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('tt_flussgb', lang)}</td>
      <td>${c['attributes'][fluss] or c['attributes'][fluss_supp] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
<%
  from urllib2 import urlopen
  dataGeoAdminHost = request.registry.settings['datageoadminhost']
  
  img_url = "https://" + dataGeoAdminHost + "/ch.bafu.wasser-teileinzugsgebiete_2/image/" + str(c['featureId']) + ".png"
  zip_url = "https://" + dataGeoAdminHost + "/ch.bafu.wasser-teileinzugsgebiete_2/downloads/" + str(100000+c['featureId']) + ".zip"
  image = None
  zip = None
  image_exist = h.resource_exists(img_url)
  zip_exist = h.resource_exists(zip_url)

  id = c['featureId']
  
%>
<div>
    <table class="table-with-border">
      <tr><th class="cell-left" colspan="2">${t.Translator.translate('tt_teileinzugsgebiete_2.ebene2km_teil1', lang)}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.namen_gewaesser', lang)}</th>          <td>${c['attributes']['ext_gewiss_nr_namen_gewaesser'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('ch.bafu.wasser-teileinzugsgebiete_2.gwlnr', lang)}</th>                                  <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.xy_gebietsauslass', lang)}</th>              <td>${c['attributes']['ext_ezg_xy_gebietsauslass'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.gebietsauslaesse_gemeindename', lang)}</th>      <td>${c['attributes']['ext_gebietsauslaesse_gemeindename'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.gewissnr', lang)}</th>                       <td>${c['attributes']['ext_ezg_gewissnr'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('ch.bafu.wasser-teileinzugsgebiete_2.ext_ezg_flussgb', lang)}</th>                        <td>${c['attributes']['ext_ezg_flussgb'] or '-'}</td></tr>
    % if c['attributes']['ext_physiogeographie_gesamtflaeche']:
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${t.Translator.translate('tt_teileinzugsgebiete_2.ebene2km_teil2', lang)}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.physiogeographie_gesamtflaeche', lang)}</th>     <td>${round(c['attributes']['ext_physiogeographie_gesamtflaeche'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.physiogeographie_anteil_ch', lang)}</th>         <td>${round(c['attributes']['ext_physiogeographie_anteil_ch'],1) or '-'}</td></tr>
    % endif
    % if c['attributes']['ext_landnutzung_ant_bestockt']:
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${t.Translator.translate('tt_teileinzugsgebiete_2.ebene2km_teil3', lang)}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.landnutzung_ant_bestockt', lang)}</th>           <td>${round(c['attributes']['ext_landnutzung_ant_bestockt'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.landnutzung_ant_landwirtschaft', lang)}</th>     <td>${round(c['attributes']['ext_landnutzung_ant_landwirtschaft'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.landnutzung_ant_unprod_sonst', lang)}</th>       <td>${round(c['attributes']['ext_landnutzung_ant_unprod_sonst'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.landnutzung_ant_gewaesser', lang)}</th>          <td>${round(c['attributes']['ext_landnutzung_ant_gewaesser'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.landnutzung_ant_gletscher_firn', lang)}</th>     <td>${round(c['attributes']['ext_landnutzung_ant_gletscher_firn'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.landnutzung_ant_siedlung', lang)}</th>           <td>${round(c['attributes']['ext_landnutzung_ant_siedlung'],1) or '-'}</td></tr>
    % endif
    % if c['attributes']['ext_physiogeographie_ch_min_z']:
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${t.Translator.translate('tt_teileinzugsgebiete_2.ebene2km_teil4', lang)}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.physiogeographie_ch_min_z', lang)}</th>          <td>${int(c['attributes']['ext_physiogeographie_ch_min_z']) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.physiogeographie_ch_max_z', lang)}</th>          <td>${int(c['attributes']['ext_physiogeographie_ch_max_z']) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.physiogeographie_ch_mean_z', lang)}</th>         <td>${int(c['attributes']['ext_physiogeographie_ch_mean_z']) or '-'}</td></tr>
    % endif
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${_('tt_teileinzugsgebiete_2.ebene2km_teil5')|n}</th></tr>

    % if c['attributes']['ext_ezg_datenausgabe'] == 0:
      <tr><th class="cell-left" colspan="2" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.noinfoforthisobject')|n}</th></tr>
    % elif c['attributes']['ext_ezg_datenausgabe'] == 2:
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_jahr', lang)}</th>                 <td>${round(c['attributes']['ext_abfluesse_mqn_jahr'],2) or '-'}</td></tr>
      <tr><th class="cell-left" colspan="2" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.noinfoforthisobject', lang)}</th></tr>
    % elif c['attributes']['ext_ezg_datenausgabe'] == 3:
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_regimetyp', lang)}</th>                 <td>${c['attributes']['ext_abfluesse_regimetyp'] or '-'}</td></tr>
      <tr><th class="cell-left" colspan="2" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.noinfoforthisobject', lang)}</th></tr>

    % else:
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_regimetyp', lang)}</th>                <td>${c['attributes']['ext_abfluesse_regimetyp'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_jan', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_jan'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_feb', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_feb'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_mar', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_mar'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_apr', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_apr'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_mai', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_mai'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_jun', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_jun'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_jul', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_jul'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_aug', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_aug'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_set', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_sep'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_okt', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_okt'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_nov', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_nov'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_dez', lang)}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_dez'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_mqn_jahr', lang)}</th>                 <td>${round(c['attributes']['ext_abfluesse_mqn_jahr'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${t.Translator.translate('tt_teileinzugsgebiete_2.abfluesse_abflussvar', lang)}</th>               <td>${c['attributes']['ext_abfluesse_abflussvar'] or '-'}</td></tr>
    % endif
      
    </table>

    % if image_exist:
      <div style="width: 100%;">
        <table class="table-with-border">
          <tr><td id="image" align="center"><img width=100% height= auto class="image"
          src="${img_url}"
          alt=""/></td>
        </table>
      </div>
    % endif
    % if zip_exist:
    <div>
      <table class="table-with-border">
        <tr><th class="cell-left">Download</th>                              <td><a href="${zip_url}" target="_blank">${t.Translator.translate('tt_teileinzugsgebiete_2.download', lang)}</a></td></tr>
      </table>
    </div>
    % endif

    <div class="chsdi-map-container table-with-border" style="width: 100%; height: 400px; page-break-inside: avoid;">
      <div id="map${id}"></div>
    </div>

</div>

<script type="text/javascript">
    var map = new ga.Map({
      target: 'map${id}',

      view: new ol.View({
        resolution: 10,
        center : [600000,200000]
      }),
      tooltip: false
      
    });
    var l1 = ga.layer.create('ch.swisstopo.pixelkarte-grau');
    var l2 = ga.layer.create('ch.bafu.wasser-teileinzugsgebiete_2');
    map.addLayer(l1);
    map.addLayer(l2);

    map.highlightFeature('${c['layerBodId']}', '${c['featureId']}');
    map.recenterFeature('${c['layerBodId']}', '${c['featureId']}');

</script>

</%def>

<%def name="extended_resources(c, lang)">
  <script type="text/javascript" src="${h.get_loaderjs_url(request)}"></script>
</%def>
