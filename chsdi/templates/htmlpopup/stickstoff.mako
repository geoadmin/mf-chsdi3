<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <tr><td width='250'>${mod_translate.Translator.translate('ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff.stickstoff', lang)}</td><td>${"%.5f"% c['attributes']['stickstoff'] or '0'}</td></tr>
</%def>
