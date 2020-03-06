<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr>
      <td class="cell-left">${h.translate('typ', lang)}</td>
      <td>
        % if lang in ('de', 'rm', 'en'):
          ${c['attributes']['name'] or '-'}
        % else:
          ${c['attributes']['nom'] or '-'}
        % endif
      </td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('flaeche_ha', lang)}</td>
      <td>${int(round(c['attributes']['flaeche_ha'])) or '-'}</td>
    </tr>
</%def>
