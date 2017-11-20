<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('fr') else 'de'
    litho = 'litho_%s' % lang
    chrono = 'chrono_%s' % lang
    harmos_rev = 'harmos_rev_%s' % lang
    if c['attributes']['litstrat_link'] is not None:
            url = "http://" + c['attributes']['litstrat_link']
%>
    <tr><td class="cell-left">${_('geocover_basisdatensatz')}</td><td>${c['attributes']['basisdatensatz'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.description')}</td><td>${c['attributes']['description'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.litstrat_link')}</td><td>
    % if c['attributes']['litstrat_link']:
          <a href="${url}" target="_blank">${c['attributes']['litstrat_link'] or '-'}</a>
    % else:
          -
    % endif
    </td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.litho')}</td><td>${c['attributes'][litho] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_tecto')}</td><td>${c['attributes']['tecto'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.chrono')}</td><td>${c['attributes'][chrono] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.harmos_rev')}</td><td>${c['attributes'][harmos_rev] or '-'}</td></tr>
</%def>
