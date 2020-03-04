<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.radio-fernsehsender.name', lang)}</td>      <td>${c['attributes']['name']}</td></tr>
  <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bakom.radio-fernsehsender.code', lang)}</td>      <td>${c['attributes']['code'] or '-'}</td></tr>
  <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bakom.leistung', lang)}</td>                      <td>${c['attributes']['power'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">

<%
service = c['attributes']['service'].split(',')
program = c['attributes']['program'].split(',')
freqchan = c['attributes']['freqchan'].split(',')
i = 0
%>

<table>
  <tr>
    <td class="cell-meta-one" colspan="2">
      <h1>${c['attributes']['name'] or '-'}</h1>
    </td>
  </tr>
  <tr>
    <td class="cell-meta">
      ${mod_translate.Translator.translate('tt_ch.bakom.radio-fernsehsender_code', lang)}
    </td>
    <td class="cell-meta">
      ${c['attributes']['code'] or '-'}
    </td>
  </tr>
  <tr>
    <td class="cell-meta">
      ${mod_translate.Translator.translate('tt_ch.bakom.leistung', lang)}
    </td>
    <td class="cell-meta">
      ${c['attributes']['power'] or '-'}
    </td>
  </tr>
</table>
</br>
<table class="table-with-border">
  <tr>
    <th>${mod_translate.Translator.translate('tt_service', lang)}</th>
    <th>${mod_translate.Translator.translate('tt_program', lang)}</th>
    <th>${mod_translate.Translator.translate('tt_freqchan', lang)}</th>
  </tr>
% while i < len(service):
  <tr>
    <td class="cell-left">
      ${service[i] or '-'}
    </td>
    <td class="cell-left">
      ${program[i] or '-'}
    </td>
    <td class="cell-left">
      ${freqchan[i] or '-'}
    </td>
  </tr>
<%
i += 1
%>
% endwhile
</table>
</br>
</%def>
