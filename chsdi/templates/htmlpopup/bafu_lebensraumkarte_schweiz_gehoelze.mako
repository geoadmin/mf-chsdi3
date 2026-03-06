<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it') else 'de'
    typoch = 'typoch_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz_gehoelze.polyid')}</td>
    <td>${c['attributes']['polyid'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz_gehoelze.typoch')}</td>
    <td>${c['attributes'][typoch] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz_gehoelze.crown_area')}</td>
    % if c['attributes']['crown_area']:
      <td>${round(c['attributes']['crown_area'])}</td>
    % else:
      <td>-</td>
    % endif
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz_gehoelze.mean_hght')}</td>
    % if c['attributes']['mean_hght']:
      <td>${round(c['attributes']['mean_hght'], 2)}</td>
    % else:
      <td>-</td>
    % endif
  </tr>
</%def>
