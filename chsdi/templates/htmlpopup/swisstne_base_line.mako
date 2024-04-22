<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
      lang = lang if lang in ('fr','it','en') else 'de'
      basetype_text = 'basetype_%s' % lang
    %>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.uuid')}</td>
      <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.from_node_uuid')}</td>
      <td>${c['attributes']['from_node_uuid'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.to_node_uuid')}</td>
      <td>${c['attributes']['to_node_uuid'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.basetype')}</td>
      <td>${c['attributes'][basetype_text] or '-'}</td>
    </tr>
</%def>

