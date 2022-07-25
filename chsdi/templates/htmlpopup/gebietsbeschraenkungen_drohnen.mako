<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    zone_name = 'zone_name_%s' % lang
    zone_restriction = 'zone_restriction_%s' % lang
    zone_message = 'zone_message_%s' % lang
    auth_url = 'auth_url_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_name')}</td>
    <td>${c['attributes'][zone_name] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_restriction')}</td>
    <td>${c['attributes'][zone_restriction] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_message')}</td>
    <td>${c['attributes'][zone_message] or '-'}</td>
  </tr>
  <tr>
    <td>${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_url')}</td>
    <td><a href="${c['attributes'][auth_url]}" target="_blank">${_('ch.bazl.gebietsbeschraenkungen-drohnen.bew_li_url')}</a>
  </tr>
</%def>

<%def name="extended_info(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    zone_name = 'zone_name_%s' % lang
    zone_restriction = 'zone_restriction_%s' % lang
    zone_message = 'zone_message_%s' % lang
    auth_url = 'auth_url_%s' % lang
  %>
  <table>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_name')}</td>
      <td>${c['attributes'][zone_name] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_restriction')}</td>
      <td>${c['attributes'][zone_restriction] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.gebietsbeschraenkungen-drohnen.zone_message')}</td>
      <td>${c['attributes'][zone_message] or '-'}</td>
    </tr>
    <tr>
      <td>${_('ch.bazl.gebietsbeschraenkungen-drohnen.auth_url')}</td>
      <td><a href="${c['attributes'][auth_url]}" target="_blank">${_('ch.bazl.gebietsbeschraenkungen-drohnen.bew_li_url')}</a>
    </tr>
  </table>
</%def>
