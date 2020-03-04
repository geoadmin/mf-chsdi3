<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

   <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.name', lang)}</td><td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.owner', lang)}</td><td>${c['attributes']['owner'] or '-'}</td></tr>
   <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.status', lang)}</td><td>${c['attributes']['status'] or '-'}</td></tr>
   <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.system', lang)}</td><td>${c['attributes']['system'] or '-'}</td></tr>
   <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.use', lang)}</td><td>${c['attributes']['use'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c,lang)">
<table class="table-with-border tiefengeothermie_projekte-extended">

   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.name', lang)}</th><td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.owner', lang)}</th><td>${c['attributes']['owner'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.status', lang)}</th><td>${c['attributes']['status'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.system', lang)}</th><td>${c['attributes']['system'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.use', lang)}</th><td>${c['attributes']['use'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.canton', lang)}</th><td>${c['attributes']['canton'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.community', lang)}</th><td>${c['attributes']['community'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.depth', lang)}</th><td>${c['attributes']['depth'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.reservoir', lang)}</th><td>${c['attributes']['reservoir'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.temp', lang)}</th><td>${c['attributes']['temp'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.power', lang)}</th><td>${c['attributes']['power'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.produc', lang)}</th><td>${c['attributes']['produc'] or '-'}</td></tr>
   <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.download', lang)}</th>
   % if c['attributes']['download'] == None or c['attributes']['download'] == "-":
       <td>-</td>
   % else:
       <td><a href="${c['attributes']['download']}" target="_blank">Zip</a></td>
   % endif
   </tr>
   <%
   weblink = c['attributes']['weblink'].split('; ')
   %>
   <tr>
     <th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-tiefengeothermie_projekte.weblink', lang)}</th>
     % if c['attributes']['weblink'] == None or c['attributes']['weblink'] == "-":
            <td>-</td>
     % else:
        <td>
         %  for i in range(len(weblink)):
            <a href="${weblink[i]}" target="_blank">Link_${i+1}</a>&nbsp;
         %endfor
        </td>
     % endif
   </tr>
</table>
</%def>
