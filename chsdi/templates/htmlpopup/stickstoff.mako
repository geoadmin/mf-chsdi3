<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td width='200'>${_('ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff.stickstoff')}</td><td>${c['properties']['stickstoff'] or '0'}</td></tr>
</%def>
