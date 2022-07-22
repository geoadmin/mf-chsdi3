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
    <td class="cell-left">${_('ch.bazl.einschraenkungen-drohnen.name')}</td>
    <td>${c['attributes'][zone_name] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.einschraenkungen-drohnen.restr')}</td>
    <td>${c['attributes'][zone_restriction] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.einschraenkungen-drohnen.bew_st')}</td>
    <td>${c['attributes'][zone_message] or '-'}</td>
  </tr>
  <tr>
    <td>${_('ch.bazl.einschraenkungen-drohnen.bew_li')}</td>
    <td><a href="${c['attributes'][auth_url]}" target="_blank">${_('ch.bazl.einschraenkungen-drohnen.bew_li_url')}</a>
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
      <td class="cell-meta">${_('ch.bazl.einschraenkungen-drohnen.name')}</td>
      <td class="cell-meta">${c['attributes'][zone_name] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.einschraenkungen-drohnen.restr')}</td>
      <td>${c['attributes'][zone_restriction] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bazl.einschraenkungen-drohnen.bew_st')}</td>
      <td>${c['attributes'][zone_message] or '-'}</td>
    </tr>
    <tr>
      <td>${_('ch.bazl.einschraenkungen-drohnen.bew_li')}</td>
      <td><a href="${c['attributes'][auth_url]}" target="_blank">${_('ch.bazl.einschraenkungen-drohnen.bew_li_url')}</a>
    </tr>
  </table>
</%def>
