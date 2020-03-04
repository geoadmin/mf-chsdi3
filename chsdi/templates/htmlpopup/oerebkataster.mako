<%inherit file="base.mako"/>

<%!
import requests
import xml.etree.ElementTree as et
import re

def sanitise_url(url):
  """du to canton TI"""
  list_to_check=['getegrid','extract']
  for to_check in list_to_check:
    url = url.replace('//{}'.format(to_check), '/{}'.format(to_check))
  return url

def get_xml(path):
    list_egrid = []
    try:
      response = requests.get(path)
      if response.status_code == 200:
       root = et.fromstring(response.text)
       list_egrid = root.findall('{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid')
    except:
      pass
    return list_egrid

%>
<%def name="table_body(c,lang)">
<%
path_xml = "/getegrid/xml/?XY="
if not 'oereb_webservice' in c['attributes'].keys():
  c['attributes']['oereb_webservice'] = None
  c['attributes']['bgdi_status'] = None
else:
  path_pdf = sanitise_url("{}/extract/reduced/pdf/".format(c['attributes']['oereb_webservice']))
request = context.get('request')
coord = request.params.get('coord')

is_oereb_service = c['attributes']['oereb_webservice'] != None and c['attributes']['bgdi_status'] == 0 # is there a service available

if is_oereb_service:
  url_get_egrid = sanitise_url("{}{}{}".format(c['attributes']['oereb_webservice'], path_xml, coord))

  list_egrid = get_xml(url_get_egrid)
%>
    <tr><td class="cell-left">${mod_translate.Translator.translate('kanton', lang)}</td>    <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('gemgemeinde', lang)}</td>    <td>${c['attributes']['gemeindename'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('oereb_status', lang)}</td>
% if lang == 'de':
     <td>${c['attributes']['oereb_status_de'] or '-'}</td></tr>
% elif lang == 'fr':
     <td>${c['attributes']['oereb_status_fr'] or '-'}</td></tr>
% elif lang == 'it':
     <td>${c['attributes']['oereb_status_it'] or '-'}</td></tr>
% elif lang == 'en':
     <td>${c['attributes']['oereb_status_en'] or '-'}</td></tr>
% elif lang == 'rm':
     <td>${c['attributes']['oereb_status_rm'] or '-'}</td></tr>
% endif
    <tr><td class="cell-left">${mod_translate.Translator.translate('oereb_firma', lang)}</td>    <td>${c['attributes']['firmenname'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('grundadresse', lang)}</td>
      % if c['attributes']['ort'] == None:
       <td>-</td>
      % else:
        <td>${c['attributes']['adresszeile']} <br>
            ${c['attributes']['plz']} ${c['attributes']['ort']}
        </td>
      % endif
    </tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('grundtel', lang)}</td>    <td>${c['attributes']['telefon'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('Email', lang)}</td>
      % if c['attributes']['email'] == None:
       <td>-</td>
      % elif "@" in c['attributes']['email']:
           <td><a href="mailto:${c['attributes']['email']}">${_(c['attributes']['email']) or '-'}</a></td>
      % else:
       <td>-</td>
      % endif
    </tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('gemdarstellung', lang)}</td>
      % if c['attributes']['url_oereb'] == None:
       <td>-</td>
      % else:
         <td><a target="_blank" href="${c['attributes']['url_oereb']}">${mod_translate.Translator.translate('link', lang)}</a></td>
      % endif
    </tr>
    % if is_oereb_service:
      % for egrid in list_egrid:
        <tr>
            <td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo-vd.stand-oerebkataster.oereb_webservice', lang)}</td>
            <td><a target="_blank" href="${path_pdf}${egrid.text}">PDF (${egrid.text})</a></td>
        </tr>
      % endfor
    % endif
</%def>
