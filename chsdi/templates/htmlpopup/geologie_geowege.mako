<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
<%
    arr_post_title = c['attributes']['post_title'].split('###')
    arr_allgemein_leadtext = c['attributes']['allgemein_leadtext'].split('###')
    arr_treffpunkt_gemeinde = c['attributes']['treffpunkt_gemeinde'].split('###')
    arr_treffpunkt_kanton = c['attributes']['treffpunkt_kanton'].split('###')
    arr_kontakt_firma = c['attributes']['kontakt_firma'].split('###')
    arr_kontakt_post_permalink = c['attributes']['post_permalink'].split('###')

%>
% for i in range(len(arr_post_title)):
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.post_title')}</td>                              <td>${arr_post_title[i] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.allgemein_leadtext')}</td>                      <td>${arr_allgemein_leadtext[i] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.treffpunkt_gemeinde')}</td>                     <td>${arr_treffpunkt_gemeinde[i] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.treffpunkt_kanton')}</td>                       <td>${arr_treffpunkt_kanton[i] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.kontakt_firma')}</td>                           <td>${arr_kontakt_firma[i] or '-'}</td></tr>
% if arr_kontakt_post_permalink:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.post_permalink')}</td>                          <td><a href="${arr_kontakt_post_permalink[i]}" target="_blank">Link</a></td></tr>
%endif
% endfor
</%def>

