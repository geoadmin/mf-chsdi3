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
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.link_to_event')}</td>         <td>${c['attributes']['link_to_event']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.link_to_data')}</td>         <td>${c['attributes']['link_to_data']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.download_img')}</td>         <td>${c['attributes']['download_img']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.download_tfw')}</td>         <td>${c['attributes']['download_tfw']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.rapidmapping.download_ovr')}</td>         <td>${c['attributes']['download_ovr']}</td></tr>
</%def>
