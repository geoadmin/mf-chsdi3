<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    ip_type = 'ip_type_%s' % lang
    ip_qclass = 'ip_qclass_%s' % lang
    ip_reg = 'ip_reg_%s' % lang
    ip_exp = 'ip_exp_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_type')}</td>                 <td>${c['attributes'][ip_type] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_name')}</td>                 <td>${c['attributes']['ip_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_qclass')}</td>               <td>${c['attributes'][ip_qclass] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_reg')}</td>                  <td>${c['attributes'][ip_reg] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_exp')}</td>                  <td>${c['attributes'][ip_exp] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_x')}</td>                    <td>${c['attributes']['ip_x'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_y')}</td>                    <td>${c['attributes']['ip_y'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-quellen_schwinden.ip_z')}</td>                    <td>${c['attributes']['ip_z'] or '-'}</td></tr>
</%def>

