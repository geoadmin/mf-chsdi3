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
      <td class="cell-left">${Translator.translate('ch.bafu.hydrologie-hochwasserstatistik.name', lang)}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${Translator.translate('ch.bafu.hydrologie-hochwasserstatistik.url', lang)}</td>
      <td><a href="${c['attributes']['url_hqpdf'] or '-'}" target="_blank">${Translator.translate('ch.bafu.hydrologie-hochwasserstatistik.pdf', lang)}</a></td>
    </tr>
    <tr>
      <td class="cell-left">${Translator.translate('ch.bafu.hydrologie-hochwasserstatistik.urlpdf', lang)}</td>
      <td><a href="${c['attributes'][url] or '-'}" target="_blank">${Translator.translate('ch.bafu.hydrologie-hochwasserstatistik.link', lang)}</a></td>
    </tr>
</%def>
