<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
      <%
            lang = lang if lang in ('de', 'fr', 'it', 'en') else 'de'
            litho = 'litho_%s' % lang
      %>
      <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Litho')}</td>
        <td>${c['attributes'][litho] or '-'}</td>
      </tr>
</%def>

