<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${t.Translator.translate('identificator', lang)}</td><td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('optionaler_name', lang)}</td><td>${c['attributes']['sg_name']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('validierungsdatum', lang)}</td><td>${c['attributes']['vali_date'] or '-'}</td></tr>
</%def>

