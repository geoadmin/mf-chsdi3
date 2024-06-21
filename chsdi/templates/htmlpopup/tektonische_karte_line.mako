<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
      <%
            lang = lang if lang in ('de', 'fr', 'it', 'en') else 'de'
            kind = 'kind_%s' % lang
            name = 'name_%s' % lang
            status = 'status_%s' % lang
      %>
      <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Kind')}</td>
        <td>${c['attributes'][kind] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Name')}</td>
        <td>${c['attributes'][name] or '-'}</td>
      </tr>
      <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Status')}</td>
        <td>${c['attributes'][status] or '-'}</td>
      </tr>
</%def>
