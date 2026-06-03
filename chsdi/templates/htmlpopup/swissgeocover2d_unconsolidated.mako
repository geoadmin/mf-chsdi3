<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr',) else 'de'
    runc_litho = 'runc_litho_%s' % lang
    runc_litstrat = 'runc_litstrat_%s' % lang
    runc_chrono = 'runc_chrono_combined_%s' % lang
    runc_glac_typ = 'runc_glac_typ_%s' % lang
    runc_structur = 'runc_structur_%s' % lang
    runc_morpholo = 'runc_morpholo_%s' % lang
%>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.runc_litho')}</td>
        <td>${c['attributes'][runc_litho] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.runc_litstrat')}</td>
        <td>${c['attributes'][runc_litstrat] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.runc_chrono')}</td>
        <td>${c['attributes'][runc_chrono] or '-'}</td>
    </tr>
    % if c['attributes'][runc_glac_typ]:
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.runc_glac_typ')}</td>
        <td>${c['attributes'][runc_glac_typ]}</td>
    </tr>
    % endif
    % if c['attributes'][runc_structur]:
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.runc_structur')}</td>
        <td>${c['attributes'][runc_structur]}</td>
    </tr>
    % endif
    % if c['attributes'][runc_morpholo]:
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.runc_morpholo')}</td>
        <td>${c['attributes'][runc_morpholo]}</td>
    </tr>
    % endif
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.erl_link')}</td>
        <td>${h.pipe_links(c['attributes'].get('erl_link')) | n}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_unconsolidated.ber_link')}</td>
        <td>${h.pipe_links(c['attributes'].get('ber_link')) | n}</td>
    </tr>
</%def>
