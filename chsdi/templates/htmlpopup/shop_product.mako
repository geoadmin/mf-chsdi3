<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%

layer = c['layerBodId']
lang = lang if lang in ('fr','it','en') else 'de'
fid = str(c['featureId'])
cmsGeoadminHost = request.registry.settings['cmsgeoadminhost']
img_id = fid
if layer == 'ch.swisstopo.geologie-gravimetrischer_atlas.metadata':
    img_id = 'GRAV-DRG' + fid
elif layer == 'ch.swisstopo.stk200-papierkarte.metadata':
    img_id = 'Strassenkarte' + fid

image = cmsGeoadminHost + '/www.swisstopo.admin.ch/shop/swisstopoproducts/250/' + img_id + '.jpg'
if layer == 'ch.swisstopo.pixelkarte-pk25.metadata':
    image_exists = False
elif 'pk_product' not in c['attributes']:
    image_exists = h.resource_exists(image)
else:
    image_exists = False

name = 'name_%s' % lang
if 'scale' in c['attributes']:
    if c['attributes']['scale']:
        c['attributes']['scale'] = h.format_scale(c['attributes']['scale'])

layerTile = ['ch.swisstopo.images-swissimage.metadata', 
             'ch.swisstopo.pixelkarte-pk25.metadata',
             'ch.swisstopo.pixelkarte-pk50.metadata', 
             'ch.swisstopo.pixelkarte-pk100.metadata', 
             'ch.swisstopo.pixelkarte-pk200.metadata']

attr = []
attr_poss = ['number', name, 'mapsheetid', 'tileid', 'datenstand', 'scale', 'release', 'data', 'isbn', 'author', 'url_legend']
for ap in attr_poss:
    if ap in c['attributes']:
        if c['attributes'][ap]:
            attr.append(ap)
rowspan = len(attr) + 1
colspan = 3 if image_exists else 2

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
      % if layer in layerTile :
          <td class="cell-left">${_('ch.swisstopo.images-swissimage.metadata.%s' % a)}</td>
      % else: 
          <td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.%s' % a)}</td>   
      % endif
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
