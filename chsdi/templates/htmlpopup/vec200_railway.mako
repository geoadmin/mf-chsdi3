<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${t.Translator.translate('construct', lang)}</td><td>${c['attributes']['construct'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('typ', lang)}</td><td>${c['attributes']['objval']}</td></tr>
</%def>
