<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    container_type_text = 'container_type_%s' % lang
  %>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.containertype')}</td>
    <td>${c['attributes'][container_type_text] or '-'}</td>
  </tr>
</%def>
