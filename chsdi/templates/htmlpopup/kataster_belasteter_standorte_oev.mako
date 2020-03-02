<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr', 'it') else 'de'
    standorttyp = 'standorttyp_%s' % lang
    statusaltlv = 'statusaltlv_%s' % lang
    untersuchungsstand = 'untersuchungsstand_%s' % lang
    arr_untersuchungsstand = c['attributes'][untersuchungsstand].split('##')
    arr_len = len(arr_untersuchungsstand)
    str_output = ''
    for i in range(arr_len):
        str_output = str_output + arr_untersuchungsstand[i] + '<br />' if  i < (arr_len-1) else str_output + arr_untersuchungsstand[i]
    endfor

%>

    <tr><td class="cell-left">${t.Translator.translate('ch.bav.kataster-belasteter-standorte-oev.katasternummer', lang)}</td>           <td>${c['attributes']['katasternummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch_bav_kataster_belasteter_standorte_oev_standorttyp', lang)}</td>              <td>${c['attributes'][standorttyp] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch_bav_kataster_belasteter_standorte_oev_beurteilung', lang)}</td>              <td>${c['attributes'][statusaltlv] or '-'}</td></tr>
    <tr><td class="cell-left" valign="top">${t.Translator.translate('tt_ch_bav_kataster_belasteter_standorte_oev_untersuchungsstand_2', lang)}</td>     <td>${_(str_output)|n}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch_bav_kataster_belasteter_standorte_oev_beschreibung', lang)}</td>             <td><a href="${c['attributes']['url'] or '-'}" target="_blank">${t.Translator.translate('tt_ch_bav_kataster_belasteter_standorte_oev_katasterauszug', lang)}</a></td></tr>
    <tr><td>&nbsp;</td>                                                                                         <td>&nbsp;</td></tr>
</%def>
