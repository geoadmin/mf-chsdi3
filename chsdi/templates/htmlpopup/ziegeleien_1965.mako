<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-geotechnik-ziegeleien_1965.ziegelei', lang)}</td><td>${c['attributes']['ziegelei'] or '-'}</td></tr>
</%def>
