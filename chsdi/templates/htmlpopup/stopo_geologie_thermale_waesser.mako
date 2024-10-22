<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
      lang = lang if lang in ('fr','it','en') else 'de'
      mineralisation_text = 'mineralisation_%s' % lang
      use_text = 'use_%s' % lang
    %>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.sample_temp')}</td>
      <td>${c['attributes']['sample_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.form_temp')}</td>
      <td>${c['attributes']['form_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.discharge')}</td>
      <td>${c['attributes']['discharge'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.ph')}</td>
      <td>${c['attributes']['ph'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.mineralisation')}</td>
      <td>${c['attributes'][mineralisation_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.chem_type')}</td>
      <td>${c['attributes']['chem_type'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.use')}</td>
      <td>${c['attributes'][use_text] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
  <%
    lang = lang if lang in ('fr','it','en') else 'de'
    mineralisation_text = 'mineralisation_%s' % lang
    use_text = 'use_%s' % lang
    annot_text = 'annot_%s' % lang
    hydrogeologic_unit_text = 'hydrogeologic_unit_%s' % lang
  %>

  <table class="table-with-border" cellpadding="5">
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.sample_temp')}</td>
      <td>${c['attributes']['sample_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.form_temp')}</td>
      <td>${c['attributes']['form_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.discharge')}</td>
      <td>${c['attributes']['discharge'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.ph')}</td>
      <td>${c['attributes']['ph'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.ec')}</td>
      <td>${c['attributes']['ec'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.mineralisation')}</td>
      <td>${c['attributes'][mineralisation_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.chem_type')}</td>
      <td>${c['attributes']['chem_type'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.use')}</td>
      <td>${c['attributes'][use_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.date_measure')}</td>
      <td>${c['attributes']['date_measure'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.annot')}</td>
      <td>${c['attributes'][annot_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.x_lv95')}</td>
      <td>${c['attributes']['x_lv95'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.y_lv95')}</td>
      <td>${c['attributes']['y_lv95'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.elevation')}</td>
      <td>${c['attributes']['elevation'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.source1')}</td>
      <td>${c['attributes']['source1'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.src_link')}</td>
      % if c['attributes']['src_link'].startswith('http'):
        <td><a href="${c['attributes']['src_link']}" target="_blank">${c['attributes']['src_link']}</a></td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.download')}</td>
      % if c['attributes']['download'].startswith('http'):
        <td><a href="${c['attributes']['download']}" target="_blank">${c['attributes']['download']}</a></td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.swissgeol')}</td>
      <td>${c['attributes']['swissgeol'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.assets_swissgeol')}</td>
      <td>${c['attributes']['assets_swissgeol'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.boreholes_swissgeol')}</td>
      <td>${c['attributes']['boreholes_swissgeol'] or '-'}</td>
    </tr>
    % if c['attributes']['category_de'] == 'Quelle':
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.catchwork_type')}</td>
        <td>${c['attributes']['catchwork_type_de'] or '-'}</td>
      </tr>
    % elif c['attributes']['category_de'] == 'Tunnel':
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.rock_overlay')}</td>
        <td>${c['attributes']['rock_overlay'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.distance')}</td>
        <td>${c['attributes']['distance'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.ref_portal')}</td>
        <td>${c['attributes']['ref_portal'] or '-'}</td>
      </tr>
    %elif c['attributes']['category_de'] == 'Borehole':
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.borehole_name')}</td>
        <td>${c['attributes']['borehole_name'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.sample_interval')}</td>
        <td>${c['attributes']['sample_interval'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.form_temp_depth')}</td>
        <td>${c['attributes']['form_temp_depth'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'ch.swisstopo.geologie-thermale_waesser.hydrogeologic_unit')}</td>
        <td>${c['attributes'][hydrogeologic_unit_text] or '-'}</td>
      </tr>
    %endif
  </table>
</%def>
