<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <tr><td class="cell-left">${t.translate('ch.bafu.bundesinventare-amphibien_wanderobjekte.objnummer', lang)}</td>         <td>${(c['attributes']['objnummer']) or '-'}</td></tr>
   <tr><td class="cell-left">${t.translate('ch.bafu.bundesinventare-amphibien_wanderobjekte.name', lang)}</td>              <td>${(c['attributes']['name']) or '-'}</td></tr>
   <tr><td class="cell-left">${t.translate('ch.bafu.bundesinventare-amphibien_wanderobjekte.refobjblat', lang)}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>
