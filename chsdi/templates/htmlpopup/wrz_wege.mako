<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    wegtyp = 'wegtyp_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bafu.wrz-wildruhezonen_portal.typ')}</td>               <td>${c['attributes'][wegtyp] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.wrz-wildruhezonen_portal.einschraenkung')}</td>               <td>${c['attributes']['einschraenkungen'] or '-'}</td></tr>
</%def>

