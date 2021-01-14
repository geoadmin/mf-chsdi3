<%inherit file="base.mako"/> 

<%def name="table_body(c, lang)">
<% 
    lang = lang if lang != 'rm' else 'de'
    title = 'title_%s' % lang
    description = 'description_%s' % lang
    topic = 'topic_%s' % lang
    status = 'status_%s' % lang
    link = 'link_%s' % lang
%>
<tr>
  <td class="cell-left">${_('ch.bfe.energieforschung.titel')}</td>
  <td>${c['attributes'][title] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bfe.energieforschung.beschreibung')}</td>
  <td>${c['attributes'][description] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bfe.energieforschung.thema')}</td>
  <td>${c['attributes'][topic] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bfe.energieforschung.projektstatus')}</td>
  <td>${c['attributes'][status] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bfe.energieforschung.projektbeginn')}</td>
  <td>${c['attributes']['duration'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bfe.energieforschung.link')}</td>
  % if c['attributes'][link] in [None, ""]:
  <td>${'-'}</td>
  % else:
  <td><a target="_blank" href="${c['attributes'][link]}">${_('link')}</a></td>
  % endif
</tr>
</%def>
