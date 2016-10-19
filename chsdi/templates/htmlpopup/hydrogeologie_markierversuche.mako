<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.nr_meldeblatt')}</td>           <td>${c['attributes']['nr_meldeblatt'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.y')}</td>         <td>${c['attributes']['y'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.x')}</td>           <td>${c['attributes']['x'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.ort')}</td>     <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.datum')}</td>         <td>${c['attributes']['datum'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.milieu')}</td>         <td>${c['attributes']['milieu'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.markierstoff')}</td>         <td>${c['attributes']['markierstoff'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrogeologie-markierversuche.menge_einheit')}</td>         <td>${c['attributes']['menge_einheit'] or '-'}</td></tr>
</%def>

