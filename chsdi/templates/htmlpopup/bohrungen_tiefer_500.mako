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
     <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.name', lang)}</td>   <td>${c['attributes']['name'] or '-'}</td></tr>
     <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.auftraggeb_de', lang)}</td>   <td>${c['attributes'][auft] or '-'}</td></tr>
     <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.rechtein', lang)}</td> <td>${c['attributes'][recht] or '-'}</td></tr>
     <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.inhalt', lang)}</td>   <td>${c['attributes'][inhalt] or '-'}</td></tr>
%  if c['attributes']['web_link'] != '-':
<%
    weblink = c['attributes']['web_link'].split('##')
%>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link', lang)}</td><td>
%  for i in range(len(weblink)):
      <a href="${weblink[i]}" target="_blank">Link_${i+1}</a>&nbsp;
%endfor
</td></tr>
% else:
    <tr>
      <td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link', lang)}</td>
      <td> - </td>
    </tr>
%endif
% if download != '-':
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.download', lang)}</td>  <td><a href=${download} target="_blank">Zip</a></td></tr>
% else:
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.download', lang)}</td>  <td>-</td></tr>
% endif
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.auskunft', lang)}</td>  <td>${c['attributes'][ausk] or '-'}</td></tr>
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
     <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.name', lang)}</th>       <td>${c['attributes']['name'] or '-'}</td></tr>
     <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.auftraggeb_de', lang)}</th>       <td>${c['attributes'][auft] or '-'}</td></tr>
     <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.rechtein', lang)}</th>       <td>${c['attributes'][recht] or '-'}</td></tr>
     <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.inhalt', lang)}</th>       <td>${c['attributes'][inhalt] or '-'}</td></tr>
%  if c['attributes']['web_link'] != '-':
<%
    weblink = c['attributes']['web_link'].split('##')
%>
<tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link', lang)}</th><td>
%  for i in range(len(weblink)):
      <a href="${weblink[i]}" target="_blank">Link_${i+1}</a>&nbsp;
%endfor
</td></tr>
% else:
    <tr>
      <th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link', lang)}</th>
      <td> - </td>
    </tr>
%endif
% if download != '-':
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.download', lang)}</th>       <td><a href="${download}" target="_blank">Zip</a></td></tr>
% else:
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.download', lang)}</th>       <td>-</td></tr>
% endif
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.auskunft', lang)}</th>       <td>${c['attributes'][ausk] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.tiefe_md', lang)}</th><td>${c['attributes']['tiefe_md'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.bohrzweck', lang)}</th><td>${c['attributes'][zweck] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.status', lang)}</th><td>${c['attributes'][status] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.startdate', lang)}</th><td>${c['attributes'][start] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.enddate', lang)}</th><td>${c['attributes'][end] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.koord_e', lang)}</th><td>${int(c['attributes']['koord_e'])}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.koord_n', lang)}</th><td>${int(c['attributes']['koord_n'])}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.height', lang)}</th><td>${c['attributes']['koord_z'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.land', lang)}</th><td>${c['attributes'][land] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-bohrungen_tiefer_500.kanton', lang)}</th><td>${c['attributes'][kanton] or '-'}</td></tr>
</table>
</%def>


