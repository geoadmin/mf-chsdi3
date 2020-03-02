<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${Translator.translate('ch_bafu_gee-kla.nummer', lang)}</td>                   <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch_bafu_gee-kla.name', lang)}</td>                     <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch_bafu_gee-kla.ort', lang)}</td>                      <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch_bafu_gee-kla.vsa_kategorie', lang)}</td>            <td>${c['attributes']['vsa_kategorie'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch_bafu_gee-kla.ausbaugroesse_egw', lang)}</td>        <td>${c['attributes']['ausbaugroesse_egw'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch_bafu_gee-kla.abwasseranteil_q347', lang)}</td>      <td>${round(c['attributes']['abwasseranteil_q347'],3) or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <td width="25%">&nbsp;</td>
      <td width="20%">&nbsp;</td>
      <td width="25%">&nbsp;</td>
      <td width="30%" >&nbsp;</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.nummer', lang)}</th>
      <td>${c['featureId'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.name', lang)}</th>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.rechtswert', lang)}</th>
      <td>${c['attributes']['rechtswert'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.hochwert', lang)}</th>
      <td>${c['attributes']['hochwert'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.hoehe', lang)}</th>
      <td>${c['attributes']['hoehe'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.adresse', lang)}</th>
      <td>${c['attributes']['adresse'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.plz', lang)}</th>
      <td>${c['attributes']['plz'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.ort', lang)}</th>
      <td>${c['attributes']['ort'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.tel_nr', lang)}</th>
      <td>${c['attributes']['tel_nr'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.vorfluterbez', lang)}</th>
      <td>${c['attributes']['vorfluterbez'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.name_vorfluter', lang)}</th>
      <td>${c['attributes']['name_vorfluter'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.gewiss_nr', lang)}</th>
      <td>${c['attributes']['gewiss_nr'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.reinigungstyp', lang)}</th>
      <td>${c['attributes']['reinigungstyp'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.abw_tagesmittel', lang)}</th>
      <td>${c['attributes']['abw_tagesmittel'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.abw_tagesspitze', lang)}</th>
      <td>${c['attributes']['abw_tagesspitze'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.spitzenbelastung_regen', lang)}</th>
      <td>${c['attributes']['spitzenbelastung_regen'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.rohabwasser_tag', lang)}</th>
      <td>${c['attributes']['rohabwasser_tag'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.frischschlamm_tag', lang)}</th>
      <td>${c['attributes']['frischschlamm_tag'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.stabilisierter_schlamm_tag', lang)}</th>
      <td>${c['attributes']['stabilisierter_schlamm_tag'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.bsb5anteil', lang)}</th>
      <td>${c['attributes']['bsb5anteil'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.bsb5absolut', lang)}</th>
      <td>${c['attributes']['bsb5absolut'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.csbanteil', lang)}</th>
      <td>${c['attributes']['csbanteil'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.csbabsolut', lang)}</th>
      <td>${c['attributes']['csbabsolut'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.docanteil', lang)}</th>
      <td>${c['attributes']['docanteil'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.docabsolut', lang)}</th>
      <td>${c['attributes']['docabsolut'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.nh4_nanteil', lang)}</th>
      <td>${c['attributes']['nh4_nanteil'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.nh4_nabsolut', lang)}</th>
      <td>${c['attributes']['nh4_nabsolut'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.nh4_n_ganzjaehrig', lang)}</th>
      <td>${c['attributes']['nh4_n_ganzjaehrig'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.nanteil', lang)}</th>
      <td>${c['attributes']['nanteil'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.nabsolut', lang)}</th>
      <td>${c['attributes']['nabsolut'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.n_abwassertemperatur', lang)}</th>
      <td>${c['attributes']['n_abwassertemperatur'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.gesamtpanteil', lang)}</th>
      <td>${c['attributes']['gesamtpanteil'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.gesamtpabsolut', lang)}</th>
      <td>${c['attributes']['gesamtpabsolut'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.gesamt_ungel_stoffe_absolut', lang)}</th>
      <td>${c['attributes']['gesamt_ungel_stoffe_absolut'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.andere_stoffe', lang)}</th>
      <td>${c['attributes']['andere_stoffe'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.kanton', lang)}</th>
      <td>${c['attributes']['kanton'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.vsa_kategorie', lang)}</th>
      <td>${c['attributes']['vsa_kategorie'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.ausbaugroesse_egw', lang)}</th>
      <td>${c['attributes']['ausbaugroesse_egw'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.anzahl_nat_einwohner', lang)}</th>
      <td>${c['attributes']['anzahl_nat_einwohner'] or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.jahr_nat_einwohner', lang)}</th>
      <td>${c['attributes']['jahr_nat_einwohner'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.abwasseranteil_q347', lang)}</th>
      <td>${round(c['attributes']['abwasseranteil_q347'],3) or '-'}</td>
      <th class="cell-left">${Translator.translate('ch_bafu_gee-kla.gwlnr', lang)}</th>
      <td>${c['attributes']['gwlnr'] or '-'}</td>
    </tr>
  </table>
</%def>


<%def name="extended_resources(c, lang)">
  <link rel="stylesheet" type="text/css" href="${h.versioned(request.static_url('chsdi:static/css/blueimp-gallery.min.css'))}"/>
  <script src="${h.versioned(request.static_url('chsdi:static/js/jquery.min.js'))}"></script>
  <script src="${h.versioned(request.static_url('chsdi:static/js/blueimp-gallery.min.js'))}"></script>
</%def>
