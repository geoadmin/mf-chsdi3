<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    unit = 'unit_%s' % lang
    type = 'hochmoore_type_%s' % lang
%>

    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-hochmoore.objnummer')}</td>           <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-hochmoore.name')}</td>         <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-hochmoore.hochmoore_type')}</td>                <td>${c['attributes'][type] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-hochmoore.unit')}</td>     <td>${c['attributes'][unit] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-hochmoore.shape_area')}</td>         <td>${round(c['attributes']['shape_area']/10000, 1) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-hochmoore.refobjblat')}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

