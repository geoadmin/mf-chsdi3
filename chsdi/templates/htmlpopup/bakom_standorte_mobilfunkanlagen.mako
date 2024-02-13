<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it','rm','en') else 'de'
        typ_text = 'typ_%s' %lang
        power_text = 'power_%s' %lang
        techno_text = 'techno_%s' %lang
        adaptiv_text = 'adaptiv_%s' %lang
        bewilligung_text = 'bewilligung_%s' %lang
        agw_text = 'agw_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bakom.standorte-mobilfunkanlagen.station')}</td>
        <td>${c['attributes']['station'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.standorte-mobilfunkanlagen.typ')}</td>
        <td>${c['attributes'][typ_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.standorte-mobilfunkanlagen.koord')}</td>
        <td>${c['attributes']['koord'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.standorte-mobilfunkanlagen.power')}</td>
        <td>${c['attributes'][power_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left"></td>
        <td>${c['attributes'][techno_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left"></td>
        <td>${c['attributes'][adaptiv_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.standorte-mobilfunkanlagen.bewilligung')}</td>
        <td>${c['attributes'][bewilligung_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left"></td>
        <td>${c['attributes'][agw_text] or '-'}</td>
    </tr>

</%def>
