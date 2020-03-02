<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
%>
<tr><td class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.gsch_n', lang)}</td><td>${c['attributes']['gsch_n'] or '-'}</td></tr>
<tr><td class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.geologie', lang)}</td><td>${c['attributes']['geologie'] or '-'}</td></tr>
<tr><td class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.fluss', lang)}</td><td>${c['attributes']['fluss'] or '-'}</td></tr>
<tr><td class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.station', lang)}</td><td>${c['attributes']['station'] or '-'}</td></tr>
<tr><td class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.institut', lang)}</td><td>${c['attributes']['institut'] or '-'}</td></tr>
<tr><td class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.amt', lang)}</td><td>${c['attributes']['amt'] or '-'}</td></tr>
<%
    dataGeoAdminHost = request.registry.settings['datageoadminhost']
    dataPath = 'ch.bafu.feststoffe-geschiebemessnetz/PDF'
    url_pdf = "https://" + dataGeoAdminHost + "/" + dataPath + "/" + c['attributes']['pdf_file']
%>
<tr><td class="cell-left">${Translator.translate('link', lang)}</td>
    <td>
    % if c['attributes']['pdf_file']:
      <a href="${url_pdf}" target="_blank">${Translator.translate('link', lang)}</a>
    % else:
      -
    % endif
     </td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
%>
<table class="table-with-border kernkraftwerke-extended">
<colgroup>
  <col width=50%>
  <col width=50%>
</colgroup>
<tr>
<th class="cell-left">${Translator.translate('x', lang)}</th>
<td>${int(c['attributes']['rechtswert']) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('y', lang)}</th>
<td>${int(c['attributes']['hochwert']) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.gsch_n', lang)}</th>
<td>${c['attributes']['gsch_n'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.lk', lang)}</th>
<td>${c['attributes']['lk'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.lage', lang)}</th>
    % if lang in ('fr','it'):
<td>${c['attributes']['lage_fr'] or '-'}</td>
    % else:
<td>${c['attributes']['lage_de'] or '-'}</td>
    %endif
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.fn', lang)}</th>
<td>${c['attributes']['fn'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.hmax', lang)}</th>
<td>${c['attributes']['hmax'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.hmin', lang)}</th>
<td>${c['attributes']['hmin'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.hmed', lang)}</th>
<td>${c['attributes']['hmed'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.exp', lang)}</th>
<td>${c['attributes']['exp'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.form', lang)}</th>
<td>${c['attributes']['form'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.geologie', lang)}</th>
<td>${c['attributes']['geologie'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.platz', lang)}</th>
    % if lang in ('fr','it'):
<td>${c['attributes']['platz_fr'] or '-'}</td>
    % else:
<td>${c['attributes']['platz_de'] or '-'}</td>
    %endif
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.fluss', lang)}</th>
<td>${c['attributes']['fluss'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.station', lang)}</th>
<td>${c['attributes']['station'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.institut', lang)}</th>
<td>${c['attributes']['institut'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ch.bafu.feststoffe-geschiebemessnetz.amt', lang)}</th>
<td>${c['attributes']['amt'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('abteilung', lang)}</th>
<td>${c['attributes']['abteilung'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('sektion', lang)}</th>
<td>${c['attributes']['sektion'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('kontakt_name', lang)}</th>
<td>${c['attributes']['kontakt_name'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('strasse_fr_de', lang)}</th>
<td>${c['attributes']['strasse'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('plz_fr_de', lang)}</th>
<td>${c['attributes']['plz'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('ort_fr_de', lang)}</th>
<td>${c['attributes']['ort'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('sachbearb', lang)}</th>
<td>${c['attributes']['sachbearb'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('telephon_fr_de', lang)}</th>
<td>${c['attributes']['telephon'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('fax', lang)}</th>
<td>${c['attributes']['fax'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('emailadresse1', lang)}</th>
<td>${c['attributes']['emailadresse1'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${Translator.translate('emailadresse2', lang)}</th>
<td>${c['attributes']['emailadresse2'] or '-'}</td>
</tr>
<tr>
<%
    from chsdi.lib.helpers import resource_exists
    pdf = None
    if c['attributes']['pdf_file'] is not None:
        dataGeoAdminHost = request.registry.settings['datageoadminhost']
        dataPath = 'ch.bafu.feststoffe-geschiebemessnetz/PDF'
        url_pdf = "https://" + dataGeoAdminHost + "/" + dataPath + "/" + c['attributes']['pdf_file']
        pdf = resource_exists(url_pdf)
%>
<th class="cell-left">${Translator.translate('link', lang)}</th>
<td>
    % if c['attributes']['pdf_file']:
      <a href="${url_pdf}" target="_blank">${Translator.translate('link', lang)}</a>
    % else:
      -
    % endif
</td>
</tr>
</table>
</%def>
