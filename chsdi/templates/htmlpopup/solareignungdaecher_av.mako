<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
<%
    lang = lang if lang != 'rm' else 'de'
%>

    <tr><td class="cell-left">${_('ch.bfe.solarenergie-eignung-daecher_overview')}</td>                     <td>${c['attributes']['de'] or '-'}</td></tr>
</%def>


<%def name="extended_info(c, lang)">
<body>

ARGH!

</body>
</%def>
