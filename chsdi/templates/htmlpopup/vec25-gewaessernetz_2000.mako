<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>
    <tr><td class="cell-left">${t.translate('ch.bafu.vec25-gewaessernetz_2000.gwlnr', lang)}</td>       <td>${c['attributes']['gwlnr']}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.vec25-gewaessernetz_2000.gewissnr', lang)}</td>    <td>${c['attributes']['gewissnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.vec25-gewaessernetz_2000.name', lang)}</td>        <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bafu.vec25-gewaessernetz_2000.objectval', lang)}</td>   <td>${c['attributes']['objectval'] or '-'}</td></tr>
</%def>
