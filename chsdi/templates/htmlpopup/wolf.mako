<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bafu.kompartimente-wolf.name')}</td>    <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.kompartimente-wolf.nummer')}</td>      <td>${c['attributes']['nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.kompartimente-wolf.geom_area')}</td>        <td>${c['attributes']['geom_area'] or '-'}</td></tr>
</%def>
