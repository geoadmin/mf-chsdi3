<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bafu.kompartimente-luchs.teilkomp_name')}</td>    <td>${c['attributes']['teilkomp_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.kompartimente-luchse.teilkomp_nr')}</td>      <td>${c['attributes']['teilkomp_nr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.kompartimente-luchs.geom_area')}</td>        <td>${c['attributes']['geom_area'] or '-'}</td></tr>
</%def>

