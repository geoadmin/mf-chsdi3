<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        c['stable_id'] = True
        lang = lang if lang in ('fr','it', 'en') else 'de'
        name_text = 'name_%s' %lang
        title_text = 'title_%s' %lang
        description_text = 'description_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone.region_id')}</td>
        <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone.canton')}</td>
        <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone.name')}</td>
        <td>${c['attributes'][name_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone.title')}</td>
        <td>${c['attributes'][title_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone.description')}</td>
        <td>${c['attributes'][description_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone.valid_from')}</td>
        <td>${c['attributes']['valid_from'] or '-'}</td>
    </tr>
</%def>