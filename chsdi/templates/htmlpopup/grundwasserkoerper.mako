<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.grundwasserkoerper.gwkid', lang)}</td>                                                 <td>${c['attributes']['gwkid'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.grundwasserkoerper.gwkname', lang)}</td>                                               <td>${c['attributes']['gwkname'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.grundwasserkoerper.flussgebiet', lang)}</td>                                           <td>${c['attributes']['flussgebiet'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.grundwasserkoerper.grundwasserleitertyp', lang)}</td>                                  <td>${c['attributes']['grundwasserleitertyp'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.grundwasserkoerper.naturraum', lang)}</td>                                             <td>${c['attributes']['naturraum'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.grundwasserkoerper.grundwasserregime', lang)}</td>                                     <td>${c['attributes']['grundwasserregime'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.grundwasserkoerper.area', lang)}</td>                                                  <td>${c['attributes']['area'] or '-'}</td></tr>

</%def>

