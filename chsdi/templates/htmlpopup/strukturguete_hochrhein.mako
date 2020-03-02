<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.strukturguete-hochrhein_linkesufer.datenherkunft', lang)}</td>
    <td>${c['attributes']['datenherkunft'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.strukturguete-hochrhein_linkesufer.lumfeld', lang)}</td>
    <td>${c['attributes']['lumfeld'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.strukturguete-hochrhein_linkesufer.lufer', lang)}</td>
    <td>${c['attributes']['lufer'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.strukturguete-hochrhein_linkesufer.sohle', lang)}</td>
    <td>${c['attributes']['sohle'] or '-'}</td></tr> 
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.strukturguete-hochrhein_linkesufer.rufer', lang)}</td>
    <td>${c['attributes']['rufer'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.strukturguete-hochrhein_linkesufer.rumfeld', lang)}</td>
    <td>${c['attributes']['rumfeld'] or '-'}</td></tr>
</%def>

