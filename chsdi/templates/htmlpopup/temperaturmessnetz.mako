<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>

   <tr><td class="cell-left">${_('ch.bafu.hydrologie-wassertemperaturmessstationen.name')}</td>     <td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><td>${_('ch.bafu.hydrologie-wassertemperaturmessstationen.id')}</td>                         <td>${c['featureId'] or '-'()}</td></tr>
% if lang in ('de', 'en', 'rm') :
    <tr><td>${_('aktuelle_daten')}</td>    <td><a target="_blank" href="http://www.hydrodaten.admin.ch/de/${c['attributes']['url']}">${_('url') or '-'}</a></td></tr>
% else :
    <tr><td>${_('aktuelle_daten')}</td>    <td><a target="_blank" href="http://www.hydrodaten.admin.ch/${lang}/${c['attributes']['url']}">${_('url') or '-'}</a></td></tr>
% endif

</%def>

