# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bfe.kernkraftwerke.name')}</td>          <td>${c['attributes']['name']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
    <%
        lang_i = {'de':0, 'fr':1, 'it':2, 'en':3}.get(lang, 0)
        link_i = 4
        operator = c['attributes']['operator'].split('##')
        enforcement_1 = c['attributes']['enforcement_1'].split('##')
        enforcement_2 = c['attributes']['enforcement_2'].split('##')
        enforcement_3 = c['attributes']['enforcement_3'].split('##')
        regulatory = c['attributes']['regulatory'].split('##')
        license = [c['attributes']['license_de'], c['attributes']['license_fr'], c['attributes']['license_it'], c['attributes']['license_en']]
        reactor_name = c['attributes']['reactor_name'].split('##')
        life_phase = [c['attributes']['life_phase_de'], c['attributes']['life_phase_fr'], c['attributes']['life_phase_it'], c['attributes']['life_phase_en']]
        reactor_type = [c['attributes']['reactor_type_de'], c['attributes']['reactor_type_fr'], c['attributes']['reactor_type_it'], c['attributes']['reactor_type_en']]
        cooling_type = [c['attributes']['cooling_type_de'], c['attributes']['cooling_type_fr'], c['attributes']['cooling_type_it'], c['attributes']['cooling_type_en']]
        life_phase = list(map(lambda x: x.split('##'), life_phase))
        reactor_type = list(map(lambda x: x.split('##'), reactor_type))
        cooling_type = list(map(lambda x: x.split('##'), cooling_type))
        nominal_thermal_output = c['attributes']['nominal_thermal_output'].split('##');
        gross_el_output = c['attributes']['gross_el_output'].split('##');
        net_el_output = c['attributes']['net_el_output'].split('##');
        construction_phase = c['attributes']['construction_phase'].split('##');
        commissioning_phase = c['attributes']['commissioning_phase'].split('##');
        operation_phase = c['attributes']['operation_phase'].split('##');
        decontamination_phase = c['attributes']['decontamination_phase'].split('##');
        dismantling_phase = c['attributes']['dismantling_phase'].split('##');

    %>
    <script>
        $(document).ready(function(){
            $('.thumbnail-container').on('click', function (event) {
              event = event || window.event;
                event.preventDefault();
              var target = event.target || event.srcElement,
                link = target.src ? target.parentNode : target,
                options = {index: link, event: event},
                links = this.getElementsByTagName('a');
              blueimp.Gallery(links, options);
            });
        });
    </script>
    <table class="table-with-border kernkraftwerke-extended">
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.name')}</th>          <td>${c['attributes']['name']}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.operator')}</th>      <td><a href='${operator[link_i]}'>${operator[lang_i]}</a></td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.enforcement_1')}</th>      <td><a href='${enforcement_1[link_i]}'>${enforcement_1[lang_i]}</a></td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.enforcement_2')}</th>      <td><a href='${enforcement_2[link_i]}'>${enforcement_2[lang_i]}</a></td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.enforcement_3')}</th>      <td><a href='${enforcement_3[link_i]}'>${enforcement_3[lang_i]}</a></td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.regulatory')}</th>      <td><a href='${regulatory[link_i]}'>${regulatory[lang_i]}</a></td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.license_de')}</th>      <td>${license[lang_i]}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.municipality')}</th>      <td>${c['attributes']['municipality']}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.canton')}</th>      <td>${c['attributes']['canton']}</td></tr>

    % for reactor_i in range(0, c['attributes']['reactors']):
        <tr></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.reactor_name')}</th>      <td><strong>${reactor_name[reactor_i]}</strong></td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.life_phase_de')}</th>      <td>${list(life_phase)[lang_i][reactor_i]}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.reactor_type_de')}</th>      <td>${list(reactor_type)[lang_i][reactor_i]}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.cooling_type_de')}</th>      <td>${list(cooling_type)[lang_i][reactor_i]}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.nominal_thermal_output')}</th>      <td>${list(nominal_thermal_output)[reactor_i]} MW</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.gross_el_output')}</th>      <td>${list(gross_el_output)[reactor_i]} MWe</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.net_el_output')}</th>      <td>${list(net_el_output)[reactor_i]} MWe</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.construction_phase')}</th>      <td>${list(construction_phase)[reactor_i]}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.operation_phase')}</th>      <td>${list(operation_phase)[reactor_i]}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.kernkraftwerke.decontamination_phase')}</th>      <td>${list(decontamination_phase)[reactor_i]}</td></tr>
    % endfor
    </table>
    <div class="thumbnail-container">
        <div class="thumbnail">
            <a href="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.kernkraftwerke/plant${c['featureId']}.jpg">
                <img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.kernkraftwerke/plant${c['featureId']}.jpg" />
            </a>
            Bild copyright ENSI
        </div>
    </div>
    <div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls">
      <div class="slides"></div>
      <div class="title">${c['attributes']['name'] or ''}</div>
      <a class="prev">&lsaquo;</a>
      <a class="next">&rsaquo;</a>
      <a class="close">x</a>
      <a class="play-pause"></a>
      <ol class="indicator"></ol>
    </div>
</%def>

<%def name="extended_resources(c, lang)">
  <link rel="stylesheet" type="text/css" href="${request.static_url('chsdi:static/css/blueimp-gallery.min.css')}"/>
  <script src="${request.static_url('chsdi:static/js/jquery.min.js')}"></script>
  <script src="${request.static_url('chsdi:static/js/blueimp-gallery.min.js')}"></script>
</%def>
