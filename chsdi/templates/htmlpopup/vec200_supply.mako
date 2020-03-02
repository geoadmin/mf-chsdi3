<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${t.Translator.translate('konf_objekt', lang)}</td><td>${c['attributes']['fco']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('lage_objekt')}</td><td>${_(c['attributes']['loc'] or '-', lang)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('typ_transpo_produkt', lang)}</td><td>
    % if c['attributes']['pro'].strip() in ['Null / No Value']:
    -
    % else:
    ${_(c['attributes']['pro'] or '-')}
    % endif
    </td></tr>
</%def>

