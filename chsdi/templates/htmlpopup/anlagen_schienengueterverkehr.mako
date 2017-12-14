<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    typ = 'typ_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bav.anlagen-schienengueterverkehr.dst_nr')}</td>                   <td>${c['attributes']['dst_nr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.anlagen-schienengueterverkehr.name')}</td>                     <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.anlagen-schienengueterverkehr.dst_abk')}</td>                  <td>${c['attributes']['dst_abk'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.anlagen-schienengueterverkehr.isb')}</td>                      <td>${c['attributes']['isb'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bav.anlagen-schienengueterverkehr.typ')}</td>                      <td>${c['attributes'][typ] or '-'}</td></tr>
</%def>
