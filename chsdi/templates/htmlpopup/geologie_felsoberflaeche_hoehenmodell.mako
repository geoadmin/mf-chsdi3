<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

  <% c['stable_id'] = False %>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-felsoberflaeche_hoehenmodell.height')}</td>
    % if c['attributes']['height']:
      <td>${round(c['attributes']['height'], 2)}</td>
    % else:
      <td>-</td>
    % endif
  </tr>
</%def>

