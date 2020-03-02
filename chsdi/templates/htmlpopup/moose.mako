<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('bafu_population', lang)}</td><td>${c['attributes']['populationsnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('bafu_jahr', lang)}</td><td>${c['attributes']['jahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('bafu_standort', lang)}</td><td>${c['attributes']['standort'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('bafu_RLtext', lang)}</td><td>${c['attributes']['rl_text'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('bafu_NHVText', lang)}</td><td>${c['attributes']['nhv_text'] or '-'}</td></tr>
</%def>

