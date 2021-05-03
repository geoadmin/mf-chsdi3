<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    massnahme = 'massnahme_%s' % lang
    typ = 'type_%s' % lang
%>
    <tr><td class="cell-left">${_(c['layerBodId']+'.nr_datenbank')}</td>    <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.nr_kanton')}</td>       <td>${c['attributes']['nr_kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.name')}</td>            <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.type')}</td>            <td>${c['attributes'][typ] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId']+'.massnahme')}</td>       <td>${c['attributes'][massnahme] or '-'}</td></tr>
    <tr><td class="cell-left">${_('link')}</td>                           <td><a target ="_blank" href="${c['attributes']['ref_datenblatt']}">${_('link') or '-'}</a></td></tr>
</%def>
