<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    noisebarriertype = 'noisebarriertype_%s' % lang
    material = 'material_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_laermschutzwaende.noisebarrierheight')}</td>             <td>${c['attributes']['noisebarrierheight'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_laermschutzwaende.height_above_track')}</td>             <td>${c['attributes']['height_above_track'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_laermschutzwaende.noisebarriertype')}</td>               <td>${c['attributes'][noisebarriertype] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_laermschutzwaende.material')}</td>                       <td>${c['attributes'][material] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_laermschutzwaende.has_glass')}</td>                      <td>${c['attributes']['has_glass'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_laermschutzwaende.year_construction')}</td>              <td>${c['attributes']['year_construction'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.laermbelastung-eisenbahn_laermschutzwaende.year_legal')}</td>                     <td>${c['attributes']['year_leagal'] or '-'}</td></tr>
</%def>
