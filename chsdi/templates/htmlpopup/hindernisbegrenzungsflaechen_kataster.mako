<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.icaoloc')}</td>    
    <td>${c['attributes']['icaoloc'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.surfacetype')}</td>
    <td>${c['attributes']['surfacetype'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.validfrom')}</td>
    <td>${c['attributes']['validfrom'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.validuntil')}</td>
    <td>${c['attributes']['validuntil'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.document')}</td>
    %if c['attributes']['document'].startswith('http'):
      <td><a href="${c['attributes']['document']}" target="_blank">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.link')}</a></td>
    %else:
      <td>-</td>
    %endif
  </tr>
</%def>
