<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.number')}</td>       <td>${c['attributes']['label']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.name_de')}</td>      <td>${c['attributes']['name']}</td></tr>
</%def>
