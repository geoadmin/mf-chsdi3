<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
  lang = lang if lang in ('fr','it','en') else 'de'
  provider = 'provider_%s' % lang
  providerlink = 'providerlink_%s' % lang
  time = 'time_%s' % lang
  rent = 'rent_%s' % lang
  description = 'description_%s' % lang
  giveback = 'return_%s' % lang
  feedback = 'feedback_%s' % lang
%>
  <tr><td class="cell-left">${_('ch.bfe.bikesharing.provider')}</td>          <td>
  % if c['attributes'][provider]:
        <a href="${c['attributes'][providerlink]}" target="_blank">${c['attributes'][provider] or '-'}</a>
  %else:
    -
  %endif
  </td></tr>
  <tr><td class="cell-left">${_('ch.bfe.bikesharing.address')}</td>            <td>${c['attributes']['address'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfe.bikesharing.time')}</td>               <td>${c['attributes'][time] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfe.bikesharing.rent')}</td>               <td>${c['attributes'][rent] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfe.bikesharing.description')}</td>        <td>${c['attributes'][description] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfe.bikesharing.return')}</td>             <td>${c['attributes'][giveback] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfe.bikesharing.feedback')}</td>          <td>
  % if c['attributes'][feedback]:
       ${_('ch.bfe.bikesharing.incorrectinfo')} <a href="${c['attributes'][feedback]}" target="_blank">${_('ch.bfe.bikesharing.feedbacklink') or '-'}</a>
  %else:
   -
  %endif
  </td></tr>
</%def>
