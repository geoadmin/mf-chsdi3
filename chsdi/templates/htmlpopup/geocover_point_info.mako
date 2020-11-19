<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = 'de' if lang in ('de', 'rm', 'en') else 'fr'
    description = 'description_%s' % lang
%>
    <tr><td class="cell-left">${_('geocover_description')}</td><td>${c['attributes'][description] or '-'}</td></tr>
</%def>
