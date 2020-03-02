<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${t.Translator.translate('ch.vbs.logistikraeume-armeelogistikcenter.kanton', lang)}</td>
    <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.vbs.logistikraeume-armeelogistikcenter.region', lang)}</td>
    <td>${c['attributes']['region'] or '-'}</td></tr>
</%def>

