<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
<%
    lang = lang if lang != 'rm' else 'de'
%>

    <tr><td class="cell-left">${_('betrieb')}</td>                     <td>${c['attributes']['betrieb'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_swissprtr_ort')}</td>            <td>${c['attributes']['ort'] or '-'}</td></tr>
</%def>

