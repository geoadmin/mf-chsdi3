<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        lang = 'de' if lang in ('de', 'rm', 'en') else 'fr'
        nutzung = 'nutzung_%s' % lang
        hauptkategorie = 'hauptkategorie_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.bur_nr')}</td>
        <td>${c['attributes']['bur_nr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.lnf_code')}</td>
        <td>${c['attributes']['lnf_code'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.nutzungsidentifikator')}</td>
        <td>${c['attributes']['nutzungsidentifikator'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.nutzung')}</td>
        <td>${c['attributes'][nutzung] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.hauptkategorie')}</td>
        <td>${c['attributes'][hauptkategorie] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.bff_qualitaet_1')}</td>
        % if c['attributes']['bff_qualitaet_1'] is not None:
            <td>${c['attributes']['bff_qualitaet_1']}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.bezugsjahr')}</td>
        <td>${c['attributes']['bezugsjahr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.bewirtschaftungsgrad')}</td>
        <td>${c['attributes']['bewirtschaftungsgrad'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.blw.landwirtschaftliche-nutzungsflaechen.flaeche_m2')}</td>
        <td>${c['attributes']['flaeche_m2'] or '-'}</td>
    </tr>
</%def>

