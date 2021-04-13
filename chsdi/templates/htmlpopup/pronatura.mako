<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${_('ch.pronatura.waldreservate.objnummer')}</td><td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.pronatura.waldreservate.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.pronatura.waldreservate.gisflaeche')}</td><td>${round(c['attributes']['gisflaeche'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.pronatura.waldreservate.obj_gesflaeche')}</td><td>${round(c['attributes']['gesflaeche'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.pronatura.waldreservate.gisteilobjekt')}</td> <td>${round(c['attributes']['gisteilobjekt'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.pronatura.waldreservate.mcpfe')}</td><td>${_('ch.pronatura.waldreservate.tt_pronatura_e3')}</td></tr>

</%def>
