<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
 % if lang == 'de' or lang == 'rm' or lang == 'en':
       <tr><td width="150" valign="top">${_('id_objekt')}</td><td>${c['attributes']['type_de'] or '-'}</td></tr>
      % elif lang == 'fr' or lang == 'it':
       <tr><td width="150" valign="top">${_('id_objekt')}</td><td>${c['attributes']['type_fr'] or '-'}</td></tr>
 % endif
</%def>
