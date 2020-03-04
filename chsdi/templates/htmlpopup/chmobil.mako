<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<%
    lang = lang if lang in ('de','fr','it','en') else 'de'
    url = None
    msgid_route = "chmobil_title"
    if c['layerBodId'] == 'ch.swisstopo.schneeschuhwandern':
        url = 'http://www.schweizmobil.ch/%s/schneeschuhwandern' % (lang)
        msgid_route = "ch.swisstopo.schneeschuhwandern.attribut_c"
    if c['layerBodId'] == 'ch.astra.mountainbikeland':
        url = 'http://www.mountainbikeland.ch/%s' % (lang)
    if c['layerBodId'] == 'ch.astra.wanderland':
        url = 'http://www.wanderland.ch/%s' % (lang)
    if c['layerBodId'] == 'ch.astra.veloland':
        url = 'http://www.veloland.ch/%s' % (lang)
    if c['layerBodId'] == 'ch.astra.skatingland':
        url = 'http://www.skatingland.ch/%s' % (lang)
%>
    <tr><td class="cell-left">${mod_translate.Translator.translate('chmobil_number', lang)}</td>   <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate(msgid_route, lang)}</td>    <td>${c['attributes']['chmobil_title'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('link', lang)}</td>          <td>
    % if url and c['attributes']['chmobil_route_number']:
      <a href="${url}/route${c['attributes']['chmobil_route_number']}" target="_blank" title="${mod_translate.Translator.translate('chmobil_url_route', lang)}">${mod_translate.Translator.translate('chmobil_url_route', lang)}</a>
    % else:
        -
    % endif
    </td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('link', lang)}</td>          <td>
    % if url and c['attributes']['chmobil_has_segment']:
      <a href="${url}/etappe${c['featureId']}" target="_blank" title="${mod_translate.Translator.translate('chmobil_url_route', lang)}">${mod_translate.Translator.translate('chmobil_url_etappe', lang)}</a>
    % else:
        -
    % endif
    </td></tr>
</%def>
