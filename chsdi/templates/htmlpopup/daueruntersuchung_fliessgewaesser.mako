<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == ('de') :
        url = 'hyperlink_d'
    elif lang == ('fr') :
        url = 'hyperlink_f'
    elif lang == ('it') :
        url = 'hyperlink_f'
    elif lang == ('en') :
        url = 'hyperlink_d'
    else :
        url = 'hyperlink_d'
%>
<style>
.cell-left {
  width: 200px !important; 
}
</style>
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.name', lang)}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.betriebsbeginn', lang)}</td>
      <td>${c['attributes']['betriebsbeginn'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.stationierung', lang)}</td>
      <td>${c['attributes']['stationierung'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.flussgebiet', lang)}</td>
      <td>${c['attributes']['flussgebiet'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.einzugsgebietsflaeche', lang)}</td>
      <td>${c['attributes']['einzugsgebietsflaeche'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hyperlink_name', lang)}</td>
      <td><a href="${c['attributes'][url] or '-'}" target="_blank">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hyperlink', lang)}</a></td>
    </tr>
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hyperlink_daten', lang)}</td>
      <td><a href="${c['attributes']['hyperlink_daten'] or '-'}" target="_blank">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.xls', lang)}</a></td>
    </tr>
</%def>


<%def name="extended_info(c, lang)">
<%
    if lang == ('de') :
        url = 'hyperlink_d'
    elif lang == ('fr') :
        url = 'hyperlink_f'
    elif lang == ('it') :
        url = 'hyperlink_f'
    elif lang == ('en') :
        url = 'hyperlink_d'
    else :
        url = 'hyperlink_d'
%>

<table>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.name', lang)}</td>
    <td class="cell-meta">${c['attributes']['name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.betriebsbeginn', lang)}</td>
    <td class="cell-meta">${c['attributes']['betriebsbeginn'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.stationierung', lang)}</td>
    <td class="cell-meta">${c['attributes']['stationierung'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.flussgebiet', lang)}</td>
    <td class="cell-meta">${c['attributes']['flussgebiet'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.einzugsgebietsflaeche', lang)}</td>
    <td class="cell-meta">${c['attributes']['einzugsgebietsflaeche'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.rechtswert', lang)}</td>
    <td class="cell-meta">${c['attributes']['rechtswert'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hochwert', lang)}</td>
    <td class="cell-meta">${c['attributes']['hochwert'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.mittlerehoehe', lang)}</td>
    <td class="cell-meta">${c['attributes']['mittlerehoehe'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hoehe', lang)}</td>
    <td class="cell-meta">${c['attributes']['hoehe'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.vergletscherung', lang)}</td>
    <td class="cell-meta">${c['attributes']['vergletscherung'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hyperlink_name', lang)}</td>
    <td class="cell-meta"><a href="${c['attributes'][url] or '-'}" target="_blank">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hyperlink', lang)}</a></td>
  </tr>
  <tr>
    <td class="cell-meta">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.hyperlink_daten', lang)}</td>
    <td class="cell-meta"><a href="${c['attributes']['hyperlink_daten'] or '-'}" target="_blank">${mod_translate.Translator.translate('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser.xls', lang)}</a></td>
  </tr>
</table>
</%def>
