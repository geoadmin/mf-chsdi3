<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('sia_261_norm')}</td><td>${c['attributes']['bgk'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.gefahren-baugrundklassen.referenz')}</td><td>${c['attributes']['referenz'] or '-'}</td></tr>
</%def>

