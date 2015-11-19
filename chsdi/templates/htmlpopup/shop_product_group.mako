<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
   lang = lang if lang in ('fr','it','en') else 'de'
   fid = c['featureId']
   webDavHost = request.registry.settings['webdav_host']
   image = webDavHost + '/swisstopoproducts/250/' + fid + '.jpg'
   scale = h.format_scale(c['attributes']['scale'])
   price = h.format_price(c['attributes']['price'])
   if c['attributes']['available'] == False :
     available = _('shop_availability')
   else :
     available = ""
%>

    <tr><td
    class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.number')}</td>
    <td>${c['attributes']['number']}</td>       <td rowspan="6"><img src="${image}" height="150" width="102" align="right"/></td></tr> 
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.name')}</td>     <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.scale')}</td>    <td>${scale}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.price')}</td>    <td>${price}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.release')}</td>  <td>${c['attributes']['release']}</td></tr>
    <tr height=50><td></td><td>${available}</td></tr>
</%def>
