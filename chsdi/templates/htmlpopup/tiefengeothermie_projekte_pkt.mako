<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
  <%
    if lang in ('fr','it','en'):
      lang = lang
    else:
      lang = 'de'
    status_text = 'status_%s' % lang
    system_text = 'system_%s' % lang
    purpose_text = 'purpose_%s' % lang
  %>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.name')}</td>
    <td>${c['attributes']['name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.owner')}</td>
    <td>${c['attributes']['owner'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.status')}</td>
    <td>${c['attributes'][status_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.system')}</td>
    <td>${c['attributes'][system_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.use')}</td>
    <td>${c['attributes'][purpose_text] or '-'}</td>
  </tr>
</%def>


<%def name="extended_info(c,lang)">
  <%
    if lang in ('fr','it','en'):
      lang = lang
    else:
      lang = 'de'
    status_text = 'status_%s' % lang
    system_text = 'system_%s' % lang
    purpose_text = 'purpose_%s' % lang
    municipality_text = 'municipality_%s' % lang
    subsidy_text = 'subsidy_%s' % lang
    more_text = 'more_%s' % lang
  %>
  <table class="table-with-border tiefengeothermie_projekte-extended">
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.name')}</th>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.owner')}</th>
      <td>${c['attributes']['owner'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.status')}</th>
      <td>${c['attributes'][status_text] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.system')}</th>
      <td>${c['attributes'][system_text] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.use')}</th>
      <td>${c['attributes'][purpose_text] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.canton')}</th>
      <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.community')}</th>
      <td>${c['attributes'][municipality_text] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.depth')}</th>
      <td>${c['attributes']['res_tvd'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.reservoir')}</th>
      <td>${c['attributes']['reservoir'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.temp')}</th>
      <td>${c['attributes']['temperature'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.year')}</th>
      <td>${c['attributes']['year'] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.subsidy')}</th>
      <td>${c['attributes'][subsidy_text] or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.download')}</th>
        % if c['attributes']['download'] == None or c['attributes']['download'] == "-":
          <td>-</td>
        % else:
          <td><a href="${c['attributes']['download']}" target="_blank">Zip</a></td>
        % endif
    </tr>
    <tr>
      <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.more')}</th>
        % if c['attributes'][more_text] == None or c['attributes'][more_text] == "-":
          <td>-</td>
        % elif "https://" in c['attributes'][more_text]:
          <td><a href="${c['attributes'][more_text]}" target="_blank">Link</a></td>
        % elif "http://" in c['attributes'][more_text]:
          <td><a href="${c['attributes'][more_text]}" target="_blank">Link</a></td>
        % else:
          <td>${c['attributes'][more_text]}</td>
        % endif
    </tr>
  </table>
</%def>

