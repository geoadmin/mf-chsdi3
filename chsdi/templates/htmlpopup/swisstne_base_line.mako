<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
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
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.rail')}</td>
      <td>
        % if c['attributes']['rail'] == 0:
          ${_('No')}
        % elif c['attributes']['rail'] == 1:
          ${_('Yes')}
        % else:
          -
        % endif
      </td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.road')}</td>
      <td>
        % if c['attributes']['road'] == 0:
          ${_('No')}
        % elif c['attributes']['road'] == 1:
          ${_('Yes')}
        % else:
          -
        % endif
      </td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.cableway')}</td>
      <td>
        % if c['attributes']['cableway'] == 0:
          ${_('No')}
        % elif c['attributes']['cableway'] == 1:
          ${_('Yes')}
        % else:
          -
        % endif
      </td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.water')}</td>
      <td>
        % if c['attributes']['water'] == 0:
          ${_('No')}
        % elif c['attributes']['water'] == 1:
          ${_('Yes')}
        % else:
          -
        % endif
      </td>
    </tr>
</%def>

