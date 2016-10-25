<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
  loli_value = '-' if c['attributes']['loli_value'] == -9999 else str(c['attributes']['loli_value'])
  upli_value = '-' if c['attributes']['upli_value']  == -9999 else str(c['attributes']['upli_value'])
%>
    <tr><td class="cell-left">${_('ch.bazl.luftraeume-fluginformationsgebiet.name')}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftraeume-fluginformationsgebiet.designator')}</td>         <td>${c['attributes']['designator'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftraeume-fluginformationsgebiet.type')}</td>         <td>${c['attributes']['type'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftraeume-fluginformationsgebiet.loli_value')}</td>         <td>${loli_value}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftraeume-fluginformationsgebiet.loli_type')}</td>         <td>${c['attributes']['loli_type'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftraeume-fluginformationsgebiet.upli_value')}</td>         <td>${upli_value}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftraeume-fluginformationsgebiet.upli_type')}</td>         <td>${c['attributes']['upli_type'] or '-'}</td></tr>
</%def>
