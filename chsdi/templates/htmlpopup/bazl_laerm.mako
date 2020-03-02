<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bazl.laermbelastungskataster.registername', lang)}</td>          <td>${c['attributes']['noisepollutionregister_registername']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bazl.laermbelastungskataster.editor', lang)}</td>                <td>${c['attributes']['noisepollutionregister_editor'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bazl.laermbelastungskataster.validfrom', lang)}</td>             <td>${c['attributes']['noisepollutionregister_validity_validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bazl.laermbelastungskataster.exposuretype', lang)}</td>          <td>${c['attributes']['exposuregroup_exposuretype'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bazl.laermbelastungskataster.level_db', lang)}</td>              <td>${c['attributes']['exposurecurve_level_db'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bazl.laermbelastungskataster.documentlink')}</td>          <td><a href="${c['attributes']['noisepollutionregister_documentlink'] or '-'}" target="_blank">${_('tt_ch.bazl.laermbelastungskataster.documentlink', lang)}</a></td></tr>
</%def>
