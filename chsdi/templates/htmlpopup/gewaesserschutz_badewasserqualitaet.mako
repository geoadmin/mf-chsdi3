<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwid')}</td>
      <td>${c['featureId']}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwname')}</td>
      <td>${c['attributes']['bwname']}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.groupid')}</td>
      <td>${c['attributes']['groupid'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.nwunitname')}</td>
      <td>${c['attributes']['nwunitname'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gemeinde')}</td>
      <td>${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.qualitaet_ch')}</td>
      <td>${c['attributes']['qualitaet_ch'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.anzahlmessungen')}</td>
      <td>${c['attributes']['anzahlmessungen'] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
<%
protocol = request.scheme
c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
topic = request.matchdict.get('map')
lang = request.lang
%>
<table class="table-with-border  kernkraftwerke-extended">
  <tr>
% if c['attributes']['baquaimg'] is None:
      <span></span>     
% else:
      <div><center><img style="width: 70%; height:auto" src="${c['attributes']['baquaimg'] or '-'}"/></center></div><br/> 
% endif
  </tr>
  <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwid')}</td>
      <td class="cell-meta">${c['featureId']}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwname')}</td>
    <td class="cell-meta">${c['attributes']['bwname'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.groupid')}</td>
    <td class="cell-meta">${c['attributes']['groupid'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.nwunitname')}</td>
    <td class="cell-meta">${c['attributes']['nwunitname']}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.rbdsuname')}</td>
    <td class="cell-meta">${c['attributes']['rbdsuname'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gemeinde')}</td>
    <td class="cell-meta">${c['attributes']['gemeinde'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.kanton')}</td>
    <td class="cell-meta">${c['attributes']['canton'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwatercat')}</td>
% if c['attributes']['bwatercat'] == 'L':
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwatercat_l')}</td>
% elif c['attributes']['bwatercat'] == 'R':
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwatercat_r')}</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.qualitaet_ch')}</td>
    <td class="cell-meta">${c['attributes']['qualitaet_ch'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.yearbw')}</td>
    <td class="cell-meta">${c['attributes']['yearbw'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.coord_ch')}</td>
    <td class="cell-meta">${c['attributes']['coord_ch'] or '-'}</td>
  </tr>
    <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.url')}</td>
% if c['attributes']['url']:
    <td class="cell-meta"><a href="${c['attributes']['url'] or '-'}" target="_blank">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.urllien')}</a></td>
% else:
    <td class="cell-meta">-</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.eua_badeplatz')}</td>
% if c['attributes']['eua_badeplatz'] == 1:
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.eua_badeplatz_ja')}</td>
% elif c['attributes']['eua_badeplatz'] == 0:
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.eua_badeplatz_nein')}</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.anzahlmessungen')}</td>
    <td class="cell-meta">${c['attributes']['anzahlmessungen'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.verunreinigung_tage')}</td>
    <td class="cell-meta">${c['attributes']['verunreinigung_tage'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.qualitaet_eua')}</td>
    <td class="cell-meta">${c['attributes']['qualitaet_eua'] or '-'}</td>
  </tr>
</table>
<br />
<div>
 <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
</div>
</%def>
