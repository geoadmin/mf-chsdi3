<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True 
    if lang == ('de') : 
        url = 'url_de'
    elif lang == ('fr') : 
        url = 'url_fr'
    elif lang == ('it') : 
        url = 'url_fr'
    elif lang == ('en') :
        url = 'url_de'
    else :
        url = 'url_de' 
%>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-hochwasserstatistik.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-hochwasserstatistik.url')}</td>
      <td><a href="${c['attributes']['url_hqpdf'] or '-'}" target="_blank">${_('ch.bafu.hydrologie-hochwasserstatistik.pdf')}</a></td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-hochwasserstatistik.urlpdf')}</td>
      <td><a href="${c['attributes'][url] or '-'}" target="_blank">${_('ch.bafu.hydrologie-hochwasserstatistik.link')}</a></td>
    </tr>
</%def>
