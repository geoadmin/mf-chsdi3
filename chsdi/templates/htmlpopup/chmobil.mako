<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<%
    lang = lang if lang in ('de','fr','it','en') else 'de'
%>
    <tr><td class="cell-left">${_('chmobil_number')}</td>   <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('chmobil_title')}</td>    <td>${c['attributes']['chmobil_title'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('link')}</td>          <td>
    % if c['attributes']['chmobil_url_route']:
      <a href="${c['attributes']['chmobil_url_route']}${lang}/route${c['attributes']['chmobil_route_number']}" target="_blank" title="${_('chmobil_url_route')}">${_('chmobil_url_route')}</a>
    % else:
        -
    % endif
    </td></tr>
    <tr><td class="cell-left">${_('link')}</td>          <td>
    % if c['attributes']['chmobil_url_etappe']:
      <a href="${c['attributes']['chmobil_url_etappe']}${lang}/etappe${c['featureId']}" target="_blank" title="${_('chmobil_url_route')}">${_('chmobil_url_etappe')}</a>
    % else:
        -
    % endif
    </td></tr>
</%def>
