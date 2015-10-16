<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
%>

    <tr><td class="cell-left">${_('ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte.stationnam')}</td>        <td>${c['attributes']['stationnam'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('coordinate_x')}</td>                                                             <td>${c['attributes']['coordhor'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('coordinate_y')}</td>                                                             <td>${c['attributes']['coordver'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte.altitude')}</td>          <td>${c['attributes']['altitude'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('bouguer_anomalie')}</td>                                                         <td>${c['attributes']['bouguerano'] or '-'}</td></tr>
</%def>
