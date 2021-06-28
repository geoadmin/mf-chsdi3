<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = 'de' if lang == 'rm' else lang
    name = 'name_' + lang
%>
    <tr><td class="cell-left">${_('id')}</td>           <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('name')}</td>         <td>${c['attributes'][name] or '-'}</td></tr>
</%def>
