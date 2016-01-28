<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
    fid = c['featureId']
    webDavHost = request.registry.settings['webdav_host']
    image = webDavHost + '/swisstopoproducts/250/' + fid + '.jpg'
    name = 's_title_%s' % lang
    if c['attributes']['scale']:
        c['attributes']['scale'] = h.format_scale(c['attributes']['scale'])
    if c['attributes']['price']:
        c['attributes']['price'] = h.format_price(c['attributes']['price'])
    attr = []
    attr_poss = ['number', 'name', 'scale', 'release', 'data', 'isbn', 'author', 'price']
    for ap in attr_poss:
        if ap in c['attributes']:
            if c['attributes'][ap]:
                attr.append(ap)
    rowspan = len(attr)
%>
% for a in attr:
  % if attr.index(a) == 0:
    <tr>
      <td height=10 class=\"cell-left\">${_('ch.swisstopo.lk25-papierkarte.metadata.%s' % a)}</td>
      <td>${c['attributes'][a]}</td> <td rowspan=${rowspan}><img src="${image}" height="150" width="102" align="right"></td>
    </tr>
  % else:
    <tr>
      <td valign="top" class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.%s' % a)}</td>
      <td valign="top">${c['attributes'][a]}</td>
    </tr>
  % endif
% endfor
% if c['attributes']['available'] == False:
  <tr><td></td><td valign="top">_('shop_availability')</td></tr>
% endif

</%def>
