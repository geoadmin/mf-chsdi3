<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('name')}</td><td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('klasse')}</td>
      % if lang in ('de', 'rm', 'en'):
           <td>${c['attributes']['klasse_de'] or '-'}</td>
      % else:
           <td>${c['attributes']['klasse_fr'] or '-'}</td>
      % endif
    </tr>
    <tr>
        % if c['attributes']['flaeche_ha']:
            <td class="cell-left">${_('flaeche_ha')}</td><td>${int(round(c['attributes']['flaeche_ha']))}</td>
        % else:
            <td class="cell-left">${_('flaeche_ha')}</td><td>-</td>
        % endif
    </tr>
</%def>
