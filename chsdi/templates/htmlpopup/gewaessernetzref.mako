<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = 'fr' if lang == 'it' else lang
    lang = 'de' if lang != 'fr' else lang
    objectval = 'objectval_%s' % lang

%>

    <tr><td class="cell-left">${_('ch.swisstopo.vec25-gewaessernetz_referenz.name')}</td>                <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.vec25-gewaessernetz_referenz.gewissnr')}</td>            <td>${c['attributes']['gewissnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.vec25-gewaessernetz_referenz.gwlnr')}</td>               <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.vec25-gewaessernetz_referenz.objectval')}</td>           <td>${c['attributes'][objectval] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.vec25-gewaessernetz_referenz.objectid')}</td>            <td>${c['attributes']['objectid'] or '-'}</td></tr>
</%def>
