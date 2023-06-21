<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
      c['stable_id'] = True 
      qualitaet_txt = 'ch.bafu.gewaesserschutz-badewasserqualitaet.%s' % c['attributes']['qualitaet']
    %>
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
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.qualitaet')}</td>
      <td>${_(qualitaet_txt)}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
    <%
      c['stable_id'] = True 
      qualitaet_txt = 'ch.bafu.gewaesserschutz-badewasserqualitaet.%s' % c['attributes']['qualitaet']
    %>

  <%
    protocol = request.scheme
    c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
    datageoadminUrl = request.registry.settings['datageoadminhost'] + '/ch.bafu.gewaesserschutz-badewasserqualitaet/image/'
    topic = request.matchdict.get('map')
    lang = request.lang
  %>

  <table class="table-with-border  kernkraftwerke-extended">
    <tr>
      % if c['attributes']['baquaimg'] is None:
            <span></span>
      % else:
            <div><center><img style="width: 70%; height:auto" src="${c['attributes']['baquaimg']}"/></center></div><br/>
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
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gemeinde')}</td>
      <td class="cell-meta">${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.canton')}</td>
      <td class="cell-meta">${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.bwatercat')}</td>
      <td class="cell-meta">${c['attributes']['bwatercat'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.year_bw')}</td>
      <td class="cell-meta">${c['attributes']['year_bw'] or '-'}</td>
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
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.qualitaet')}</td>
      <td class="cell-meta">${_(qualitaet_txt)}</td>
    </tr>
  </table>
  <br />
  <div>
    <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
  </div>
</%def>
