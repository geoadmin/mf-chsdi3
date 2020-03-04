<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>


<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.gewaessertyp', lang)}</td>     <td>${c['attributes']['gewaessertyp']}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.hoehe', lang)}</td>            <td>${c['attributes']['hoehe'] or '-'}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.abfluss', lang)}</td>          <td>${c['attributes']['abfluss'] or '-'}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.gefaelle', lang)}</td>         <td>${c['attributes']['gefaelle'] or '-'}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.geo', lang)}</td>              <td>${c['attributes']['geo'] or '-'}</td></tr>
<%
    from chsdi.lib.helpers import resource_exists
    dataPath = 'ch.bafu.typisierung-fliessgewaesser/PDF'
    pdf = None
    if c['attributes']['url_portraits'] is not None:
        dataGeoAdminHost = request.registry.settings['datageoadminhost']
        url_pdf = "https://" + dataGeoAdminHost + "/" + dataPath + "/" + c['attributes']['url_portraits']
        pdf = resource_exists(url_pdf)
%>
<tr>
  <td class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.url_portraits', lang)}</td>
  <td>
% if pdf:
    <a href="${url_pdf}" target="_blank">${c['attributes']['url_portraits']}</a></td>
% else:
    -
% endif
</td>
</tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    from chsdi.lib.helpers import resource_exists
    dataPath = 'ch.bafu.typisierung-fliessgewaesser/PDF'
    lang = 'fr' if lang in ('fr', 'it') else 'de'
    url_uebersicht = 'url_uebersicht_%s' % lang
    quali = 'quali_%s' % lang[0]
    dataGeoAdminHost = request.registry.settings['datageoadminhost']

    pdf = None
    pdf_legend = None

    if c['attributes']['url_portraits'] is not None:
        url_pdf = "https://" + dataGeoAdminHost + "/" + dataPath + "/" + c['attributes']['url_portraits']
        pdf = resource_exists(url_pdf)
    if c['attributes'][url_uebersicht] is not None:
        url_legend_pdf = "https://" + dataGeoAdminHost + "/" + dataPath + "/" + c['attributes'][url_uebersicht]
        pdf_legend = resource_exists(url_legend_pdf)
%>

<table class="table-with-border kernkraftwerke-extended">
<colgroup>
   <col width=20%>
   <col width=30%>
   <col width=20%>
   <col width=30%>
</colgroup>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.gewaessertyp', lang)}</th>
<td>${c['attributes']['gewaessertyp'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.grosserfluss', lang)}</th>
<td>${c['attributes']['grosserfluss'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.biogeo', lang)}</th>
<td>${c['attributes']['biogeo'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.hoehe', lang)}</th>
<td>${c['attributes']['hoehe'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.abfluss', lang)}</th>
<td>${c['attributes']['abfluss'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.gefaelle', lang)}</th>
<td>${c['attributes']['gefaelle'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.geo', lang)}</th>
<td>${c['attributes']['geo'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.code', lang)}</th>
<td>${c['attributes']['code'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.objectid_gwn25', lang)}</th>
<td>${c['attributes']['objectid_gwn25'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.aehnlichkeit', lang)}</th>
<td>${c['attributes']['aehnlichkeit'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.shape_length', lang)}</th>
% if c['attributes']['shape_length']:
    <td>${round(c['attributes']['shape_length'],3) or '-'}</td>
% else:
    <td>-</td>
% endif
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.url_portraits', lang)}</th>
% if pdf:
<td><a href="${url_pdf}" target="_blank">${c['attributes']['url_portraits'] or '-'}</a></td>
% else:
<td>-</td>
% endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.url_uebersicht', lang)}</th>
% if pdf_legend:
<td><a href="${url_legend_pdf}" target="_blank">${c['attributes'][url_uebersicht] or '-'}</a></td>
% else:
<td>-</td>
% endif
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.name', lang)}</th>
<td>${c['attributes']['name'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.discharge', lang)}</th>
<td>${c['attributes']['discharge'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.discharge_source', lang)}</th>
% if c['attributes']['discharge_source']=='GAB_EZGG_CH':
<td>${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.discharge_source.gab_ezgg_ch', lang)}</td>
% elif  c['attributes']['discharge_source']=='MQ_GWN_CH':
<td>${_('ch.bafu.typisierung-fliessgewaesser.discharge_source.mq_gwn_ch')|n}</td>
% else:
<td>-</td>
% endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.discharge_quality', lang)}</th>
% if c['attributes']['discharge_quality']==1:
<td>${_('ch.bafu.typisierung-fliessgewaesser.discharge_quality_1')|n}</td>
% elif  c['attributes']['discharge_quality']==2:
<td>${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.discharge_quality_2', lang)}</td>
% elif  c['attributes']['discharge_quality']==3:
<td>${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.discharge_quality_3', lang)}</td>
% else:
<td>-</td>
% endif
<th></th>
<td></td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.slope', lang)}</th>
<td>${c['attributes']['slope'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.slope_quality', lang)}</th>
% if c['attributes']['slope_quality']==1:
<td>${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.slope_quality_1', lang)}</td>
% elif  c['attributes']['slope_quality']==2:
<td>${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.slope_quality_2', lang)}</td>
% else:
<td>-</td>
% endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.ibchqregim', lang)}</th>
<td>${c['attributes']['ibchqregim'] or '-'}</td>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.ibch_corr', lang)}</th>
<td>${c['attributes']['ibch_corr'] or '0'}</td>
</tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.typisierung-fliessgewaesser.quali_d', lang)}</th>
<td>${c['attributes'][quali] or '-'}</td>
<th class="cell-left">&nbsp;</th>
<td>&nbsp;</td>
</tr>

</table>
</%def>
