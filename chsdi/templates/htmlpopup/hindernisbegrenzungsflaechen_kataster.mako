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
  %if 'Polygon' in c['attributes']['geom_type']:
    <tr>
      <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.heightaccordingvil')}</td>
      %if c['attributes']['heightaccordingvil'] == 'Yes':
        <td>${_('yesText')}</td>
      %elif c['attributes']['heightaccordingvil'] == 'No':
        <td>${_('noText')}</td>
      %else:
        <td>-</td>
      %endif
    </tr>
    %if c['attributes']['heightaboveground'] != None:
    <tr>
      <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.heightaboveground')}</td>
      <td>${c['attributes']['heightaboveground'] or '-'}</td>
    </tr>
    %endif
  %endif
  <tr>
    <td class="cell-left">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.document')}</td>
    %if c['attributes']['document'].startswith('http'):
      <td><a href="${c['attributes']['document']}" target="_blank">${_('ch.bazl.hindernisbegrenzungsflaechen-kataster.link')}</a></td>
    %else:
      <td>-</td>
    %endif
  </tr>
</%def>
