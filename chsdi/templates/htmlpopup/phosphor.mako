<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td width='250'>${_('ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor.phosphor')}</td><td>${"%.5f"% c['attributes']['phosphor'] or '0'}</td></tr>
</%def>
