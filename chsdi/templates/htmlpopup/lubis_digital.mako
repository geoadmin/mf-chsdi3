<%inherit file="base.mako"/>

<%!
import datetime
%>

<%def name="table_body(c, lang)">
<%
from chsdi.lib.helpers import resource_exists

lang = lang if lang in ('fr', 'it', 'en') else 'de'
c['stable_id'] = True
request = context.get('request')

gori_asset = c['attributes'].get('bgdi_gori_asset')
gori_exists = resource_exists(gori_asset) if gori_asset else False

dataGeoAdminHost = request.registry.settings['datageoadminhost']
cog_asset = f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.tif"
cog_exists = resource_exists(cog_asset)
viewer_url = f"{c['baseUrl']}/#/map?layers={c['layerBodId']}@year=all@features={c['featureId']},f;COG|{cog_asset}&lang={request.params.get('lang', 'de')}"

capture_time = c['attributes'].get('capture_time')
if isinstance(capture_time, datetime.datetime):
    capture_time = capture_time.strftime('%d-%m-%Y')
elif isinstance(capture_time, str):
    try:
        capture_time = datetime.datetime.strptime(capture_time, '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y')
    except ValueError:
        pass

fields = [
    ('feature_id', c['featureId'] or '-'),
    ('capture_time', capture_time or '-'),
    ('easting', c['attributes'].get('easting') or '-'),
    ('northing', c['attributes'].get('northing') or '-'),
    ('altitude', c['attributes'].get('altitude') or '-')
]
%>
% for attr, value in fields:
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.{attr}")}</td>
  <td>${value}</td>
</tr>
% endfor

<tr>
  <td class="cell-left">${_('zusatzinfo')}</td>
  <td>
  % if gori_exists:
    <a href="${gori_asset}" target="_blank">${_(f"{c['layerBodId']}.bgdi_gori_asset")}</a>
  % else:
    -
  % endif
  </td>
</tr>

<tr>
  <td class="cell-left">${_('tt_lubis_Quickview')}</td>
  <td>
  % if cog_exists:
    <a href="${viewer_url}" target="_blank">${_('tt_lubis_Quickview')}</a>
  % else:
    ${_('tt_lubis_noQuickview')}
  % endif
  </td>
</tr>
</%def>
