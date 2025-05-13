<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.hoheitsgrenzpunkte-landesvermessung.nummer')}</td>
      <td>${c['attributes']['nummer'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.hoheitsgrenzpunkte-landesvermessung.isthoheitsgrenzsteinalt')}</td>
      <td>${c['attributes']['isthoheitsgrenzsteinalt'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.hoheitsgrenzpunkte-landesvermessung.lagegenauigkeit')}</td>
      <td>${c['attributes']['lagegenauigkeit'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.hoheitsgrenzpunkte-landesvermessung.istlagezuverlaessig')}</td>
      <td>${c['attributes']['istlagezuverlaessig'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.hoheitsgrenzpunkte-landesvermessung.punktzeichen')}</td>
      <td>${c['attributes']['punktzeichen'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.hoheitsgrenzpunkte-landesvermessung.istexaktdefiniert')}</td>
      <td>${c['attributes']['istexaktdefiniert'] or '-'}</td>
    </tr>
</%def>
