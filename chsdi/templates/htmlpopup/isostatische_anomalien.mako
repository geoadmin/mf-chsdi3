<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td width="150" valign="top">${_('et_fromatt_anom')}</td><td>${c['attributes']['et_fromatt'] or '-'}</td></tr>
</%def>
