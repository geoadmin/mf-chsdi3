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
      <td class="cell-left">${_('ch.bafu.wasser-teileinzugsgebiete_2.id')}</td>
      <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.wasser-teileinzugsgebiete_2.gwlnr')}</td>
      <td>${c['attributes']['gwlnr'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_measure_2')}</td>
      <td>${c['attributes']['measure'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('teilezgfla')}</td>
      <td>${c['attributes']['teilezgfla'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ezgflaeche')}</td>
      <td>${c['attributes']['ezgflaeche'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('typ')}</td>
      <td>${c['attributes'][typ] or c['attributes'][typ_supp] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_flussgb')}</td>
      <td>${c['attributes'][fluss] or c['attributes'][fluss_supp] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
<%
  from urllib2 import urlopen

  webDavHost = request.registry.settings['webdav_host']
  
  img_url = webDavHost + "/bafu/ch.bafu.wasser-teileinzugsgebiete_2/images/" + str(c['featureId']) + ".png"
  zip_url = webDavHost + "/bafu/ch.bafu.wasser-teileinzugsgebiete_2/downloads/" + str(100000+c['featureId']) + ".zip"
  image = None
  zip = None

  try:
      image = urlopen(img_url)
      image_exist = True
  except:
      image_exist = False
  finally:
      if image:
          image.close()

  try:
      zip = urlopen(zip_url)
      zip_exist = True
  except urllib2.HTTPError:
      zip_exist = False
  finally:
      if zip:
          zip.close()


  id = c['featureId']
  
%>
<div>
    <table class="table-with-border">
      <tr><th class="cell-left" colspan="2">${_('tt_teileinzugsgebiete_2.ebene2km_teil1')}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.namen_gewaesser')}</th>          <td>${c['attributes']['ext_gewiss_nr_namen_gewaesser'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('ch.bafu.wasser-teileinzugsgebiete_2.gwlnr')}</th>                                  <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.xy_gebietsauslass')}</th>              <td>${c['attributes']['ext_ezg_xy_gebietsauslass'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.gebietsauslaesse_gemeindename')}</th>      <td>${c['attributes']['ext_gebietsauslaesse_gemeindename'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.gewissnr')}</th>                       <td>${c['attributes']['ext_ezg_gewissnr'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_ezg_flussgb')}</th>                        <td>${c['attributes']['ext_ezg_flussgb'] or '-'}</td></tr>
    % if c['attributes']['ext_physiogeographie_gesamtflaeche']:
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${_('tt_teileinzugsgebiete_2.ebene2km_teil2')}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.physiogeographie_gesamtflaeche')}</th>     <td>${round(c['attributes']['ext_physiogeographie_gesamtflaeche'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.physiogeographie_anteil_ch')}</th>         <td>${round(c['attributes']['ext_physiogeographie_anteil_ch'],1) or '-'}</td></tr>
    % endif
    % if c['attributes']['ext_landnutzung_ant_bestockt']:
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${_('tt_teileinzugsgebiete_2.ebene2km_teil3')}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.landnutzung_ant_bestockt')}</th>           <td>${round(c['attributes']['ext_landnutzung_ant_bestockt'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.landnutzung_ant_landwirtschaft')}</th>     <td>${round(c['attributes']['ext_landnutzung_ant_landwirtschaft'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.landnutzung_ant_unprod_sonst')}</th>       <td>${round(c['attributes']['ext_landnutzung_ant_unprod_sonst'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.landnutzung_ant_gewaesser')}</th>          <td>${round(c['attributes']['ext_landnutzung_ant_gewaesser'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.landnutzung_ant_gletscher_firn')}</th>     <td>${round(c['attributes']['ext_landnutzung_ant_gletscher_firn'],1) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.landnutzung_ant_siedlung')}</th>           <td>${round(c['attributes']['ext_landnutzung_ant_siedlung'],1) or '-'}</td></tr>
    % endif
    % if c['attributes']['ext_physiogeographie_ch_min_z']:
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${_('tt_teileinzugsgebiete_2.ebene2km_teil4')}</th></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.physiogeographie_ch_min_z')}</th>          <td>${int(c['attributes']['ext_physiogeographie_ch_min_z']) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.physiogeographie_ch_max_z')}</th>          <td>${int(c['attributes']['ext_physiogeographie_ch_max_z']) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.physiogeographie_ch_mean_z')}</th>         <td>${int(c['attributes']['ext_physiogeographie_ch_mean_z']) or '-'}</td></tr>
    % endif
      <tr><th class="cell-left" colspan="2"></th></tr>
      <tr><th class="cell-left" colspan="2">${_('tt_teileinzugsgebiete_2.ebene2km_teil5')|n}</th></tr>

    % if c['attributes']['ext_ezg_datenausgabe'] == 0:
      <tr><th class="cell-left" colspan="2" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.noinfoforthisobject')|n}</th></tr>
    % elif c['attributes']['ext_ezg_datenausgabe'] == 2:
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_jahr')}</th>                 <td>${round(c['attributes']['ext_abfluesse_mqn_jahr'],2) or '-'}</td></tr>
      <tr><th class="cell-left" colspan="2" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.noinfoforthisobject')}</th></tr>
    % elif c['attributes']['ext_ezg_datenausgabe'] == 3:
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_regimetyp')}</th>                 <td>${c['attributes']['ext_abfluesse_regimetyp'] or '-'}</td></tr>
      <tr><th class="cell-left" colspan="2" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.noinfoforthisobject')}</th></tr>

    % else:
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_regimetyp')}</th>                <td>${c['attributes']['ext_abfluesse_regimetyp'] or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_jan')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_jan'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_feb')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_feb'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_mar')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_mar'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_apr')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_apr'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_mai')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_mai'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_jun')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_jun'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_jul')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_jul'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_aug')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_aug'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_set')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_sep'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_okt')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_okt'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_nov')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_nov'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_dez')}</th>                  <td>${round(c['attributes']['ext_abfluesse_mqn_dez'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_mqn_jahr')}</th>                 <td>${round(c['attributes']['ext_abfluesse_mqn_jahr'],2) or '-'}</td></tr>
      <tr><th class="cell-left" style="font-weight: normal">${_('tt_teileinzugsgebiete_2.abfluesse_abflussvar')}</th>               <td>${c['attributes']['ext_abfluesse_abflussvar'] or '-'}</td></tr>
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
        <tr><th class="cell-left">Download</th>                              <td><a href="${zip_url}" target="_blank">${_('tt_teileinzugsgebiete_2.download')}</a></td></tr>
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
