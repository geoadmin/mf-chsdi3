<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == ('de') :
        url = 'hyperlink_d'
    elif lang == ('fr') :
        url = 'hyperlink_f'
    elif lang == ('it') :
        url = 'hyperlink_f'
    elif lang == ('en') :
        url = 'hyperlink_d'
    else :
        url = 'hyperlink_d'
%>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.flussgebiet')}</td>
      <td>${c['attributes']['flussgebiet'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.rechtswert')}</td>
      <td>${c['attributes']['rechtswert'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.hochwert')}</td>
      <td>${c['attributes']['hochwert'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.hoehe')}</td>
      <td>${c['attributes']['hoehe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.einzugsgebietsflaeche')}</td>
      <td>${c['attributes']['einzugsgebietsflaeche'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.betriebsbeginn')}</td>
      <td>${c['attributes']['betriebsbeginn'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.url')}</td>
      <td><a href="${c['attributes'][url] or '-'}" target="_blank">${_('ch.bafu.hydrologie-untersuchungsgebiete_stationen.url')}</a></td>
    </tr>
</%def>
