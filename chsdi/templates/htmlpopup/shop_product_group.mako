<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%

   lang = lang if lang in ('fr','it','en') else 'de'
   fid = c['featureId']
   webDavHost = request.registry.settings['webdav_host']
   image = webDavHost + '/swisstopoproducts/250/' + fid + '.jpg'
   scale_str = str(c['attributes']['scale'])
   n = ""
   while len(scale_str)>3:
     scale_prov = int(scale_str)/1000
     n = n + "'000"
     scale_str = str(scale_prov)
   scale = "1:" + scale_str + n
   price_float = c['attributes']['price']/100.0
   price_2dec = format(price_float, '.2f')
   price = "CHF " + str(price_2dec)
   if c['attributes']['available'] == False :
     available = _('shop_availability')
   else:
     available = ""
%>

    <tr><td
    class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.number')}</td>
    <td>${c['attributes']['number']}</td>       <td rowspan="6"><img
    src="${image}" height="150" width="102" align="right"/></td></tr>
    <tr><td
    class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.name')}</td>
    <td>${c['attributes']['name']}</td></tr>
    <tr><td
    class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.scale')}</td>
    <td>${scale}</td></tr>
    <tr><td
    class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.price')}</td>
    <td>${price}</td></tr>
    <tr><td
    class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.release')}</td>
    <td>${c['attributes']['release']}</td></tr>
    <tr height=50><td></td><td>${available}</td></tr>
</%def>
