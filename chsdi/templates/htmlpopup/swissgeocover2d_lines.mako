<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr',) else 'de'
    kind = 'kind_%s' % lang
    spec = c['attributes'].get('spec_' + lang)
%>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_lines.kind')}</td>
        <td>${c['attributes'][kind] or '-'}</td>
    </tr>
    % if spec:
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_lines.spec')}</td>
        <td>${spec}</td>
    </tr>
    % endif
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_lines.erl_link')}</td>
        <td>${h.pipe_links(c['attributes'].get('erl_link')) | n}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_lines.ber_link')}</td>
        <td>${h.pipe_links(c['attributes'].get('ber_link')) | n}</td>
    </tr>
</%def>
