<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${h.translate('ch.bafu.hydrologie-gewaesserzustandsmessstationen.name', lang)}</td>    <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td>${h.translate('ch.bafu.hydrologie-gewaesserzustandsmessstationen.gewaesser', lang)}</td>   <td>${c['attributes']['gewaesser'] or '-'}</td></tr>
    <tr><td>${h.translate('ch.bafu.hydrologie-gewaesserzustandsmessstationen.nr', lang)}</td>   <td>${c['attributes']['nr'] or '-'()}</td></tr>

</%def>

