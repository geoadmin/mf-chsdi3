<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    attendantplanttype_text = 'attendantplanttype_%s' % lang
  %>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.attendantplanttype')}</td>
    <td>${c['attributes'][attendantplanttype_text] or '-'}</td>
  </tr>
</%def>
