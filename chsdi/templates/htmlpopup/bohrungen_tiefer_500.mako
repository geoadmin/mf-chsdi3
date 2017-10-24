<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en', 'rm') else 'de'
    auftraggeb = 'auftraggeb_%s' % lang
    rechtein = 'rechtein_%s' % lang
    inhalt = 'inhalt_%s' % lang
    auskunft = 'auskunft_%s' % lang
    download = c['attributes']['download']
%>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</td>       <td>${c['attributes']['name'] or '-'}</td></tr>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auftraggeb_de')}</td>       <td>${c['attributes'][auftraggeb] or '-'}</td></tr>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.rechtein')}</td>       <td>${c['attributes'][rechtein] or '-'}</td></tr>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.inhalt')}</td>       <td>${c['attributes'][inhalt] or '-'}</td></tr>
     % if download != '-':
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</td>       <td><a href="${download}" target="_blank">Link</a></td></tr>
     % else:
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</td>       <td>-</td></tr>
     % endif
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auskunft')}</td>       <td>${c['attributes'][auskunft] or '-'}</td></tr>



</%def>


<%def name="extended_info(c,lang)">
<%
    lang = lang if lang in ('fr','it','en', 'rm') else 'de'
    auftraggeb = 'auftraggeb_%s' % lang
    rechtein = 'rechtein_%s' % lang
    inhalt = 'inhalt_%s' % lang
    auskunft = 'auskunft_%s' % lang
    download = c['attributes']['download']
    bohrzweck = 'bohrzweck_%s' % lang
    status = 'status_%s' % lang
    land = 'land_%s' % lang
    kanton = 'kanton_%s' % lang
    startdate = 'startdate_%s' % lang
    enddate = 'enddate_%s' % lang
%>

<table class="table-with-border bohrungen_tiefer_500-extended">
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</th>       <td>${c['attributes']['name'] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auftraggeb_de')}</th>       <td>${c['attributes'][auftraggeb] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.rechtein')}</th>       <td>${c['attributes'][rechtein] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.inhalt')}</th>       <td>${c['attributes'][inhalt] or '-'}</td></tr>
      % if download != '-':
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</th>       <td><a href="${download}" target="_blank">Link</a></td></tr>
     % else:
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</th>       <td>-</td></tr>
     % endif
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auskunft')}</th>       <td>${c['attributes'][auskunft] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.tiefe_md')}</th><td>${c['attributes']['tiefe_md'] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.bohrzweck')}</th><td>${c['attributes'][bohrzweck] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.status')}</th><td>${c['attributes'][status] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.startdate')}</th><td>${c['attributes'][startdate] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.enddate')}</th><td>${c['attributes'][enddate] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.koord_e')}</th><td>${int(c['attributes']['koord_e'])}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.koord_n')}</th><td>${int(c['attributes']['koord_n'])}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.height')}</th><td>${c['attributes']['height'] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.land')}</th><td>${c['attributes'][land] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.kanton')}</th><td>${c['attributes'][kanton] or '-'}</td></tr>
</table>
</%def>


