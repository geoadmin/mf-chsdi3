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

<style>
  * {
    margin: 0;
    padding: 0;
  }
  .imgbox {
    display: grid;
    height: 100%;
  }
  .center-fit {
    max-width: 100%;
    max-height: 100vh;
    margin: auto;
  }
</style>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.gmde')}</td>
  <td class="cell-left" colspan="4">${c['attributes']['gmde'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.swissnames')}</td>
  <td class="cell-left" colspan="4">${c['attributes']['swissnames'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.typ')}</td>
  <td class="cell-left"><div style='display: inline-block; padding: 0px;'>${c['attributes'][typ1_text] or ''}</div></td>
  <td class="cell-left"><div style='display: inline-block; padding: 0px;'>${c['attributes'][typ2_text] or ''}</div></td>
  <td class="cell-left"><div style='display: inline-block; padding: 0px;'>${c['attributes'][typ3_text] or ''}</div></td>
  <td class="cell-left"><div style='display: inline-block; padding: 0px;'>${c['attributes'][typ4_text] or ''}</div></td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.linkdownload')}</td>
  <td class="cell-left" colspan="4"><a href="${c['attributes'][download_link] or '-'}" target="_blank">${_('link')}</a></td>
</tr>

<tr style="height: 10px;"><td></td></tr>

<script>
function openQuickviewImage(image_url) { 
  window.open('_blank').document.write('<div class="imgbox"><img class="center-fit" src="' + image_url + '"></div>');
}
</script>

<tr>
  <td class="cell-left">Quickview</td>
  <td class="cell-left" colspan="4">
    <a href="#">
      <img src="${getQuickviewLink(c['attributes']['linkbild'])}" onclick="openQuickviewImage('${c['attributes']['linkbild']}');">
    </a>
  </td>
</tr>  

</%def>

