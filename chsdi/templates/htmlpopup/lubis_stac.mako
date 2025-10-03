<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
from chsdi.lib.helpers import resource_exists
import os

lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')

dataGeoAdminHost = request.registry.settings['datageoadminhost']
meta_csv_url = f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.csv"
preview_url = f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.jpg"

preview_exists = resource_exists(preview_url)
meta_csv_exists = resource_exists(meta_csv_url)
aerialimages_exists = resource_exists(c['attributes'].get('filename')) if c['attributes'].get('filename') else False
orthophoto_exists = resource_exists(c['attributes'].get('orthofilename')) if c['attributes'].get('orthofilename') else False
calibration_exists = resource_exists(c['attributes'].get('calibration')) if c['attributes'].get('calibration') else False

viewer_url = None
orthopotho_label = None
calibration_label = None
permalink_cog = None
if orthophoto_exists and c['attributes'].get('orthofilename'):
    permalink_cog = c['attributes'].get('orthofilename')
    orthophoto_label = os.path.basename(c['attributes'].get('orthofilename'))
elif aerialimages_exists:
    permalink_cog = c['attributes'].get('filename')
    viewer_url = f"{c['baseUrl']}/#/map?layers=COG|{c['attributes'].get('filename')}&lang={request.params.get('lang', 'de')}"

if permalink_cog:
    viewer_url = f"{c['baseUrl']}/#/map?layers=COG|{permalink_cog};{c['layerBodId']}@year=all@features={c['featureId']}&lang={request.params.get('lang', 'de')}"

if calibration_exists:
    calibration_label = os.path.basename(c['attributes'].get('calibration'))

fields = [
    ('id', 'featureId'),
    ('acquired', 'acquired'),
    ('film_type', 'filmart'),
    ('orthofilename', 'orthofilename'),
    ('e', 'e'),
    ('n', 'n'),
    ('z', 'z')
]
%>
% for label, attr in fields:
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.{label}")}</td>
  <td>
  % if label == 'orthofilename' and orthophoto_exists:
    <a href="${c['attributes'].get(attr) or '-'}" target="_blank">${orthophoto_label}</a>
  % elif label == 'id' and aerialimages_exists:
    <a href="${c['attributes'].get('filename') or '-'}" target="_blank">${c['featureId'] or '-'}</a>
  % else:
    ${c['attributes'].get(attr) or '-'}
  % endif
  </td>
</tr>
% endfor

<tr>
  <td class="cell-left">${_("zusatzinfo")}</td>
  <td>
  % if meta_csv_exists:
    <a href="${meta_csv_url}" target="_blank">${_(f"{c['layerBodId']}.meta_csv_url")}</a>
  % else:
    -
  % endif
  </td>
</tr>

<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.calibration")}</td>
  <td>
  % if calibration_exists:
    <a href="c['attributes'].get('calibration')" target="_blank">${calibration_label}</a>
  % else:
    -
  % endif
  </td>
</tr>

<tr>
  <td class="cell-left">${_("tt_lubis_Permalink")}</td>
  <td>
  % if viewer_url:
    <a href="${viewer_url}" target="_blank">
    % if preview_exists:
      <img src="${preview_url}" alt="${_('tt_lubis_permalink')}">
    % else:
      ${_("tt_lubis_permalink")}
    % endif
    </a>
  % else:
    ${_("ch.swisstopo.lubis.notiff")}
  % endif
  </td>
</tr>
</%def>
