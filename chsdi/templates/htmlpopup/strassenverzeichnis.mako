<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <%
    validated = 'yesText' if c['attributes']['validated'] == 1 else 'noText'
    official = 'yesText' if c['attributes']['official'] == 1 else 'noText'
    %>

    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.esid')}</td>                 <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.label')}</td>                 <td>${c['attributes']['label'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.plzo')}</td>                 <td>${c['attributes']['plzo'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.gdenr')}</td>                 <td>${c['attributes']['gdenr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.gdename')}</td>                 <td>${c['attributes']['gdename'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.type')}</td>                 <td>${_(c['attributes']['type'] or '-')}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.status')}</td>                 <td>${_(c['attributes']['status'] or '-')}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.official')}</td>                 <td>${_(official)}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.validated')}</td>                 <td>${_(validated)}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-strassenverzeichnis.modified')}</td>                 <td>${_(c['attributes']['modified'] or '-')}</td></tr>
</%def>
