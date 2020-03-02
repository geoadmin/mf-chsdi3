<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
  loli_value = '-' if c['attributes']['loli_value'] == -9999 else str(c['attributes']['loli_value'])
  upli_value = '-' if c['attributes']['upli_value']  == -9999 else str(c['attributes']['upli_value'])
%>
    <tr><td class="cell-left">${Translator.translate('ch.bazl.luftraeume-fluginformationsgebiet.name', lang)}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bazl.luftraeume-fluginformationsgebiet.designator', lang)}</td>         <td>${c['attributes']['designator'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bazl.luftraeume-fluginformationsgebiet.type', lang)}</td>         <td>${c['attributes']['type'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bazl.luftraeume-fluginformationsgebiet.loli_value', lang)}</td>         <td>${loli_value}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bazl.luftraeume-fluginformationsgebiet.loli_type', lang)}</td>         <td>${c['attributes']['loli_type'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bazl.luftraeume-fluginformationsgebiet.upli_value', lang)}</td>         <td>${upli_value}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bazl.luftraeume-fluginformationsgebiet.upli_type', lang)}</td>         <td>${c['attributes']['upli_type'] or '-'}</td></tr>
</%def>
