<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    import datetime
    lang = lang if lang in ('fr','it','de') else 'de'
%>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.title')}</td>         <td>${c['attributes']['title']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.acquisition_date')}</td>         <td>${c['attributes']['acquisition_date']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.abstract')}</td>         <td>${c['attributes']['abstract']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.filename')}</td>         <td>${c['attributes']['filename']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.first_publication')}</td>         <td>${c['attributes']['first_publication']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.link_to_event')}</td>
        <td>
            <a href="${c['attributes']['link_to_event']}" target="_blank">Link</a>
        </td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.link_to_viewer')}</td>
        <td>
            ${' | '.join('<a href="%s" target="_blank">Link</a>' % link for link in c['attributes']['link_to_viewer']) or '-' | n}
        </td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.rapidmapping.downloads')}</td>
        <td>
            <a href="${c['attributes']['link_to_data']}" target="_blank">Event index</a> | 
            <a href="${c['attributes']['download_img']}" target="_blank">.tif</a> | 
            <a href="${c['attributes']['download_tfw']}" target="_blank">.tfw</a> | 
            <a href="${c['attributes']['download_ovr']}" target="_blank">.ovr</a>
        </td>
    </tr>
</%def>
