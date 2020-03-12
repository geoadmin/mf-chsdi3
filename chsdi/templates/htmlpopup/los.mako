<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    % if c['attributes']['operatsname'] and c['attributes'] :
    <tr><td class="cell-left" valign="top">${t.translate('losentreprise', lang)}</td>    <td>${c['attributes']['operatsname'] or '-'}</td></tr>
    % endif
    % if c['attributes']['losnr'] and c['attributes']:
    <tr><td class="cell-left">${t.translate('losnummer', lang)}</td>    <td>${c['attributes']['losnr'] or '-'}</td></tr>
    % endif
    % if c['attributes']['taetigkeit_d'] and c['attributes']:
    <tr><td class="cell-left">${t.translate('losactivite', lang)}</td>
      % if lang == 'de'or lang == 'rm' or lang == 'en':
           <td>${c['attributes']['taetigkeit_d'] or '-'}</td>
      % elif lang == 'fr':
           <td>${c['attributes']['taetigkeit_f'] or '-'}</td>
      % elif lang == 'it':
           <td>${c['attributes']['taetigkeit_i'] or '-'}</td>
      % endif
    </tr>
    % endif
    % if c['attributes']['quality'] and c['attributes']:
    <tr><td class="cell-left">${t.translate('losquality', lang)}</td>    <td>${c['attributes']['quality'] or '-'}</td></tr>
    % endif
    % if c['attributes']['flaeche_vertrag']:
    <tr><td class="cell-left">${t.translate('losarea', lang)}</td>    <td>${c['attributes']['flaeche_vertrag'] or '-'}</td></tr>
    % endif
    % if c['attributes']['frame']:
        <tr><td class="cell-left">${t.translate('losbezungsramen', lang)}</td>    <td>${c['attributes']['frame'] or '-'}</td></tr>
    % endif
    % if c['attributes']['neu_id']:
    <tr><td class="cell-left">${t.translate('losidentifikator', lang)}</td>    <td>${c['attributes']['neu_id'] or '-'}</td></tr>
    % endif
</%def>
