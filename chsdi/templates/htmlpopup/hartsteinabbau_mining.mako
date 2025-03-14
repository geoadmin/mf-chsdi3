<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
      lang_select = lang if lang in ('fr','it','en') else 'de'
      stkind_text = 'stkind_%s' % lang_select
      ltkinds_text = 'ltkinds_%s' % lang_select
      emkinds_text = 'emkinds_%s' % lang_select

      lang_url_select ={
        "de": "de",
        "en": "de",
        "rm": "de",
        "fr": "fr",
        "it": "fr",
      }
      infos_url_text = 'infos_url_%s' % lang_url_select[lang]

      layerid = c['layerBodId']
    %>
    <tr>
      <td class="cell-left">${_(f'{layerid}.obname_mining')}</td>
      <td>${c['attributes']['obname'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.cpkind_mining')}</td>
      <td>${c['attributes']['cpkind'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.stkind_mining')}</td>
      <td>${c['attributes'][stkind_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.ltkinds')}</td>
      <td>${c['attributes'][ltkinds_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.emkinds')}</td>
      <td>${c['attributes'][emkinds_text] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.infos_url')}</td>
    % if c['attributes'].get(infos_url_text, '-').startswith('http'):
      <td><a href="${c['attributes'][infos_url_text] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes'][infos_url_text] or '-'}</td>
    %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.purl')}</td>
    % if c['attributes'].get('purl', '-').startswith('http'):
      <td><a href="${c['attributes']['purl'] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes']['purl'] or '-'}</td>
    %endif
    </tr>
    <tr>
      <td class="cell-left">${_(f'{layerid}.swissgeol_link')}</td>
    % if c['attributes'].get('swissgeol_link', '-').startswith('http'):
      <td><a href="${c['attributes']['swissgeol_link'] or '-'}" target="_blank">${_('link')}</a></td></tr>
    % else:
      <td>${c['attributes']['swissgeol_link'] or '-'}</td>
    %endif
    </tr>
</%def>
