<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${_('ch.bafu.grundwasserkoerper.gwkid')}</td>                                                 <td>${c['attributes']['gwkid'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.grundwasserkoerper.gwkname')}</td>                                               <td>${c['attributes']['gwkname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.grundwasserkoerper.flussgebiet')}</td>                                           <td>${c['attributes']['flussgebiet'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.grundwasserkoerper.grundwasserleitertyp')}</td>                                  <td>${c['attributes']['grundwasserleitertyp'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.grundwasserkoerper.naturraum')}</td>                                             <td>${c['attributes']['naturraum'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.grundwasserkoerper.grundwasserregime')}</td>                                     <td>${c['attributes']['grundwasserregime'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.grundwasserkoerper.area')}</td>                                                  <td>${c['attributes']['area'] or '-'}</td></tr>

</%def>

