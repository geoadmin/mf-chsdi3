<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr><td class="cell-left">${_('tt_ch.bakom.radio-fernsehsender_name')}</td>      <td>${c['attributes']['name']}</td></tr>
  <tr><td class="cell-left">${_('tt_ch.bakom.radio-fernsehsender_code')}</td>      <td>${c['attributes']['code'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('tt_ch.bakom.leistung')}</td>                      <td>${c['attributes']['power'] or '-'}</td></tr>
  <tr>
    <td class="cell-left"></td>
    <td><a href="${c['baseUrl']}/${c['instanceId']}/rest/services/all/MapServer/${c['layerBodId']}/${c['featureId']}/extendedHtmlPopup" target="_blank">${_('zusatzinfo')}<img src="http://www.swisstopo.admin.ch/images/ico_extern.gif" /></a></td>
  </tr>
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
      ${_('tt_ch.bakom.radio-fernsehsender_code')}
    </td>
    <td class="cell-meta">
      ${c['attributes']['code'] or '-'}
    </td>
  </tr>
  <tr>
    <td class="cell-meta">
      ${_('tt_ch.bakom.leistung')}
    </td>
    <td class="cell-meta">
      ${c['attributes']['power'] or '-'}
    </td>
  </tr>
</table>
</br>
<table class="table-with-border">
  <tr>
    <th>${_('tt_service')}</th>
    <th>${_('tt_program')}</th>
    <th>${_('tt_freqchan')}</th>
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
