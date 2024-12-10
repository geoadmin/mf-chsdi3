<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it') else 'de'
    typoch = 'typoch_%s' % lang
    prob = 'prob_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz.polyid')}</td>
    <td>${c['attributes']['polyid'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz.typoch')}</td>
    <td>${c['attributes'][typoch] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz.prob')}</td>
    <td>${c['attributes'][prob] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bafu.lebensraumkarte-schweiz.cover')}</td>
    % if c['attributes']['cover'] and c['attributes']['cover'] < 9999:
      <td>${c['attributes']['cover']}</td>
    % else:
      <td>-</td>
    % endif
  </tr>
</%def>
