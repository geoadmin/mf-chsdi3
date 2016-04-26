<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<% 
c['stable_id'] = True 
status = '%s_%s' % ('status',c['attributes']['status'])
kategorie = '%s_%s' % ('kategorie',c['attributes']['kategorie'])
rechtsgrundlage = '%s_%s' % ('rechtsgrundlage',c['attributes']['rechtsgrundlage'])
%>
    <tr><td class="cell-left">${_('name')}</td>                 <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('objnummer')}</td>            <td>${c['featureId'] or '-'}</td>
    <tr><td class="cell-left">${_('status')}</td>               <td>${_(status)}</td></tr>
    <tr><td class="cell-left">${_('kategorie')}</td>            <td>${_(kategorie)}</td></tr>
    <tr><td class="cell-left">${_('rechtsgrundlage')}</td>      <td>${_(rechtsgrundlage)}</td></tr>
</%def>
