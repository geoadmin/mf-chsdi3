<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
 lang = lang if lang != 'rm' else 'de'
 chmurl = 'chmurl_%s' % lang
 technikr = 'technikr_%s' % lang
 link = c['attributes'][chmurl]
%>

<% c['stable_id'] = False %>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.namer')}</td>                      <td>${c['attributes']['namer'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.nrr')}</td>                        <td>${c['attributes']['nrr']  or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.beschreibr')}</td>                 <td>${c['attributes']['beschreibr']  or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.laenger')}</td>                    <td>${c['attributes']['laenger']  or '-'} ${_('ch.astra.schneeschuhwanderwege.einheit_distanz')}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.hoeheaufr')}</td>                  <td>${c['attributes']['hoeheaufr']  or '-'}  ${_('ch.astra.schneeschuhwanderwege.einheit_aufstieg')}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.hoeheabr')}</td>                   <td>${c['attributes']['hoeheabr']  or '-'}  ${_('ch.astra.schneeschuhwanderwege.einheit_aufstieg')}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.zeitstzir')}</td>                  <td>${c['attributes']['zeitstzir']  or '-'} ${_('ch.astra.schneeschuhwanderwege.einheit_zeit')}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.technikr')}</td>                  <td>${c['attributes'][technikr]  or '-'}</td></tr>
   % if c['attributes'][chmurl]:
      <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.chmurl')}</td>                  <td><a href="${c['attributes'][chmurl]}" target='_blank'>${_('ch.astra.schneeschuhwanderwege.chmurl')}</td></tr>
   % else:
      <tr><td class="cell-left">${_('ch.astra.schneeschuhwanderwege.chmurl')}</td>                  <td>-</td></tr>
   % endif
</%def>
