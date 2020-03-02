<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${t.Translator.translate('flaeche_m2', lang)}</td><td>${int(round(c['attributes']['area'])) or '-'} m2</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('perimeter_m', lang)}</td>    <td>${int(round(c['attributes']['perimeter'])) or '-'} m</td></tr>
</%def>
