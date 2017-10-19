<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    description = 'description_%s' % lang
    type = 'type_%s' % lang
%>

    <tr><td class="cell-left">${_('objektname')}</td>         <td>${c['attributes']['hm_name']}</td></tr>
    <tr><td class="cell-left">${_('objektnr')}</td>           <td>${c['attributes']['hm_obj'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('typ')}</td>                <td>${c['attributes'][type] or '-'}</td></tr>
    <tr><td class="cell-left">${_('flaeche_ha')}</td>         <td>${round(c['attributes']['hm_fl'], 3) or '-'}</td></tr>
    <tr><td class="cell-left">${_('kartiereinheit')}</td>     <td>${c['attributes']['hm_ke'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('description')}</td>        <td>${c['attributes'][description] or '-'}</td></tr>
</%def>
