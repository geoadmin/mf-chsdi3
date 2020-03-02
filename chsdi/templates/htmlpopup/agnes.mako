<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${Translator.translate('name', lang)}</td>   <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('url', lang)}</td>    <td><a target="_blank" href="http://${c['attributes']['url']}">${_('url') or '-'}</a></td></tr>
</%def>
