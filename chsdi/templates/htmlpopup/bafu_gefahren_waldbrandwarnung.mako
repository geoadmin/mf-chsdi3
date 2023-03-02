<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        c['stable_id'] = True
        lang = lang if lang in ('fr','it', 'en') else 'de'
        name_text = 'name_%s' %lang
        title_text = 'title_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_warnung.region_id')}</td>
        <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_warnung.canton')}</td>
        <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_warnung.name')}</td>
        <td>${c['attributes'][name_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_warnung.title')}</td>
        <td>${c['attributes'][title_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_warnung.valid_from')}</td>
        <td>${c['attributes']['valid_from'] or '-'}</td>
    </tr>
</%def>