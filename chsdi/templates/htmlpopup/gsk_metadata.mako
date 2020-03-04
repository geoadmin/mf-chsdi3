<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">


    <tr><td class="cell-left">${mod_translate.Translator.translate('nr', lang)}</td>                    <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('title', lang)}</td>                 <td>${c['attributes']['titel'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ausgabejahr', lang)}</td>           <td>${c['attributes']['jahr'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_lubis_massstab', lang)}</td>     <td>${c['attributes']['massstab'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('autor', lang)}</td>                 <td>${c['attributes']['author'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('format_de', lang)}</td>             <td>${c['attributes']['format_kz'] or _('notintoposhop', lang)}</td></tr>


</%def>
