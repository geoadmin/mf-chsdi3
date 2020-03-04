<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    format = 'formate_%s' % lang
%>
    <tr><td class="cell-left">${mod_translate.Translator.translate('safety_zone', lang)}</td><td>${c['attributes']['zone_name']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('geometry_type', lang)}</td><td>${c['attributes']['zonetype_%s' % lang]}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('originator', lang)}</td><td>${c['attributes']['originator']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('kanton', lang)}</td><td>${c['attributes']['canton']}</td></tr>
</%def>

<%def name="extended_info(c, lang)"> 

<%
    import dateutil.parser as date_parser
    lang = lang if lang in ('fr','it') else 'de'
    format = 'formate_%s' % lang
    zone_description = c['attributes']['zone_description']
    try:
        aproval_date = date_parser.parse(c['attributes']['approval_date']).strftime('%d.%m.%Y')
    except ValueError:
        aproval_date = 'format error'
    try:
        zone_valid_from = date_parser.parse(c['attributes']['zone_valid_from']).strftime('%d.%m.%Y')
    except ValueError:
        zone_valid_from = 'format error'

%>
  <table>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('safety_zone', lang)}</td><td class="cell-meta-big">${c['attributes']['zone_name']}</td></tr>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('geometry_type', lang)}</td><td class="cell-meta-big">${c['attributes']['zonetype_%s' % lang]}</td></tr>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('originator', lang)}</td><td class="cell-meta-big">${c['attributes']['originator']}</td></tr>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('kanton', lang)}</td><td class="cell-meta-big">${c['attributes']['canton']}</td></tr>
<%
    municipality = c['attributes']['municipality']
    if municipality is not None:
        nb_municipality = ", ".join(c['attributes']['municipality'].split(','))
        i = 0
    else:
        municipality = 0
%>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('municipality', lang)}</td><td class="cell-meta-big">${nb_municipality}</td></tr>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('bazlrechtstatus', lang)}</td><td class="cell-meta-big">${c['attributes']['legalstatus_%s' % lang]}</td></tr>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('approval_date', lang)}</td><td class="cell-meta-big">${aproval_date}</td></tr>
    <tr><td class="cell-meta-small">${mod_translate.Translator.translate('ch.bazl.sicherheitszonenplan.SafetyZone.Valdity.ValidFrom', lang)}</td><td class="cell-meta-big">${zone_valid_from}</td></tr>
%   if zone_description:
        <tr><td class="cell-meta-small">${mod_translate.Translator.translate('ch.bazl.sicherheitszonenplan.SafetyZone.Valdity.Description', lang)}</td><td class="cell-meta-big">${zone_description}</td></tr>
%   endif

<%
     weblink = c['attributes']['weblink']
     if weblink:
      weblink = c['attributes']['weblink'].split('##')
      doctitle = c['attributes']['title'].split('##')
      nb=len(weblink)
      doctitle_new = []
      weblink_new = []
      todel = []
      i = 0
      while i < nb:
        if weblink[i] not in weblink_new:
          weblink_new.append(weblink[i])
          doctitle_new.append(doctitle[i])
        endif
        i = i+1
      arr_len = len(weblink_new)

     else:
      weblink_nb = 0
%>
% for i in range(arr_len):
<tr><td class="cell-meta-small">${mod_translate.Translator.translate('tt_document', lang)}</td> <td class="cell-meta-big"><a href=${weblink_new[i]}  target="_blank">${doctitle_new[i]}<a/></td></tr>
% endfor
</table>
</%def>
