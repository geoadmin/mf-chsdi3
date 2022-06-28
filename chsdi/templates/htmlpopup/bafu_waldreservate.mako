<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <%
       lang = 'de' if lang in ('de', 'rm') else lang
       class_text = 'mcpfe_class_%s' % lang
    %>

    <tr><td class="cell-left">${_('ch.bafu.waldreservate.objnummer')}</td><td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.waldreservate.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.waldreservate.gisflaeche')}</td>
      % if c['attributes']['gisflaeche']:
        <td>${round(c['attributes']['gisflaeche'], 2)}</td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.waldreservate.obj_gesflaeche')}</td>
      % if c['attributes']['gesflaeche'] is not None:
        <td>${round(c['attributes']['gesflaeche'], 2)}</td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.waldreservate.gisteilobjekt')}</td>
      % if c['attributes']['gisteilobjekt']:
        <td>${round(c['attributes']['gisteilobjekt'], 2)}</td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr><td class="cell-left">${_('ch.bafu.waldreservate.mcpfe')}</td><td>${c['attributes'][class_text] or '-'}</td></tr>
</%def>

