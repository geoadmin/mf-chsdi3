<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
      lang_select = lang if lang in ('fr','it','en') else 'de'
      please_note = 'please_note_%s' % lang_select
      unit = 'unit_%s' % lang_select
      usable_thickness_concat = 'usable_thickness_concat_%s' % lang_select
      legend_simple_tooltip = 'legend_simple_tooltip_%s' % lang_select

      layerid = c['layerBodId']
    %>
    <tr>
      <td class="cell-left">${_(f'{layerid}.please_note')}</td>
      <td>${c['attributes'][please_note] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.unit')}</td>
      <td>${c['attributes'][unit] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.thickness_concat')}</td>
      <td>${c['attributes']['thickness_concat'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.usable_thickness_concat')}</td>
      <td>${c['attributes'][usable_thickness_concat] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.usability_ratio_concat')}</td>
      <td>${c['attributes']['usability_ratio_concat'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.legend_simple_tooltip')}</td>
    % if c['attributes'].get(legend_simple_tooltip, '-').startswith('http'):
      <td><a href="${c['attributes'][legend_simple_tooltip] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes'][infos_url_text] or '-'}</td>
    %endif
    </tr>
</%def>

<%def name="extended_info(c, lang)">
  <%
    lang_select = lang if lang in ('fr','it','en') else 'de'
    please_note = 'please_note_%s' % lang_select
    unit = 'unit_%s' % lang_select
    usable_thickness_concat = 'usable_thickness_concat_%s' % lang_select
    usable_lithologies = 'usable_lithologies_%s' % lang_select
    not_usable_lithologies = 'not_usable_lithologies_%s' % lang_select
    legend = 'legend_%s' % lang_select
    level_of_confidence = 'level_of_confidence_%s' % lang_select
    thickness_boxplot_descr = 'thickness_boxplot_descr_%s' %lang_select

    lang_mat_mapping ={
      "de": "de",
      "en": "de",
      "rm": "de",
      "fr": "fr",
      "it": "fr",
    }
    mat_min_link = 'mat_min_link_%s' % lang_mat_mapping[lang]
    layerid = c['layerBodId']
  %>

  <table class="table-with-border" cellpadding="5">
    <tr>
      <td class="cell-left">${_(f'{layerid}.please_note')}</td>
      <td>${c['attributes'][please_note] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.unit')}</td>
      <td>${c['attributes'][unit] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.thickness_concat')}</td>
      <td>${c['attributes']['thickness_concat'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.usable_thickness_concat')}</td>
      <td>${c['attributes'][usable_thickness_concat] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.usability_ratio_concat')}</td>
      <td>${c['attributes']['usability_ratio_concat'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.usable_lithologies')}</td>
      <td>${c['attributes'][usable_lithologies] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.not_usable_lithologies')}</td>
      <td>${c['attributes'][not_usable_lithologies] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.elevation')}</td>
      <td>${c['attributes']['elevation'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left"">${_(f'{layerid}.legend')}</td>
      % if c['attributes'].get(legend, '-').startswith('http'):
        <td>
            <a href="${c['attributes'][legend]}" target="_blank"><img class="image" src="${c['attributes'][legend]}" alt="" style="width: 100%;"/></a>
        </td>
      % else:
        <td>${c['attributes'][legend] or '-'}</td>
      %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.data_density_thickness')}</td>
      <td>${c['attributes']['data_density_thickness'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.data_density_usability')}</td>
      <td>${c['attributes']['data_density_usability'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.level_of_confidence')}</td>
      <td>${c['attributes'][level_of_confidence] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.thickness_boxplot_descr')}</td>
      <td>${c['attributes'][thickness_boxplot_descr] or '-'}</td>
    </tr>
    <tr>
      <td colspan="2">
      % if c['attributes'].get('thickness_boxplot_filename', '-').startswith('http'):
            <a href="${c['attributes']['thickness_boxplot_filename']}" target="_blank"><img class="image" src="${c['attributes']['thickness_boxplot_filename']}" alt="" style="width: 100%;"/></a>
      % else:
        ${c['attributes']['thickness_boxplot_filename'] or '-'}
      %endif
      </td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.hst_catalog_link')}</td>
    % if c['attributes'].get('hst_catalog_link', '-').startswith('http'):
      <td><a href="${c['attributes']['hst_catalog_link'] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes']['hst_catalog_link'] or '-'}</td>
    %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.tech_doc_link')}</td>
    % if c['attributes'].get('tech_doc_link', '-').startswith('http'):
      <td><a href="${c['attributes']['tech_doc_link'] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes']['tech_doc_link'] or '-'}</td>
    %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.auto_thickness_paper_link')}</td>
    % if c['attributes'].get('auto_thickness_paper_link', '-').startswith('http'):
      <td><a href="${c['attributes']['auto_thickness_paper_link'] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes']['auto_thickness_paper_link'] or '-'}</td>
    %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.mat_min_link')}</td>
    % if c['attributes'].get(mat_min_link, '-').startswith('http'):
      <td><a href="${c['attributes'][mat_min_link] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes'][mat_min_link] or '-'}</td>
    %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.swissgeol_link')}</td>
    % if c['attributes'].get('swissgeol_link', '-').startswith('http'):
      <td><a href="${c['attributes']['swissgeol_link'] or '-'}" target="_blank">${c['attributes']['swissgeol_link'] or '-'}</a></td></tr>
    % else:
      <td>${c['attributes']['swissgeol_link'] or '-'}</td>
    %endif
    </tr>
  </table>
</%def>
