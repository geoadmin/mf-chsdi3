<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr>
      <td class="cell-left">${_('typ')}</td>
      <td>
        % if lang in ('de', 'rm', 'en'):
          ${c['attributes']['name'] or '-'}
        % else:
          ${c['attributes']['nom'] or '-'}
        % endif
      </td>
    </tr>
    <tr>
      <td class="cell-left">${_('flaeche_ha')}</td>
      % if c['attributes']['flaeche_ha']:
        <td>${int(round(c['attributes']['flaeche_ha']))}</td>
      % else:
        <td>-</td>
      % endif
    </tr>
</%def>
