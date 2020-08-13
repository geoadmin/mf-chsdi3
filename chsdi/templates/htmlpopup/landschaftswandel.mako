<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
    typ1_text = 'typ1_%s' % lang
    typ2_text = 'typ2_%s' % lang
    typ3_text = 'typ3_%s' % lang
    typ4_text = 'typ4_%s' % lang
    download_link = 'linkdownload_%s' % lang
    quickview_link = ${c['attributes']['linkbild']}
    quickview_size = "?width=198&height=120"
%>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.gmde')}</td>
  <td colspan="4">${c['attributes']['gmde'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.swissnames')}</td>
  <td colspan="4">${c['attributes']['swissnames'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.typ')}</td>
  <td><div style='display: inline-block; padding: 2px;'>${c['attributes'][typ1_text] or ''}</div></td>
  <td><div style='display: inline-block; padding: 2px;'>${c['attributes'][typ2_text] or ''}</div></td>
  <td><div style='display: inline-block; padding: 2px;'>${c['attributes'][typ3_text] or ''}</div></td>
  <td><div style='display: inline-block; padding: 2px;'>${c['attributes'][typ4_text] or ''}</div></td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.linkdownload')}</td>
  <td colspan="4"><a href="${c['attributes'][download_link] or '-'}" target="_blank">${_('link')}</a></td>
</tr>

<tr>
  <td class="cell-left">${_('quickview')}</td>
  <td colspan="4">${quickview_link}"</td>
</tr>  

</%def>

