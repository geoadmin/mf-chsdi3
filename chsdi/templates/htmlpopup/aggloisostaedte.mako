<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('name', lang)}</td><td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('klasse', lang)}</td>
      % if lang in ('de', 'rm', 'en'):
           <td>${c['attributes']['klasse_de'] or '-'}</td>
      % else:
           <td>${c['attributes']['klasse_fr'] or '-'}</td>
      % endif
    </tr>
    % if c['attributes']['flaeche_ha']:
        <tr><td class="cell-left">${mod_translate.Translator.translate('flaeche_ha', lang)}</td>    <td>${int(round(c['attributes']['flaeche_ha']))}</td></tr>
    % else:
        <tr><td class="cell-left">${mod_translate.Translator.translate('flaeche_ha', lang)}</td>    <td>-</td></tr>
    % endif
</%def>
