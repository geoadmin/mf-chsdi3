<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td width="230">${_('tezgnr40')}</td>          <td>${c['attributes']['tezgnr40'] or '-'}</td></tr>
    <tr><td>${_('teilezgfla')}</td>         <td>${c['attributes']['teilezgfla'] or '-'}</td></tr>
</%def>

