<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td width="150" valign="top">${_('et_fromatt')}</td><td>${c['attributes']['et_fromatt'] or '-'}</td></tr>
</%def>
