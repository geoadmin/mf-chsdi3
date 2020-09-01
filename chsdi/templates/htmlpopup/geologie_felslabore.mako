<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = {'rm': 'de', 'it': 'fr'}.get(lang, lang)
    description = 'description_%s' % lang
    website = 'website_%s' % lang
    contact = 'contact_%s' % lang
%>

    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.name')}</td>       <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.description')}</td>       <td>${c['attributes'][description] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.operator')}</td>       <td>${c['attributes']['operator'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.time_frame')}</td>       <td>${c['attributes']['time_frame'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.website')}</td>       <td><a href="${c['attributes'][website]}" target="_blank">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.contact')}</td>       <td><a href="${c['attributes'][contact]}" target="_blank">Link</a></td></tr>

</%def>


<%def name="extended_info(c,lang)">

<%
    lang = {'rm': 'de', 'it': 'fr'}.get(lang, lang)
    description = 'description_%s' % lang
    website = 'website_%s' % lang
    contact = 'contact_%s' % lang
    visitor = 'visitor_%s' % lang
    partners = 'partners_%s' % lang
    publ_opr = 'publ_opr_%s' % lang
    publ_tech = 'publ_tech_%s' % lang
%>

<table class="table-with-border geologie-felslabore-extended">
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.name')}</td>       <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.description')}</td>       <td>${c['attributes'][description] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.operator')}</td>       <td>${c['attributes']['operator'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.time_frame')}</td>       <td>${c['attributes']['time_frame'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.website')}</td>       <td><a href="${c['attributes'][website]}" target="_blank">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.contact')}</td>       <td><a href="${c['attributes'][contact]}" target="_blank">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.visitor')}</td>       <td><a href="${c['attributes'][visitor]}" target="_blank">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.partners')}</td>       <td><a href="${c['attributes'][partners]}" target="_blank">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.publ_opr')}</td>       <td><a href="${c['attributes'][publ_opr]}" target="_blank">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.publ_tech')}</td>       <td><a href="${c['attributes'][publ_tech]}" target="_blank">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felslabore.research_data')}</td>       <td>${c['attributes']['research_data'] or '-'}</td></tr>
</table>
</%def>


