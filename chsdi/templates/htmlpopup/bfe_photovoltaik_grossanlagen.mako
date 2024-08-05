<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
        status_text = 'statuscategory_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.projectname')}</td>
        %if c['attributes']['projectweb'] is not None:
            <td><a href="${c['attributes']['projectweb']}" target="_blank">${c['attributes']['projectname']}</a></td>
        %else:
            <td>${c['attributes']['projectname']}</td>
        %endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.projectmanagement')}</td>
        <td>${c['attributes']['projectmanagement'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.status')}</td>
        <td>${c['attributes'][status_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.power')}</td>
        <td>${c['attributes']['power'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.annualproduction')}</td>
        <td>${c['attributes']['annualproduction'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.winterproduction')}</td>
        <td>${c['attributes']['winterproduction'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.specificannualproduction')}</td>
        <td>${c['attributes']['specificannualproduction'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.specificwinterproduction')}</td>
        <td>${c['attributes']['specificwinterproduction'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.photovoltaik-grossanlagen.elevation')}</td>
        <td>${c['attributes']['elevation'] or '-'}</td>
    </tr>
</%def>
