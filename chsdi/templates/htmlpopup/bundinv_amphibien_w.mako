<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien_wanderobjekte.objnummer')}</td>         <td>${(c['attributes']['objnummer']) or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien_wanderobjekte.name')}</td>              <td>${(c['attributes']['name']) or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien_wanderobjekte.refobjblat')}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>
