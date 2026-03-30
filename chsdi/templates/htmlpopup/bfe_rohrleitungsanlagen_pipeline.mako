<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    pipeline_status_text = 'pipeline_status_%s' % lang
    medium_type_text = 'medium_type_%s' % lang
  %>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.pipelinestatus')}</td>
    <td>${c['attributes'][pipeline_status_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.aname')}</td>
    <td>${c['attributes']['pipeline_name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.mediumtype')}</td>
    <td>${c['attributes'][medium_type_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.maximumoperatingpressure')}</td>
    <td>${c['attributes']['maximum_operating_pressure'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.yearofconstruction')}</td>
    <td>${c['attributes']['year_of_construction'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.outsidediameter')}</td>
    <td>${c['attributes']['outside_diameter'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.operatorname')}</td>
    <td>${c['attributes']['operator_name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.operatoruri')}</td>
    % if c['attributes']['operator_uri'].startswith('http'):
      <td><a target ="_blank" href="${c['attributes']['operator_uri']}">${_('link')}</a></td>
    % else:
      <td>-</td>
    % endif
  </tr>
</%def>
