<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-geotechnik-ziegeleien_1907.ziegelei_2', lang)}</td><td>${c['attributes']['ziegelei_2'] or '-'}</td></tr>
</%def>
