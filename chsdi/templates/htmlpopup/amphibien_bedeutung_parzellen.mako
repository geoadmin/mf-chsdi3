<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        layer = c['layerBodId']
    %>

    <tr><td class="cell-left">${_(layer + '.species_corridors')}</td> <td>${c['attributes']['species_corridors'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.species_suit200')}</td> <td>${c['attributes']['species_suit200'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.species_suit500')}</td> <td>${c['attributes']['species_suit500'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.species_suit1000')}</td> <td>${c['attributes']['species_suit1000'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.bedeutung_parzelle')}</td> <td>${c['attributes']['bedeutung_parzelle'] or '-'}</td></tr>
</%def>

