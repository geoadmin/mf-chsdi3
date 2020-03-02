<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-eiszeit-lgm.ads_name', lang)}</td><td>${c['attributes']['ads_name'] or '-'}</td></tr>
</%def>
