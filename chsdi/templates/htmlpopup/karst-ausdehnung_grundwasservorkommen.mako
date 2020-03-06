<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it','en') else 'de'
    nk_hdyn = 'nk_hdyn_%s' % lang
    nk_type = 'nk_type_%s' % lang
%>
    <tr><td class="cell-left">${h.translate('ch.bafu.karst-ausdehnung_grundwasservorkommen.nk_type', lang)}</td>       <td>${c['attributes'][nk_type] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.karst-ausdehnung_grundwasservorkommen.nk_level', lang)}</td>      <td>${c['attributes']['nk_level'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.karst-ausdehnung_grundwasservorkommen.nk_hdyn', lang)}</td>       <td>${c['attributes'][nk_hdyn] or '-'}</td></tr>
</%def>

