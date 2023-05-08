<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<%
    lang = lang if lang in ('de','fr','it','en') else 'de'
    url_base = None
    url_land = _('%s.url_land' % (c['layerBodId']))
    url_route = _('chmobil.url_pfad_route')
    url_etappe = _('chmobil.url_pfad_etappe')
    url_base = "https://schweizmobil.ch/%s/%s" % (lang, url_land)
    etappe_number = int(c['featureId'].split('.')[1])
    msgid_route = "chmobil_title"
%>
    <!-- Für Routen: https://schweizmobil.ch/{Sprache}/{Land}/{route}-{nr}  Bsp:  https://schweizmobil.ch/de/veloland/route-61 -->
    <!-- Für Etappen: https://schweizmobil.ch/{Sprache}/{Land}/{route}{nr}/{etappe}{nr} Bsp: https://schweizmobil.ch/de/veloland/route-61/etappe-1 -->

    <tr><td class="cell-left">${_('chmobil_number')}</td>   <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(msgid_route)}</td>    <td>${c['attributes']['chmobil_title'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('link')}</td>          <td>
    % if url_base and c['attributes']['chmobil_route_number']:
      <a href="${url_base}/${url_route}-${c['attributes']['chmobil_route_number']}" target="_blank" title="${_('chmobil_url_route')}">${_('chmobil_url_route')}</a>
    % else:
        -
    % endif
    </td></tr>
    <tr><td class="cell-left">${_('link')}</td>          <td>
    % if url_base and c['attributes']['chmobil_has_segment']:
      <a href="${url_base}/${url_route}-${c['attributes']['chmobil_route_number']}/${url_etappe}-${etappe_number}" target="_blank" title="${_('chmobil_url_etappe')}">${_('chmobil_url_etappe')}</a>
    % else:
        -
    % endif
    </td></tr>
</%def>
