<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.owner')}</td><td>${c['attributes']['owner'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.status')}</td><td>${c['attributes']['status'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.system')}</td><td>${c['attributes']['system'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.use')}</td><td>${c['attributes']['use'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c,lang)">
<table class="table-with-border tiefengeothermie_projekte-extended">

   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.name')}</th><td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.owner')}</th><td>${c['attributes']['owner'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.status')}</th><td>${c['attributes']['status'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.system')}</th><td>${c['attributes']['system'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.use')}</th><td>${c['attributes']['use'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.canton')}</th><td>${c['attributes']['canton'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.community')}</th><td>${c['attributes']['community'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.depth')}</th><td>${c['attributes']['depth'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.temp')}</th><td>${c['attributes']['temp'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.power')}</th><td>${c['attributes']['power'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.produc')}</th><td>${c['attributes']['produc'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.weblink')}</th><td><a href="${c['attributes']['weblink']}" target="_blank">Link</a></td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.id_project')}</th><td>${c['attributes']['id_project'] or '-'}</td></tr>
</table>
</%def>
