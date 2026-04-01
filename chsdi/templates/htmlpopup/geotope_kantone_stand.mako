<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

    <%
        lang = lang if lang in ('fr','it','en') else 'de'
        access_text = 'access_%s' % lang
        publikatio_text = 'publikatio_%s' % lang
        bemerkung_text = 'bemerkung_%s' % lang
    %>

    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.sigel')}</td>
        <td>${c['attributes']['sigel'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.zugang')}</td>
        <td>${c['attributes'][access_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.link')}</td>
        % if c['attributes']['link'] and c['attributes']['link'].startswith('http'):
            <td><a href="${c['attributes']['link']}" target="_blank">${c['attributes']['link']}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.kontakt')}</td>
        % if c['attributes']['kontakt'] != '-':
            <td><a href="${c['attributes']['kontakt']}" target="_blank">${c['attributes']['kontakt']}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.publikation')}</td>
        % if c['attributes'][publikatio_text] and c['attributes'][publikatio_text].startswith('http'):
            <td><a href="${c['attributes'][publikatio_text]}" target="_blank">${c['attributes'][publikatio_text]}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.quelle')}</td>
        <td>${c['attributes']['quelle'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.bemerkung')}</td>
        <td>${c['attributes'][bemerkung_text] or '-'}</td>
    </tr>

</%def>
