<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.bafu.karst-einzugsgebiete.ba_name')}</td>                    <td>${c['attributes']['ba_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-einzugsgebiete.ba_surf')}</td>                    <td>${c['attributes']['ba_surf'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-einzugsgebiete.ba_alt_min')}</td>                 <td>${c['attributes']['ba_alt_min'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-einzugsgebiete.ba_alt_moy')}</td>                 <td>${c['attributes']['ba_alt_moy'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-einzugsgebiete.ba_alt_max')}</td>                 <td>${c['attributes']['ba_alt_max'] or '-'}</td></tr>

<%
dataHost = request.registry.settings['datageoadminhost']
dataPath = 'ch.bafu.karst-einzugsgebiete'
url_pdf = '//%s/%s/%s.pdf' % (dataHost, dataPath, c['attributes']['ba_id'])
%>

<tr><td class="cell-left">${_('link2dok')}</td>    <td><a href="${url_pdf}" target="_blank">${c['attributes']['ba_id']}.pdf</a></td></tr>
</%def>

