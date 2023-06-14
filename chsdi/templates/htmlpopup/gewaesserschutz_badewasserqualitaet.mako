<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    % if c['attributes']['kategorie'] == 'See':
        klasse_txt = 'ch.bafu.gewaesserschutz-badewasserqualitaet.l%s' % c['attributes']['klasse']
    % elif c['attributes']['kategorie'] == 'Fluss':
        klasse_txt = 'ch.bafu.gewaesserschutz-badewasserqualitaet.r%s' % c['attributes']['klasse']
    % endif
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.id')}</td>
      <td>${c['featureId']}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.station')}</td>
      <td>${c['attributes']['station']}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gruppe')}</td>
      <td>${c['attributes']['gruppe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gewaesser')}</td>
      <td>${c['attributes']['gewaesser'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gemeinde')}</td>
      <td>${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.klasse')}</td>
      <td>${_(klasse_txt)}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
  % if c['attributes']['kategorie'] == 'See':
      klasse_txt = 'ch.bafu.gewaesserschutz-badewasserqualitaet.l%s' % c['attributes']['klasse']
  % elif c['attributes']['kategorie'] == 'Fluss':
      klasse_txt = 'ch.bafu.gewaesserschutz-badewasserqualitaet.r%s' % c['attributes']['klasse']
  % endif
  <%
    protocol = request.scheme
    c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
    datageoadminUrl = request.registry.settings['datageoadminhost'] + '/ch.bafu.gewaesserschutz-badewasserqualitaet/image/'
    topic = request.matchdict.get('map')
    lang = request.lang
  %>
  <table class="table-with-border  kernkraftwerke-extended">
    <tr>
      % if c['attributes']['foto'] is None:
            <span></span>
      % else:
            <div><center><img style="width: 70%; height:auto" src="${datageoadminUrl + c['attributes']['foto'] or '-'}"/></center></div><br/>
      % endif
    </tr>
    <tr>
        <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.id')}</td>
        <td class="cell-meta">${c['featureId']}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.station')}</td>
      <td class="cell-meta">${c['attributes']['station'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gruppe')}</td>
      <td class="cell-meta">${c['attributes']['gruppe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gewaesser')}</td>
      <td class="cell-meta">${c['attributes']['gewaesser']}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.gemeinde')}</td>
      <td class="cell-meta">${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.kanton')}</td>
      <td class="cell-meta">${c['attributes']['kanton'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.kategorie')}</td>
      <td class="cell-meta">${c['attributes']['kategorie'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.jahr')}</td>
      <td class="cell-meta">${c['attributes']['jahr'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.link')}</td>
      % if c['attributes']['link']:
          <td class="cell-meta"><a href="${c['attributes']['link'] or '-'}" target="_blank">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.urllien')}</a></td>
      % else:
          <td class="cell-meta">-</td>
      % endif
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.klasse')}</td>
      <td class="cell-meta">${_(klasse_txt)}</td>
    </tr>
  </table>
  <br />
  <div>
    <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
  </div>
</%def>
