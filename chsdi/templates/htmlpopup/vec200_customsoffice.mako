<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${Translator.translate('name', lang)}</td><td>${c['attributes']['objname']}</td></tr>
</%def>
