<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<% c['stable_id'] = True %>
    <tr><td class="cell-left">${t.Translator.translate('stationsname', lang)}</td>   <td>${c['attributes']['lhg_name']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('stationsnr', lang)}</td>     <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('aktuelle_daten', lang)}</td>
      % if lang in ('de', 'en', 'rm'):
           <td><a target="_blank" href="http://www.hydrodaten.admin.ch/de/${c['featureId']}.html">${_('url') or '-'}</a></td>
      % elif lang == 'fr':
           <td><a target="_blank" href="http://www.hydrodaten.admin.ch/fr/${c['featureId']}.html">${_('url') or '-'}</a></td>
      % elif lang == 'it':
           <td><a target="_blank" href="http://www.hydrodaten.admin.ch/it/${c['featureId']}.html">${_('url') or '-'}</a></td>
      % endif
    </tr>
</%def>
