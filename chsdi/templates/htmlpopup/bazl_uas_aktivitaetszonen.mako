<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr', 'it', 'en') else 'de'
        routelocation_text = 'routelocation_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.routelocation')}</td>
        <td>${c['attributes'][routelocation_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.startdatetime')}</td>
        <td>${c['attributes']['startdatetime'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.enddatetime')}</td>
        <td>${c['attributes']['enddatetime'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.validityutc')}</td>
        <td>${c['attributes']['validity'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.lowerlimit')}</td>
        <td>${c['attributes']['lowerlimit'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.upperlimit')}</td>
        <td>${c['attributes']['upperlimit'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.heightaboveground')}</td>
        <td>${c['attributes']['heightaboveground'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.description')}</td>
        <td>${c['attributes']['description'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.existingdetectionsystems')}</td>
        <td>${c['attributes']['existingdetectionsystems'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.uas-aktivitaetszonen.coordination')}</td>
        <td>${c['attributes']['coordination'] or '-'}</td>
    </tr>
</%def>
