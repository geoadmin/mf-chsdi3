<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
 lang = lang if lang != 'rm' else 'de'
 chmurl = 'chmurl_%s' % lang
 link = c['attributes'][chmurl]
%>

<% c['stable_id'] = False %>
   <tr><td class="cell-left">${_('ch.astra.winterwanderwege.namer')}</td>                      <td>${c['attributes']['namer'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.winterwanderwege.nrr')}</td>                        <td>${c['attributes']['nrr']  or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.winterwanderwege.beschreibr')}</td>                 <td>${c['attributes']['beschreibr']  or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.winterwanderwege.laenger')}</td>                    <td>${c['attributes']['laenger']  or '-'} ${_('ch.astra.winterwanderwege.einheit_distanz')}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.winterwanderwege.hoeheaufr')}</td>                  <td>${c['attributes']['hoeheaufr']  or '-'} ${_('ch.astra.winterwanderwege.einheit_aufstieg')}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.winterwanderwege.hoeheabr')}</td>                   <td>${c['attributes']['hoeheabr']  or '-'} ${_('ch.astra.winterwanderwege.einheit_aufstieg')}</td></tr>
   <tr><td class="cell-left">${_('ch.astra.winterwanderwege.zeitstzir')}</td>                  <td>${c['attributes']['zeitstzir']  or '-'} ${_('ch.astra.winterwanderwege.einheit_zeit')}</td></tr>
   % if c['attributes'][chmurl]:
      <tr><td class="cell-left">${_('ch.astra.winterwanderwege.chmurl')}</td>                  <td><a href="${c['attributes'][chmurl]}" target='_blank'>${_('ch.astra.winterwanderwege.chmurl')}</td></tr>
   % else:
      <tr><td class="cell-left">${_('ch.astra.winterwanderwege.chmurl')}</td>                  <td>-</td></tr>
   % endif
</%def>
