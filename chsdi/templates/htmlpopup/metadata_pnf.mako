<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.geometa-periodische_nachfuehrung.canton')}</td>    <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.geometa-periodische_nachfuehrung.description')}</td>    <td>${c['attributes']['description'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.geometa-periodische_nachfuehrung.year')}</td>    <td>${c['attributes']['year'] or '-'}</td></tr>
</%def>
