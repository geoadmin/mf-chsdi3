<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${t.Translator.translate('et_fromatt_ch', lang)}</td><td>${c['attributes']['et_fromatt'] or '-'}</td></tr>
</%def>
