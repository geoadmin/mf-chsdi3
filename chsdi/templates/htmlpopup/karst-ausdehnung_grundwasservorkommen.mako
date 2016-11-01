<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it','en') else 'de'
    nk_hdyn = 'nk_hdyn_%s' % lang
    nk_type = 'nk_type_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bafu.karst-ausdehnung_grundwasservorkommen.nk_type')}</td>       <td>${c['attributes'][nk_type] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-ausdehnung_grundwasservorkommen.nk_level')}</td>      <td>${c['attributes']['nk_level'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.karst-ausdehnung_grundwasservorkommen.nk_hdyn')}</td>       <td>${c['attributes'][nk_hdyn] or '-'}</td></tr>
</%def>

