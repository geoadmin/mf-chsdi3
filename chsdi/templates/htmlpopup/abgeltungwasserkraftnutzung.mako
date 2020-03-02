<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% c['stable_id'] = True %>
    <tr><td class="cell-left">${Translator.translate('ch.bfe.abgeltung-wasserkraftnutzung.name', lang)}</td>                        <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.abgeltung-wasserkraftnutzung_objectnumber', lang)}</td>                <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.abgeltung-wasserkraftnutzung_area', lang)}</td>                        <td>${c['attributes']['area'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.abgeltung-wasserkraftnutzung_perimeter', lang)}</td>                   <td>${c['attributes']['perimeter'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.abgeltung-wasserkraftnutzung_startprotectioncommitment', lang)}</td>   <td>${h.parse_date_string(c['attributes']['startprotectioncommitment'])}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bfe.abgeltung-wasserkraftnutzung_endprotectioncommitment', lang)}</td>     <td>${h.parse_date_string(c['attributes']['endprotectioncommitment'])}</td></tr>
</%def>
