<%inherit file="base.mako"/>

<%!
import requests
import xml.etree.ElementTree as et
import re

def get_xml(path):
    list_egrid = []
    try:
      response = requests.get(path)
      if response.status_code == 200:
       # there are different namespaces from canton to canton -> remove namespace
       xmlstring = re.sub(r'\sxmlns[^"]+"[^"]+"', '', response.text)
       xmlstring = re.sub(r'\sxsi[^"]+"[^"]+"', '', xmlstring)
       root = et.fromstring(xmlstring)
       #egrid = root.find('{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid').text
       list_egrid = root.findall('.//egrid') # findall, as the cantons have different structures
    except:
      pass
    return list_egrid

%>
<%def name="table_body(c,lang)">
<%
path_pdf = "/extract/reduced/pdf/"
path_xml = "/getegrid/xml/?XY="
if not 'oereb_webservice' in c['attributes'].keys():
  c['attributes']['oereb_webservice'] = None
  c['attributes']['bgdi_status'] = None
request = context.get('request')
coord = request.params.get('coord')

is_oereb_service = c['attributes']['oereb_webservice'] != None and c['attributes']['bgdi_status'] == 0 # is there a service available

if is_oereb_service:
  url_get_egrid = "{}{}{}".format(c['attributes']['oereb_webservice'], path_xml, coord)
  list_egrid = get_xml(url_get_egrid)
%>
    <tr><td class="cell-left">${_('kanton')}</td>    <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('gemgemeinde')}</td>    <td>${c['attributes']['gemeindename'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('oereb_status')}</td>
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
    <tr><td class="cell-left">${_('oereb_firma')}</td>    <td>${c['attributes']['firmenname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('grundadresse')}</td>
      % if c['attributes']['ort'] == None:
       <td>-</td>
      % else:
        <td>${c['attributes']['adresszeile']} <br>
            ${c['attributes']['plz']} ${c['attributes']['ort']}
        </td>
      % endif
    </tr>
    <tr><td class="cell-left">${_('grundtel')}</td>    <td>${c['attributes']['telefon'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('Email')}</td>
      % if c['attributes']['email'] == None:
       <td>-</td>
      % elif "@" in c['attributes']['email']:
           <td><a href="mailto:${c['attributes']['email']}">${_(c['attributes']['email']) or '-'}</a></td>
      % else:
       <td>-</td>
      % endif
    </tr>
    <tr><td class="cell-left">${_('gemdarstellung')}</td>
      % if c['attributes']['url_oereb'] == None:
       <td>-</td>
      % else:
         <td><a target="_blank" href="${c['attributes']['url_oereb']}">${_('link')}</a></td>
      % endif
    </tr>
    % if is_oereb_service:
      % for egrid in list_egrid:
        <tr>
            <td class="cell-left">${_('ch.swisstopo-vd.stand-oerebkataster.oereb_webservice')}</td>
            <td><a target="_blank" href="${c['attributes']['oereb_webservice']}${path_pdf}${egrid.text}">PDF (${egrid.text})</a></td>
        </tr>
      % endfor
    % endif
</%def>
