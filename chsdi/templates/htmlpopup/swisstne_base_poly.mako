<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr','it','en') else 'de'
    type_text = 'type_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.swisstne-base.uuid')}</td>
    <td>${c['attributes']['uuid'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.swisstne-base.type')}</td>
    <td>${c['attributes'][type_text] or '-'}</td>
  </tr>
</%def>

