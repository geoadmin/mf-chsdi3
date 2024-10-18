<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
      lang = lang if lang in ('fr','it','en') else 'de'
      category_text = 'category_%s' % lang
      mineralisation_text = 'mineralisation_%s' % lang
      use_text = 'use_%s' % lang

      layer_id = c['layerBodId']
    %>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.category')}</td>
      <td>${c['attributes'][category_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.sample_temp')}</td>
      <td>${c['attributes']['sample_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.form_temp')}</td>
      <td>${c['attributes']['form_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.discharge')}</td>
      <td>${c['attributes']['discharge'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.ph')}</td>
      <td>${c['attributes']['ph'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.mineralisation_')}</td>
      <td>${c['attributes'][mineralisation_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.chem_type')}</td>
      <td>${c['attributes']['chem_type'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.use')}</td>
      <td>${c['attributes'][use_text] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
  <%
    lang = lang if lang in ('fr','it','en') else 'de'
    category_text = 'category_%s' % lang
    mineralisation_text = 'mineralisation_%s' % lang
    use_text = 'use_%s' % lang
    annot_text = 'annot_%s' % lang

    layerid = c['layerBodId']
  %>

  <table class="table-with-border" cellpadding="5">
    <tr>
      <td class="cell-left">${_(f'{layer_id}.category')}</td>
      <td>${c['attributes'][category_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.sample_temp')}</td>
      <td>${c['attributes']['sample_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.form_temp')}</td>
      <td>${c['attributes']['form_temp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.discharge')}</td>
      <td>${c['attributes']['discharge'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.ph')}</td>
      <td>${c['attributes']['ph'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.ec')}</td>
      <td>${c['attributes']['ec'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.mineralisation_')}</td>
      <td>${c['attributes'][mineralisation_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.chem_type')}</td>
      <td>${c['attributes']['chem_type'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.use')}</td>
      <td>${c['attributes'][use_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.date_measure')}</td>
      <td>${c['attributes']['date_measure'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.annot')}</td>
      <td>${c['attributes'][annot_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.x_lv95')}</td>
      <td>${c['attributes']['x_lv95'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.y_lv95')}</td>
      <td>${c['attributes']['y_lv95'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.elevation')}</td>
      <td>${c['attributes']['elevation'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.source1')}</td>
      <td>${c['attributes']['source1'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.src_link')}</td>
      <td>${c['attributes']['src_link'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.download')}</td>
      <td>${c['attributes']['download'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.swissgeol')}</td>
      <td>${c['attributes']['swissgeol'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.assets_swissgeol')}</td>
      <td>${c['attributes']['assets_swissgeol'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layer_id}.boreholes_swissgeol')}</td>
      <td>${c['attributes']['boreholes_swissgeol'] or '-'}</td>
    </tr>
    %if c['attributes']['category_de'] == 'Quelle':
      <tr>
        <td class="cell-left">${_(f'{layer_id}.catchwork_type')}</td>
        <td>${c['attributes']['catchwork_type_de'] or '-'}</td>
      </tr>
    %else if c['attributes']['category_de'] == 'Tunnel':
      <tr>
        <td class="cell-left">${_(f'{layer_id}.rock_overlay')}</td>
        <td>${c['attributes']['rock_overlay'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'{layer_id}.distance')}</td>
        <td>${c['attributes']['distance'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'{layer_id}.ref_portal')}</td>
        <td>${c['attributes']['ref_portal'] or '-'}</td>
      </tr>
    %else if c['attributes']['category_de'] == 'Borehole':
      <tr>
        <td class="cell-left">${_(f'{layer_id}.borehole_name')}</td>
        <td>${c['attributes']['borehole_name'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'{layer_id}.sample_interval')}</td>
        <td>${c['attributes']['sample_interval'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'{layer_id}.form_temp_depth')}</td>
        <td>${c['attributes']['form_temp_depth'] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_(f'{layer_id}.hydrogeologic_unit')}</td>
        <td>${c['attributes']['hydrogeologic_unit_de'] or '-'}</td>
      </tr>
    %endif
  </table>
</%def>
