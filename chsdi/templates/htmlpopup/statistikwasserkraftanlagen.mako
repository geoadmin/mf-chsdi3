<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% 
    c['stable_id'] = True
    lang = lang if lang in ('fr','it') else 'de'
    hydropowerplantoperationalstatus = 'hydropowerplantoperationalstatus_%s' % lang
    hydropowerplanttype = 'hydropowerplanttype_%s' % lang
%>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_wastanumber')}</td>
      <td>${c['featureId']}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_name')}</td>
      <td>${c['attributes']['name']}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_location')}</td>
      <td>${c['attributes']['location'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_canton')}</td>
      <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_hydropowerplantoperationalstatus_de')}</td>
      <td>${c['attributes'][hydropowerplantoperationalstatus] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_hydropowerplanttype')}</td>
      <td>${c['attributes'][hydropowerplanttype] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_beginningofoperation')}</td>
      <td>${c['attributes']['beginningofoperation'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('tt_ch.bfe.statistik-wasserkraftanlagen_endofoperation')}</td>
      <td>${c['attributes']['endofoperation'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left"></td>
      <td><a href="${c['baseUrl']}/${c['instanceId']}/rest/services/all/MapServer/${c['layerBodId']}/${c['featureId']}/extendedHtmlPopup" target="_blank">${_('zusatzinfo')}<img src="http://www.swisstopo.admin.ch/images/ico_extern.gif" /></a></td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    c['stable_id'] = True
    lang = 'de' if lang in ('de', 'rm', 'en') else lang
    import urllib2
    has_picture = True
    try:
        xml_file == urllib2.urlopen("http://dav0.bgdi.admin.ch/bfe_pub/images_wasserkraftanlagen/%d.jpg" % c['featureId'])
    except:
        has_picture = False

%>
<table>
  <tr>
    <td class="cell-meta-one" colspan="2"><h1>${_('wasserkraftanlagen')}&nbsp;${c['attributes']['name']}</h1></td>
  </tr>
  <tr>
    <td class="cell-meta-one" colspan="2">&nbsp;</td>
  </tr>
  <tr>
    <td class="cell-meta-one" colspan="2"><strong>${_('zentrale')}</strong></td>
  </tr>
  <tr>
    <td class="cell-meta">${_('name')}</td>
    <td class="cell-meta">${c['attributes']['name']}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('tt_ch.bfe.statistik-wasserkraftanlagen_wastanumber')}</td>
    <td class="cell-meta">${c['featureId']}</td>
  </tr>    
  <tr>
    <td class="cell-meta">${_('tt_ch.bfe.statistik-wasserkraftanlagen_location')}</td>
    <td class="cell-meta">${c['attributes']['location'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('kanton')}</td>
    <td class="cell-meta">${c['attributes']['canton'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('tt_ch.bfe.statistik-wasserkraftanlagen_hydropowerplantoperationalstatus_de')}</td>
    <td class="cell-meta">${c['attributes']['hydropowerplantoperationalstatus_%s' %lang] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('tt_ch.bfe.statistik-wasserkraftanlagen_hydropowerplanttype')}</td>
    <td class="cell-meta">${c['attributes']['hydropowerplanttype_%s' %lang] or '-'}</td>
  <tr>
    <td class="cell-meta">${_('tt_ch.bfe.statistik-wasserkraftanlagen_beginningofoperation')}</td>
    <td class="cell-meta">${c['attributes']['beginningofoperation'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('tt_ch.bfe.statistik-wasserkraftanlagen_endofoperation')}</td>
    <td class="cell-meta">${c['attributes']['endofoperation'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta-one" colspan="2">&nbsp;</td>
  </tr>
  <tr>
    <td class="cell-meta-one" colspan="2"><strong>${_('technische_angaben')}</strong></td>
  </tr>
  <tr>
    <td class="cell-meta">${_('leistung')}</td>
    <td class="cell-meta">${c['attributes']['leistung'] or '-'}&nbsp;MW</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('produktionserwartung')}</td>
    <td class="cell-meta">${c['attributes']['produktionserwartung'] or '-'}&nbsp;GWh</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('leistungsaufnahme_pumpen')}</td>
    <td class="cell-meta">${c['attributes']['leistungsaufnahme_pumpen'] or '-'}&nbsp;MW</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('energiebedarf_motoren')}</td>
    <td class="cell-meta">${c['attributes']['energiebedarf_motore'] or '-'}&nbsp;GWh</td>
  </tr>
  <tr>
    <td class="cell-meta-one" colspan="2">&nbsp;</td>
  </tr>
</table>
% if has_picture:
<div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls">
  <div class="slides"></div>
  <div class="title">${c['attributes']['name']}</div>
  <a class="prev">&lsaquo;</a>
  <a class="next">&rsaquo;</a>
  <a class="close">x</a>
  <a class="play-pause"></a>
  <ol class="indicator"></ol>
</div>
<div class="thumbnail-container">
  <div class="thumbnail">
    <a href="http://dav0.bgdi.admin.ch/bfe_pub/images_wasserkraftanlagen/${c['featureId']}.jpg">
      <img class="image" src="http://dav0.bgdi.admin.ch/bfe_pub/images_wasserkraftanlagen/${c['featureId']}.jpg" alt=""/>
    </a>
  </div>
</div>
<script>
$('.thumbnail-container').on('click', function (event) {
  event = event || window.event;
  var target = event.target || event.srcElement,
    link = target.src ? target.parentNode : target,
    options = {index: link, event: event},
    links = this.getElementsByTagName('a');
  blueimp.Gallery(links, options);
});
</script>
% endif
</%def>
