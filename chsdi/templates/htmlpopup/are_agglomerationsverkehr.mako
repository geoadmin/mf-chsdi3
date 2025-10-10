<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.are.agglomerationsverkehr.gem_no')}</td><td>${c['attributes']['gem_no'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.agglomerationsverkehr.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.agglomerationsverkehr.agglo_no')}</td><td>${c['attributes']['agglo_no'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.agglomerationsverkehr.agglo_name')}</td><td>${c['attributes']['agglo_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.agglomerationsverkehr.land')}</td><td>${c['attributes']['land'] or '-'}</td></tr>
</%def>

