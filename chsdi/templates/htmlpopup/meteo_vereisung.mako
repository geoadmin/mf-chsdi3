<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('ch.bfe.meteorologische-vereisung.vereisung', lang)}</td>    <td>${c['attributes']['vereisung']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bfe.meteorologische-vereisung.hoehe', lang)}</td>    <td>${c['attributes']['hoehe']}</td></tr>
</%def>
