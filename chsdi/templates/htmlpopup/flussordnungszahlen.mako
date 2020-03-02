<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_abschnr', lang)}</td>      <td>${c['attributes']['arc_id'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.flussordnungszahlen-strahler.strahler', lang)}</td>     <td>${c['attributes']['floz'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.flussordnungszahlen-strahler.dist_source', lang)}</td>  <td>${round(c['attributes']['main_len'],1) or '-'}</td></tr>
</%def>
