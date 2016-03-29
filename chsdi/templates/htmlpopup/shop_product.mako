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
    rowspan = len(attr) + 1
%>
% for a in attr:
  <tr style="height: 25px;">
  % if attr.index(a) == 0:
    <td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.%s' % a)}</td>
    <td>${c['attributes'][a]}</td>
    <td rowspan=${rowspan}><img src="${image}" height="150" width="102" align="right"></td>
  % else:
    <td valign="top" class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.%s' % a)}</td>
    <td valign="top">${c['attributes'][a]}</td>
  % endif
  </tr>
% endfor
  <tr style="height: 100%;">
    <td></td>
% if c['attributes']['available'] == False:
    <td valign="top">${_('shop_availability')}
% else:
    <td valign="top">
% endif
    </td>
  </tr>

</%def>
