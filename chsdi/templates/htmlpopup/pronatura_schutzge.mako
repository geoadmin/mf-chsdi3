<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.vec200-names-namedlocation.id', lang)}</td>   <td>${c['attributes']['nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_kkw_name', lang)}</td>                                  <td>${c['attributes']['name'] or '-'}</td></tr>
</%def>

