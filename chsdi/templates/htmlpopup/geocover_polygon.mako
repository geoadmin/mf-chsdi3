<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('fr') else 'de'
    basisdatensatz = 'basisdatensatz_%s' % lang
    description = 'description_%s' % lang
    litstrat_link = 'litstrat_link_%s' % lang
    litho = 'litho_%s' % lang
    chrono = 'chrono_%s' % lang
    tecto = 'tecto_%s' % lang
    harmos_rev = 'harmos_rev_%s' % lang
    if c['attributes'][litstrat_link] is not None:
            url = "http://" + c['attributes'][litstrat_link]
%>
    <tr><td class="cell-left">${t.translate('geocover_basisdatensatz', lang)}</td><td>${c['attributes'][basisdatensatz] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geocover.description', lang)}</td><td>${c['attributes'][description] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geocover.litstrat_link', lang)}</td><td>
    % if c['attributes'][litstrat_link]:
          <a href="${url}" target="_blank">Link</a>
    % else:
          -
    % endif
    </td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geocover.litho', lang)}</td><td>${c['attributes'][litho] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('geocover_tecto', lang)}</td><td>${c['attributes'][tecto] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geocover.chrono', lang)}</td><td>${c['attributes'][chrono] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geocover.harmos_rev', lang)}</td><td>${c['attributes'][harmos_rev] or '-'}</td></tr>
</%def>
