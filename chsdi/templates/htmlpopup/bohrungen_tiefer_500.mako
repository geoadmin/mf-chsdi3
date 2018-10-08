<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en', 'rm') else 'de'
    auft = 'auft_%s' % lang
    recht = 'recht_%s' % lang
    inhalt = 'inhalt_%s' % lang
    ausk = 'ausk_%s' % lang
    download = c['attributes']['download']
%>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</td>   <td>${c['attributes']['name'] or '-'}</td></tr>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auftraggeb_de')}</td>   <td>${c['attributes'][auft] or '-'}</td></tr>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.rechtein')}</td> <td>${c['attributes'][recht] or '-'}</td></tr>
     <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.inhalt')}</td>   <td>${c['attributes'][inhalt] or '-'}</td></tr>
%  if c['attributes']['web_link'] != '-':
<%
    weblink = c['attributes']['web_link'].split('##')
%>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link')}</td><td> 
%  for i in range(len(weblink)):
      <a href="${weblink[i]}" target="_blank">Link_${i+1}</a>&nbsp;
%endfor
</td></tr>
% else:
    <tr>
      <td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link')}</td>
      <td> - </td>
    </tr>
%endif
% if download != '-':
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</td>  <td><a href=${download} target="_blank">Zip</a></td></tr>
% else:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</td>  <td>-</td></tr>
% endif
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auskunft')}</td>  <td>${c['attributes'][ausk] or '-'}</td></tr>
</%def>

<%def name="extended_info(c,lang)">
<%
    lang = lang if lang in ('fr','it','en', 'rm') else 'de'
    auft = 'auft_%s' % lang
    recht = 'recht_%s' % lang
    inhalt = 'inhalt_%s' % lang
    ausk = 'ausk_%s' % lang
    download = c['attributes']['download']
    web_link = c['attributes']['web_link']
    zweck = 'zweck_%s' % lang
    status = 'status_%s' % lang
    land = 'land_%s' % lang
    kanton = 'kanton_%s' % lang
    start = 'start_%s' % lang
    end = 'end_%s' % lang
%>

<table class="table-with-border bohrungen_tiefer_500-extended">
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</th>       <td>${c['attributes']['name'] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auftraggeb_de')}</th>       <td>${c['attributes'][auft] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.rechtein')}</th>       <td>${c['attributes'][recht] or '-'}</td></tr>
     <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.inhalt')}</th>       <td>${c['attributes'][inhalt] or '-'}</td></tr>
%  if c['attributes']['web_link'] != '-':
<%
    weblink = c['attributes']['web_link'].split('##')
%>
<tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link')}</th><td>
%  for i in range(len(weblink)):
      <a href="${weblink[i]}" target="_blank">Link_${i+1}</a>&nbsp;
%endfor
</td></tr>
% else:
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link')}</th>
      <td> - </td>
    </tr>
%endif
% if download != '-':
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</th>       <td><a href="${download}" target="_blank">Zip</a></td></tr>
% else:
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</th>       <td>-</td></tr>
% endif
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.auskunft')}</th>       <td>${c['attributes'][ausk] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.tiefe_md')}</th><td>${c['attributes']['tiefe_md'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.bohrzweck')}</th><td>${c['attributes'][zweck] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.status')}</th><td>${c['attributes'][status] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.startdate')}</th><td>${c['attributes'][start] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.enddate')}</th><td>${c['attributes'][end] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.koord_e')}</th><td>${int(c['attributes']['koord_e'])}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.koord_n')}</th><td>${int(c['attributes']['koord_n'])}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.height')}</th><td>${c['attributes']['koord_z'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.land')}</th><td>${c['attributes'][land] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.kanton')}</th><td>${c['attributes'][kanton] or '-'}</td></tr>
</table>
</%def>


