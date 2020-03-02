<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang != 'rm' else 'de'
%>

    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.solarenergie-eignung-daecher_overview', lang)}</td>                     <td>${c['attributes'][lang] or '-'}</td></tr>
</%def>


<%def name="extended_info(c, lang)">
<body>

ARGH!

</body>
</%def>
