<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    layer = c['layerBodId']
    lang = lang if lang in ('fr','it','en') else 'de'
    fid = str(c['featureId'])
    webDavHost = request.registry.settings['webdav_host']
    image = webDavHost + '/swisstopoproducts/250/' + fid + '.jpg'
    if 'pk_product' not in c['attributes']:
        if h.resource_exists(image):
            image_exists = True
        else:
            image_exists = False
    else:
        image_exists = False
       
    name = 'name_%s' % lang
    if 'scale' in c['attributes']:
        if c['attributes']['scale']:
            c['attributes']['scale'] = h.format_scale(c['attributes']['scale'])
    
    attr = []
    attr_poss = ['number', name, 'scale', 'release', 'data', 'isbn', 'author', 'url_legend']
    for ap in attr_poss:
        if ap in c['attributes']:
            if c['attributes'][ap]:
                attr.append(ap)
    rowspan = len(attr) + 1
    if image_exists == True:
        colspan = 3
    else:
        colspan = 2

%>

<head>
  <style>
    .htmlpopup-content .image_mako {
      vertical-align: middle;
    }
    @media only screen and (max-width:480px) {
      .htmlpopup-content .image_mako {
        display: none;
      }
    }
  </style>
</head>

% for a in attr:
  <tr style="height: 25px;">
  % if attr.index(a) == 0:
    <td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.%s' % a)}</td>
    <td>${c['attributes'][a]}</td>
    % if image_exists == True:
        <td class="image_mako" rowspan=${rowspan}><img src="${image}" height="150" width="102" align="right"></td>
    % endif
  % else:
      % if a == 'url_legend':
          <td>${_('linkzurlegende')}</td>
          <td><a href="${c['attributes']['url_legend']}" target="_blank">${c['attributes'][name]}</a></td>
      % else:
          <td valign="top" class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.%s' % a)}</td>
          <td valign="top">${c['attributes'][a]}</td>
      % endif
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
