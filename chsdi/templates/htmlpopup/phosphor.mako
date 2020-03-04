<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td width='250'>${mod_translate.Translator.translate('ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor.phosphor', lang)}</td><td>${"%.5f"% c['attributes']['phosphor'] or '0'}</td></tr>
</%def>
