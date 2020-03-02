<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    typ = 'typ_%s' % lang
%>
    <tr><td class="cell-left">${Translator.translate('ch.bav.anlagen-schienengueterverkehr.dst_nr', lang)}</td>                   <td>${c['attributes']['dst_nr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.anlagen-schienengueterverkehr.name', lang)}</td>                     <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.anlagen-schienengueterverkehr.dst_abk', lang)}</td>                  <td>${c['attributes']['dst_abk'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.anlagen-schienengueterverkehr.isb', lang)}</td>                      <td>${c['attributes']['isb'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bav.anlagen-schienengueterverkehr.typ', lang)}</td>                      <td>${c['attributes'][typ] or '-'}</td></tr>
</%def>
