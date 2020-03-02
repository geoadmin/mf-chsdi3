<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">


    <tr><td class="cell-left">${Translator.translate('nr', lang)}</td>                    <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('title')}</td>                 <td>${c['attributes']['titel'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ausgabejahr')}</td>           <td>${c['attributes']['jahr'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_lubis_massstab')}</td>     <td>${c['attributes']['massstab'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('autor')}</td>                 <td>${c['attributes']['author'] or _('notintoposhop', lang)}</td></tr>
    <tr><td class="cell-left">${Translator.translate('format_de')}</td>             <td>${c['attributes']['format_kz'] or _('notintoposhop', lang)}</td></tr>


</%def>
