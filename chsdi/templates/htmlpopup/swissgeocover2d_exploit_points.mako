<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr',) else 'de'
    attrs = c['attributes']
%>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.kind')}</td>
        <td>${attrs.get('kind_' + lang) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.spec')}</td>
        <td>${attrs.get('spec_' + lang) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.erl_link')}</td>
        <td>${h.pipe_links(attrs.get('erl_link')) | n}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_points.ber_link')}</td>
        <td>${h.pipe_links(attrs.get('ber_link')) | n}</td>
    </tr>
</%def>
