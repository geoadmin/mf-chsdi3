<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('fr') else 'de'
    description = 'description_%s' % lang
    litstrat_link = 'litstrat_link_%s' % lang
    litho = 'litho_%s' % lang
    chrono = 'chrono_%s' % lang
    tecto = 'tecto_%s' % lang
    if c['attributes'][litstrat_link] is not None:
            url = "http://" + c['attributes'][litstrat_link]
    orig_description = 'orig_description_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.description')}</td><td>${c['attributes'][description] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.litstrat_link')}</td><td>
    % if c['attributes'][litstrat_link]:
          <a href="${url}" target="_blank">Link</a>
    % else:
          -
    % endif
    </td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.litho')}</td><td>${c['attributes'][litho] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_tecto')}</td><td>${c['attributes'][tecto] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.chrono')}</td><td>${c['attributes'][chrono] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_orig_description')}</td><td>${c['attributes'][orig_description] or '-'}</td></tr>
</%def>
