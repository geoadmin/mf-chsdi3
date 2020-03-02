<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geotechnik-ziegeleien_1995.ziegeleien', lang)}</td><td>${c['attributes']['ziegeleien'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.translate('produkt', lang)}</td><td>${c['attributes']['produkt'] or '-'}</td></tr>
</%def>
