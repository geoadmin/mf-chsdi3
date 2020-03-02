<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${t.translate('name', lang)}</td><td>${c['attributes']['name'].strip()}</td></tr>
</%def>

