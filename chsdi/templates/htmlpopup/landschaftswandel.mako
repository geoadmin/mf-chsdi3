<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
    typ1_text = 'typ1_%s' % lang
    typ2_text = 'typ2_%s' % lang
    typ3_text = 'typ3_%s' % lang
    typ4_text = 'typ4_%s' % lang
    download_link = 'linkdownload_%s' % lang

    def getQuickviewLink(link):
        quickview_link = link.split('?')[0] + "?width=198&height=120"
        return quickview_link

%>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.gmde')}</td>
  <td class="cell-left" colspan="4">${c['attributes']['gmde'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.swissnames')}</td>
  <td class="cell-left" colspan="4">${c['attributes']['swissnames'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left" rowspan="4">${_('ch.bfs.landschaftswandel.typ')}</td>
  <td class="cell-left">${c['attributes'][typ1_text] or ''}</td>
</tr>
<tr>
  <td class="cell-left">${c['attributes'][typ2_text] or ''}</td>
</tr>
<tr>
  <td class="cell-left">${c['attributes'][typ3_text] or ''}</td>
</tr>
<tr>
  <td class="cell-left">${c['attributes'][typ4_text] or ''}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.linkdownload')}</td>
  <td class="cell-left" colspan="4"><a href="${c['attributes'][download_link] or '-'}" target="_blank">${_('link')}</a></td>
</tr>

<tr style="height: 10px;"><td></td></tr>

<tr>
  <td class="cell-left">Quickview</td>
  <td class="cell-left" colspan="4">
      <img src="${getQuickviewLink(c['attributes']['linkbild'])}">
  </td>
</tr>

</%def>

