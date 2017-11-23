<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    lang = lang if lang in ('fr','it') else 'de'
    auen_typ = 'auen_type_%s' %lang
    %>


    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_anhang2.objnummer')}</td>       <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_anhang2.name')}</td>           <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_anhang2.type')}</td>            <td>${c['attributes'][auen_typ] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_anhang2.area')}</td>     <td>${round(c['attributes']['shape_area']/10000, 1) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_anhang2.refobjblatt')}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

