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
#quickviewImage {
  border-radius: 0px;
  cursor: pointer;
  transition: 0.1s;
}

#quickviewImagemy:hover {
  opacity: 1.0;
}

.modal {
  display: none;
  position: fixed;
  z-index: 1;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

#caption {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  text-align: center;
  color: #ccc;
  padding: 10px 0;
  height: 150px;
}

.modal-content, #caption {  
  -webkit-animation-name: zoom;
  -webkit-animation-duration: 0.1s;
  animation-name: zoom;
  animation-duration: 0.1s;
}

@-webkit-keyframes zoom {
  from {-webkit-transform:scale(0)} 
  to {-webkit-transform:scale(1)}
}

@keyframes zoom {
  from {transform:scale(0)} 
  to {transform:scale(1)}
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.1s;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}

@media only screen and (max-width: 700px){
  .modal-content {
    width: 100%;
  }
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

<tr>
  <td class="cell-left">Quickview</td>
  <td class="cell-left" colspan="4">
    <a href="${c['attributes']['linkbild'] or '-'}" target="_blank">
      <img id="quickviewImage" src="${getQuickviewLink(c['attributes']['linkbild'])}" alt="${c['attributes']['linkbild']}">
    </a>
  </td>
</tr>  

<div id="qvModal" class="modal">
  <span class="close">&times;</span>
  <img class="modal-content" id="qvImg">
  <div id="caption"></div>
</div>

<script>
var modal = document.getElementById("qvModal");
var img = document.getElementById("quickviewImage");
var modalImg = document.getElementById("qvImg");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

var span = document.getElementsByClassName("close")[0];

span.onclick = function() { 
  modal.style.display = "none";
}
</script>

</%def>

