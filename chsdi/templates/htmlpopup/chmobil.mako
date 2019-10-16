<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<%
    lang = lang if lang in ('de','fr','it','en') else 'de'
    url = None
    if c['layerBodId'] == 'ch.swisstopo.schneeschuhwandern':
        url = 'http://www.schweizmobil.ch/%s/schneeschuhwandern' % (lang)
    if c['layerBodId'] == 'ch.swisstopo.mountainbikeland':
        url = 'http://www.mountainbikeland.ch/%s' % (lang)
    if c['layerBodId'] == 'ch.swisstopo.wanderland':
        url = 'http://www.wanderland.ch/%s' % (lang)
    if c['layerBodId'] == 'ch.swisstopo.veloland':
        url = 'http://www.veloland.ch/%s' % (lang)
    if c['layerBodId'] == 'ch.swisstopo.skatingland':
        url = 'http://www.skatingland.ch/%s' % (lang)
%>
    <tr><td class="cell-left">${_('chmobil_number')}</td>   <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('chmobil_title')}</td>    <td>${c['attributes']['chmobil_title'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('link')}</td>          <td>
    % if url and c['attributes']['chmobil_route_number']:
      <a href="${url}/route${c['attributes']['chmobil_route_number']}" target="_blank" title="${_('chmobil_url_route')}">${_('chmobil_url_route')}</a>
    % else:
        -
    % endif
    </td></tr>
    <tr><td class="cell-left">${_('link')}</td>          <td>
    % if url and c['attributes']['chmobil_has_segment']:
      <a href="${url}/etappe${c['featureId']}" target="_blank" title="${_('chmobil_url_route')}">${_('chmobil_url_etappe')}</a>
    % else:
        -
    % endif
    </td></tr>
</%def>
