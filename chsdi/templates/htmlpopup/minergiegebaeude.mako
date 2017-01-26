<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == 'de':
        info = c['attributes']['buildinginfo_de']
        http = c['attributes']['http_de']
    elif lang == 'fr':
        info = c['attributes']['buildinginfo_fr']
        http = c['attributes']['http_fr']
    elif lang == 'it':
        info == c['attributes']['buildinginfo_it']
        http = c['attributes']['http_it']
    elif lang == 'en':
        info == c['attributes']['buildinginfo_en']
        http = c['attributes']['http_en']
%>
    <% c['stable_id'] = True %>
    <tr><td class="cell-left-large">${_('ch.bfe.minergiegebaeude.zertifikat')}</td><td>${c['attributes']['certificate'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${_('ch.bfe.minergiegebaeude.standard')}</td><td>${c['attributes']['standard'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${_('ch.bfe.minergiegebaeude.adresse')}</td><td>${c['attributes']['street'] or '-'}&nbsp;${c['attributes']['streetnr'] or '-'}</td></tr>
    <tr><td class="cell-left-large">&nbsp;</td><td>${c['attributes']['postcode'] or '-'}&nbsp;${c['attributes']['place'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${_('ch.bfe.minergiegebaeude.kanton')}</td><td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left-large">${_('ch.bfe.minergiegebaeude.gebaeude')}&nbsp;(${_('ch.bfe.minergiegebaeude.energiebezugsflaeche')}&nbsp;m<sup>2</sup>)</td><td>${info}&nbsp;(${c['attributes']['ebf'] or '-'}&nbsp;m<sup>2</sup>)</td></tr>
    <tr><td class="cell-left-large">${_('ch.bfe.minergiegebaeude.weitere_informationen')}</td><td><a href="${http}" target="_blank">${_('ch.bfe.minergiegebaeude')}</a></td></tr>

</%def>
