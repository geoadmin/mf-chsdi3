<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<%
badewasserqualitaet_eua = 'ch.bafu.gewaesserschutz-badewasserqualitaet.%s' % c['attributes']['qualitaet_eua']
%>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.bwid', lang)}</td>
      <td>${c['featureId']}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.bwname', lang)}</td>
      <td>${c['attributes']['bwname']}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.groupid', lang)}</td>
      <td>${c['attributes']['groupid'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.nwunitname', lang)}</td>
      <td>${c['attributes']['nwunitname'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.gemeinde', lang)}</td>
      <td>${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.qualitaet_eua', lang)}</td>
      <td>${_(badewasserqualitaet_eua)}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.anzahlmessungen', lang)}</td>
      <td>${c['attributes']['anzahlmessungen'] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
<%
badewasserqualitaet_eua = 'ch.bafu.gewaesserschutz-badewasserqualitaet.%s' % c['attributes']['qualitaet_eua']
protocol = request.scheme
c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
datageoadminUrl = 'https://' + request.registry.settings['datageoadminhost'] + '/ch.bafu.gewaesserschutz-badewasserqualitaet/image/'
topic = request.matchdict.get('map')
lang = request.lang
%>
<table class="table-with-border  kernkraftwerke-extended">
  <tr>
% if c['attributes']['baquaimg'] is None:
      <span></span>
% else:
      <div><center><img style="width: 70%; height:auto" src="${datageoadminUrl + c['attributes']['baquaimg'] or '-'}"/></center></div><br/>
% endif
  </tr>
  <tr>
      <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.bwid', lang)}</td>
      <td class="cell-meta">${c['featureId']}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.bwname', lang)}</td>
    <td class="cell-meta">${c['attributes']['bwname'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.groupid', lang)}</td>
    <td class="cell-meta">${c['attributes']['groupid'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.nwunitname', lang)}</td>
    <td class="cell-meta">${c['attributes']['nwunitname']}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.rbdsuname', lang)}</td>
    <td class="cell-meta">${c['attributes']['rbdsuname'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.gemeinde', lang)}</td>
    <td class="cell-meta">${c['attributes']['gemeinde'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.kanton', lang)}</td>
    <td class="cell-meta">${c['attributes']['canton'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.bwatercat', lang)}</td>
% if c['attributes']['bwatercat'] == 'L':
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.bwatercat_l', lang)}</td>
% elif c['attributes']['bwatercat'] == 'R':
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.bwatercat_r', lang)}</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.yearbw', lang)}</td>
    <td class="cell-meta">${c['attributes']['yearbw'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.coord_ch', lang)}</td>
    <td class="cell-meta">${c['attributes']['coord_ch'] or '-'}</td>
  </tr>
    <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.url', lang)}</td>
% if c['attributes']['url']:
    <td class="cell-meta"><a href="${c['attributes']['url'] or '-'}" target="_blank">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.urllien', lang)}</a></td>
% else:
    <td class="cell-meta">-</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.eua_badeplatz', lang)}</td>
% if c['attributes']['eua_badeplatz'] == 1:
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.eua_badeplatz_ja', lang)}</td>
% elif c['attributes']['eua_badeplatz'] == 0:
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.eua_badeplatz_nein', lang)}</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.anzahlmessungen', lang)}</td>
    <td class="cell-meta">${c['attributes']['anzahlmessungen'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.verunreinigung_tage', lang)}</td>
    <td class="cell-meta">${c['attributes']['verunreinigung_tage'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.qualitaet_eua', lang)}</td>
    <td class="cell-meta">${_(badewasserqualitaet_eua)}</td>
  </tr>
</table>
<br />
<div>
 <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
</div>
</%def>
