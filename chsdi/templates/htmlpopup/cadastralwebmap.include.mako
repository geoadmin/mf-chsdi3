<%def name="table_body_cadastral(c, lang, fallbackLang)">
    % if c['attributes']['ak'] in ['D','I','F','AUT']:
        <tr><td class="cell-left">${_('No info outside CH and FL')}</td><td></td></tr>
    % elif c['attributes']['ak'] and c['attributes']['geoportal_url']:
        <tr>
            <td class="cell-left">${_('link to canton geoportal')}</td>
            <td><a href="http://${c['attributes']['geoportal_url']}" target="_blank">${c['attributes']['ak']}</a></td>
        </tr>
    % else:
        <tr>
            <td class="cell-left">${_('link to canton geoportal')}</td>
            <td>${_('Canton has provided no link to portal')}</td>
        </tr>
    % endif
    <tr><td class="cell-left">${_('cwm_number')}</td><td>${c['attributes']['number'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('cwm_egris_egrid')}</td><td>${c['attributes']['egris_egrid'] or '-'}</td></tr>
    <tr>
        <td class="cell-left">${_('cwm_realestate_type')}</td>
        <td>${_('cwm_realestate_type_{}'.format(c['attributes'].get('realestate_type', 'default')) if c['attributes']['realestate_type'] is not None else 'cwm_realestate_type_default')}</td>
    </tr>
</%def>

