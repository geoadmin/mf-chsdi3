<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.ortschaftenverzeichnis_plz.plz')}</td> <td>${c['attributes']['plz'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.ortschaftenverzeichnis_plz.zusziff')}</td> <td>${c['attributes']['zusziff'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.ortschaftenverzeichnis_plz.langtext')}</td> <td>${c['attributes']['langtext']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.ortschaftenverzeichnis_plz.status')}</td> <td>${c['attributes']['status']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo-vd.ortschaftenverzeichnis_plz.modified')}</td> <td>${c['attributes']['modified']}</td></tr>
</%def>
