<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    titel = 'titel_%s' % lang
    weblink = 'weblink_%s' % lang
    download = c['attributes']['download']
%>
     <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.land', lang)}</td>       <td>${c['attributes']['land'] or '-'}</td></tr>
     <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.kanton', lang)}</td>       <td>${c['attributes']['kanton'] or '-'}</td></tr>
     <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.nb_studien', lang)}</td>       <td>${c['attributes']['nb_studien']}</td></tr>
</%def>


<%def name="extended_info(c,lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    titel = 'titel_%s' % lang
    weblink = 'weblink_%s' % lang
    download = c['attributes']['download']
    nbstudien = c['attributes']['nb_studien']
    titel = c['attributes'][titel].split('##')
    autor = c['attributes']['autor'].split('##')
    jahr = c['attributes']['jahr'].split('##')
    auftraggeber = c['attributes']['auftraggeber'].split('##')
    weblink = c['attributes'][weblink].split('##')
    download = c['attributes']['download'].split('##')
%>

<table class="table-with-border geothermishce_potenzialstudien-extended">
     <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.land', lang)}</th>       <td>${c['attributes']['land'] or '-'}</td></tr>
     <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.kanton', lang)}</th>       <td>${c['attributes']['kanton'] or '-'}</td></tr>
     <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.nb_studien', lang)}</th>       <td>${nbstudien}</td></tr>
% if nbstudien==0:
     <tr><th class="cell-left" colspan=2>${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.studie', lang)}</th></tr>
     <tr><td class="cell-left" colspan=2>${titel[0] or '-'}</td></tr>
%endif
% if nbstudien>0:
   % for i in range(int(nbstudien)):
      <tr><th class="cell-left" colspan=2>${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.studie', lang)} ${i+1}</th></tr>
      <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.titel', lang)}</th>       <td>${titel[i] or '-'}</td></tr>
      <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.autor', lang)}</th>       <td>${autor[i] or '-'}</td></tr>
      <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.jahr', lang)}</th>       <td>${jahr[i] or '-'}</td></tr>
      <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.auftraggeber', lang)}</th>       <td>${auftraggeber[i] or '-'}</td></tr>
      % if weblink[i] != '-':
         <%
            weblink2=weblink[i].split(' ; ') 
         %>
         % if len(weblink2)==1:
            % if "http" in weblink2[0]:  
            <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.weblink', lang)}</th>       <td><a href="${weblink2[0]}" target="_blank">Link</a></td></tr>
            % else:
            <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.weblink', lang)}</th>       <td>${weblink2[0]}</td></tr>
            %endif
         % else:
            <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.weblink', lang)}</th><td>
            % for j in range(len(weblink2)):
               % if weblink2[j] != '-':
                 % if "http" in weblink2[j]:
                  <a href="${weblink2[j]}" target="_blank">Link_${j+1}</a>&nbsp;
                 % else:
                  ${weblink2[j]}&nbsp;
                 %endif                
               % else:
                  <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.weblink', lang)}</th>       <td>-</td></tr>
               %endif
            %endfor 
            </td></tr>
         %endif
      % else:
         <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.weblink', lang)}</th>       <td>-</td></tr>
      %endif
      % if download[0]=='-':
      <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.download', lang)}</th>       <td>-</td></tr>
      % else:
      <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-geothermische_potenzialstudien_regional.download', lang)}</th>       <td><a href="${download[0]}" target="_blank">Zip</a></td></tr>
      %endif
   %endfor
%endif 
</table>
</%def>


