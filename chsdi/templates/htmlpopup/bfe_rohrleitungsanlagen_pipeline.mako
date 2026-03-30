<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    pipeline_status_text = 'pipeline_status_%s' % lang
    medium_type_text = 'medium_type_%s' % lang
  %>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.pipeline_status')}</td>
    <td>${c['attributes'][pipeline_status_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.aname')}</td>
    <td>${c['attributes']['namepipeline_name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.medium_type')}</td>
    <td>${c['attributes'][medium_type_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.maximum_operating_pressure')}</td>
    <td>${c['attributes']['maximum_operating_pressure'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.year_of_construction')}</td>
    <td>${c['attributes']['year_of_construction'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.outside_diameter')}</td>
    <td>${c['attributes']['outside_diameter'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.operator_name')}</td>
    <td>${c['attributes']['operator_name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.operator_uri')}</td>
    <td>${c['attributes']['operator_uri'] or '-'}</td>
  </tr>
</%def>
