<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    nummer = c['layerBodId'] + '.' + 'id'
%>
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_(nummer)}</td>             <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${_('name')}</td>             <td>${c['attributes']['punktname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('fp_E95_N95')}</td>       <td>${'{0:.3f}'.format(c['attributes']['e95']) or '-'} / ${'{0:.3f}'.format(c['attributes']['n95']) or '-'}</td></tr>
    <tr><td class="cell-left">${_('fp_H02_fida')}</td>      <td>${'{0:.3f}'.format(c['attributes']['h02']) if c['attributes']['h02'] is not None else '-'}</td></tr>
    <tr><td class="cell-left">${_('protokoll')}</td>        <td><a href="${c['attributes']['proto_url'] or '-'}" target="_blank">${_('protokoll')}</a></td></tr>
</%def>
