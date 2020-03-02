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
  <tr><td class="cell-left">${t.translate('ch.bfe.bikesharing.provider', lang)}</td>          <td>
  % if c['attributes'][provider]:
        <a href="${c['attributes'][providerlink]}" target="_blank">${c['attributes'][provider] or '-'}</a>
  %else:
    -
  %endif
  </td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfe.bikesharing.address', lang)}</td>            <td>${c['attributes']['address'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfe.bikesharing.time', lang)}</td>               <td>${c['attributes'][time] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfe.bikesharing.rent', lang)}</td>               <td>${c['attributes'][rent] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfe.bikesharing.description', lang)}</td>        <td>${c['attributes'][description] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfe.bikesharing.return', lang)}</td>             <td>${c['attributes'][giveback] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfe.bikesharing.feedback', lang)}</td>          <td>
  % if c['attributes'][feedback]:
       ${t.translate('ch.bfe.bikesharing.incorrectinfo', lang)} <a href="${c['attributes'][feedback]}" target="_blank">${_('ch.bfe.bikesharing.feedbacklink') or '-'}</a>
  %else:
   -
  %endif
  </td></tr>
</%def>
