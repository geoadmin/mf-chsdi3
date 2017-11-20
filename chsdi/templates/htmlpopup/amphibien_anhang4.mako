<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien_anhang4.objnummer')}</td>          <td>${c['attributes']['obnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien_anhang4.name')}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-amphibien_anhang4.refobjblat')}</td>        <td><a target ="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

