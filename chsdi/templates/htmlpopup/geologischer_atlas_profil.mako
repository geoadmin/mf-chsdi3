<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
    if lang == 'rm':
        lang = 'de'

    link_onlineshop = c['attributes']['link_onlineshop_' + lang]
    swissgeol_link = c['attributes']['swissgeol_link_' + lang]
    %>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.ga25_name')}</td>
        <td>${c['attributes']['ga25_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.ga25_edition')}</td>
        <td>${c['attributes']['ga25_edition'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.link_original')}</td>
        % if c['attributes']['link_original']:
        <td><a target ="_blank" href="${c['attributes']['link_original']}">${_('link')}</a></td>
        % else:
        <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.link_onlineshop')}</td>
        % if link_onlineshop:
        <td><a target ="_blank" href="${link_onlineshop}">${_('link')}</a></td>
        % else:
        <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.swissgeol_link')}</td>
        % if swissgeol_link:
        <td><a target ="_blank" href="${swissgeol_link}">${_('link')}</a></td>
        % else:
        <td>-</td>
        % endif
    </tr>
</%def>


<%def name="extended_info(c, lang)">
    <%
    if lang == 'rm':
        lang = 'de'

    section_type = c['attributes']['section_type_' + lang]
    link_onlineshop = c['attributes']['link_onlineshop_' + lang]
    swissgeol_link = c['attributes']['swissgeol_link_' + lang]
    %>
    <table>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.ga25_name')}</td>
            <td class="cell-meta">${c['attributes']['ga25_name'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.ga25_no')}</td>
            <td class="cell-meta">${c['attributes']['ga25_no'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.ga25_edition')}</td>
            <td class="cell-meta">${c['attributes']['ga25_edition'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.plate_no')}</td>
            <td class="cell-meta">${c['attributes']['plate_no'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.section_no')}</td>
            <td class="cell-meta">${c['attributes']['section_no'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.section_type')}</td>
            <td class="cell-meta">${section_type or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.scale')}</td>
            <td class="cell-meta">${c['attributes']['scale'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.vert_exag')}</td>
            % if c['attributes']['vert_exag']:
                <td class="cell-meta">${round(c['attributes']['vert_exag'], 2)}</td>
            % else:
                <td class="cell-meta">-</td>
            % endif
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.author')}</td>
            <td class="cell-meta">${c['attributes']['author'] or '-'}</td>
        </tr>

        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.link_original')}</td>
            % if c['attributes']['link_original']:
            <td class="cell-meta"><a target ="_blank" href="${c['attributes']['link_original']}">${_('link')}</a></td>
            % else:
            <td class="cell-meta">-</td>
            % endif
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.link_onlineshop')}</td>
            % if link_onlineshop:
            <td class="cell-meta"><a target ="_blank" href="${link_onlineshop}">${_('link')}</a></td>
            % else:
            <td class="cell-meta">-</td>
            % endif
        </tr>
        <tr>
            <td class="cell-meta">${_(c['layerBodId'] + '.swissgeol_link')}</td>
            % if swissgeol_link:
            <td class="cell-meta"><a target ="_blank" href="${swissgeol_link}">${_('link')}</a></td>
            % else:
            <td class="cell-meta">-</td>
            % endif
        </tr>
    </table>
</%def>
