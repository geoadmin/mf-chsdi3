<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it') else 'de'
        genh1_text = 'genh1_%s' %lang
        gwaersceh1_text = 'gwaersceh1_%s' %lang
        gwaerzh1_text = 'gwaerzh1_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.egid')}</td>
        <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.strname')}</td>
        <td>${c['attributes']['strname'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.dplzname')}</td>
        <td>${c['attributes']['dplzname'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.gwaerzh1')}</td>
        <td>${c['attributes'][gwaerzh1_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.genh1')}</td>
        <td>${c['attributes'][genh1_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.gwaersceh1')}</td>
        <td>${c['attributes'][gwaersceh1_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.gwaerdath1')}</td>
        <td>${c['attributes']['gwaerdath1'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung.gexpdat')}</td>
        <td>${c['attributes']['gexpdat'] or '-'}</td>
    </tr>
</%def>
