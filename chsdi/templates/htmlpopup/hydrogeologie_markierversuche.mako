<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.nr_meldeblatt', lang)}</td>           <td>${c['attributes']['nummer_ein'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.y', lang)}</td>         <td>${c['attributes']['y'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.x', lang)}</td>           <td>${c['attributes']['x'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.ort', lang)}</td>     <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.datum', lang)}</td>         <td>${c['attributes']['datum'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.milieu', lang)}</td>         <td>${c['attributes']['milieu'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.markierstoff', lang)}</td>         <td>${c['attributes']['markierstoff'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.hydrogeologie-markierversuche.menge_einheit', lang)}</td>         <td>${c['attributes']['menge_einheit'] or '-'}</td></tr>
</%def>

