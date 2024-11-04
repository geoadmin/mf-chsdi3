<%inherit file="base.mako"/>

<%!
import datetime
from pyramid.url import route_url
import chsdi.lib.helpers as h
import markupsafe
# TODO python2 clean-up
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

def br(text):
    return text.replace('\n', markupsafe.Markup('<br />'))

def date_to_str(datum):
    try:
        return datetime.datetime.strptime(datum.strip(), "%Y%m%d").strftime("%d-%m-%Y")
    except:
        return request.translate('None') + request.translate('Datenstand')
%>

<%def name="table_body(c, lang)">
<%

tt_lubis_ebkey = c['layerBodId'] + '.' + 'id'
lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')
datum = date_to_str(c['attributes']['flugdatum'])
%>
<tr>
  <td class="cell-left">${_(tt_lubis_ebkey)}</td>
  <td>${c['featureId'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('tt_lubis_Flugdatum')}</td>
  <td>${datum or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('tt_lubis_Filmart')}</td>
  <td>${c['attributes']['filmart'] or '-'}</td>
</tr>

% if 'contact_image_url' in c['attributes'] and c['attributes']['contact_image_url']:
<tr>
  <td class="cell-left">${_('tt_lubis_url_canton')}</td>
  <td><a href="${c['attributes']['contact_image_url']}" target="_blank">${_('tt_lubis_url_canton')}</td>
</tr>
% endif

% if str(c['attributes'].get('doi_link', '-')).startswith('http'):
<tr>
  <td class="cell-left">${_('tt_lubis_Quickview')}</td>
  <td><a href="${c['attributes']['doi_link']}" target="_blank">${c['attributes']['doi_link']}</a></td></tr>
</tr>

% else:
<tr>
  <td class="cell-left">${_('tt_lubis_Quickview')}</td>
  <td>${_('tt_lubis_noQuickview')}</td>
</tr>
% endif

% if 'contact_web' in c['attributes']:
<tr>
  <th class="cell-left">${_('tt_lubis_bildorder')}</th>
  <td>
    ${c['attributes']['contact'] | br }
    <br/>
    ${c['attributes']['contact_email']}
    <br/>

% if  c['attributes']['contact_web'] != '-':
    <a href="${c['attributes']['contact_web']}" target="_blank">
% endif

    ${c['attributes']['contact_web']}

% if  c['attributes']['contact_web'] != '-':
    </a>
% endif

  </td>
</tr>
% endif
</%def>
