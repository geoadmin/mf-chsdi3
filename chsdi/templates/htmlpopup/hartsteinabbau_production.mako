<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
      lang_select = lang if lang in ('fr','it','en') else 'de'
      stkind_text = 'stkind_%s' % lang_select
      ltkinds_text = 'ltkinds_%s' % lang_select
      emkinds_text = 'emkinds_%s' % lang_select

      lang_select = lang if lang in ('fr','it') else 'de'
      infos_url_text = 'infos_url_%s' % lang_select

      layerid = c['layerBodId']
    %>
    <tr>
      <td class="cell-left">${_(f'{layerid}.obname_production')}</td>
      <td>${c['attributes']['obname'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.cpkind_production')}</td>
      <td>${c['attributes']['cpkind'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.stkind_production')}</td>
      <td>${c['attributes'][stkind_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.infos_url')}</td>
    % if c['attributes'].get(infos_url_text, '-').startswith('http'):
      <td><a href="${c['attributes'][infos_url_text] or '-'}" target="_blank">${c['attributes'][infos_url_text] or '-'}</a></td></tr>
    % else:
      <td>${c['attributes'][infos_url_text] or '-'}</td>
    %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.purl')}</td>
    % if c['attributes'].get('purl', '-').startswith('http'):
      <td><a href="${c['attributes']['purl'] or '-'}" target="_blank">${c['attributes']['purl'] or '-'}</a></td></tr>
    % else:
      <td>${c['attributes']['purl'] or '-'}</td>
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
</%def>
