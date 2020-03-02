<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('spectralinfolink', lang)}</td>    <td>${c['attributes']['spectral_4'] or '-'|n}</td></tr>
    <tr><td class="cell-left">${t.translate('spectralzone', lang)}</td>        <td>${c['attributes']['spectral_3'] or '-'|n}</td></tr>
</%def>

