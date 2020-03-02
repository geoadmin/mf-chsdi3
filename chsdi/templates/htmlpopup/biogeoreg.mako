<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('datumactu', lang)}</td>    <td>${c['attributes']['biogreg_ve'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('bioregname', lang)}</td>    <td>${c['attributes']['biogreg_r6'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('biounterregname', lang)}</td>    <td>${c['attributes']['biogreg_r1'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('bioregnummer', lang)}</td>    <td>${c['attributes']['biogreg_c6'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('biounterregnummer', lang)}</td>    <td>${c['attributes']['biogreg_c1'] or '-'}</td></tr>
</%def>

