<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.post_title')}</td>                              <td>${c['attributes']['post_title'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.allgemein_leadtext')}</td>                      <td>${c['attributes']['allgemein_leadtext'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.treffpunkt_gemeinde')}</td>                     <td>${c['attributes']['treffpunkt_gemeinde'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.treffpunkt_kanton')}</td>                       <td>${c['attributes']['treffpunkt_kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.kontakt_firma')}</td>                           <td>${c['attributes']['kontakt_firma'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geowege.post_permalink')}</td>                          <td><a href="${c['attributes']['post_permalink'] or '-'}" target="_blank">Link</a></td></tr>
</%def>

