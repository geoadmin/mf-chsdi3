<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td width="150" valign="top">${_('deklination')}</td><td>${c['attributes']['magne'] or '-'}</td></tr>
</%def>
