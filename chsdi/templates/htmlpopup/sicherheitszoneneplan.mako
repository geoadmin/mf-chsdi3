<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    format = 'formate_%s' % lang
%>
    <tr><td class="cell-left">${_('safety_zone')}</td><td>${c['attributes']['zone_name']}</td></tr>
    <tr><td class="cell-left">${_('geometry_type')}</td><td>${c['attributes']['zonetype_%s' % lang]}</td></tr>
    <tr><td class="cell-left">${_('originator')}</td><td>${c['attributes']['originator']}</td></tr>
    <tr><td class="cell-left">${_('kanton')}</td><td>${c['attributes']['canton']}</td></tr>
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
    <tr><td class="cell-meta-small">${_('safety_zone')}</td><td class="cell-meta-big">${c['attributes']['zone_name']}</td></tr>
    <tr><td class="cell-meta-small">${_('geometry_type')}</td><td class="cell-meta-big">${c['attributes']['zonetype_%s' % lang]}</td></tr>
    <tr><td class="cell-meta-small">${_('originator')}</td><td class="cell-meta-big">${c['attributes']['originator']}</td></tr>
    <tr><td class="cell-meta-small">${_('kanton')}</td><td class="cell-meta-big">${c['attributes']['canton']}</td></tr>
<%
    municipality = c['attributes']['municipality']
    if municipality is not None:
        nb_municipality = ", ".join(c['attributes']['municipality'].split(','))
        i = 0
    else:
        municipality = 0
%>
    <tr><td class="cell-meta-small">${_('municipality')}</td><td class="cell-meta-big">${nb_municipality}</td></tr>
    <tr><td class="cell-meta-small">${_('bazlrechtstatus')}</td><td class="cell-meta-big">${c['attributes']['legalstatus_%s' % lang]}</td></tr>
    <tr><td class="cell-meta-small">${_('approval_date')}</td><td class="cell-meta-big">${aproval_date}</td></tr>
    <tr><td class="cell-meta-small">${_('ch.bazl.sicherheitszonenplan.SafetyZone.Valdity.ValidFrom')}</td><td class="cell-meta-big">${zone_valid_from}</td></tr>
%   if zone_description:
        <tr><td class="cell-meta-small">${_('ch.bazl.sicherheitszonenplan.SafetyZone.Valdity.Description')}</td><td class="cell-meta-big">${zone_description}</td></tr>
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
<tr><td class="cell-meta-small">${_('tt_document')}</td> <td class="cell-meta-big"><a href=${weblink_new[i]}  target="_blank">${doctitle_new[i]}<a/></td></tr>
% endfor
</table>
</%def>
