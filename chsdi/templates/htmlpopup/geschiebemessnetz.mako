<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
%>
<tr><td class="cell-left">${_('gsch_n')}</td><td>${c['attributes']['gsch_n']}</td></tr>
<tr><td class="cell-left">${_('geologie_fr_de')}</td><td>${c['attributes']['geologie']}</td></tr>
<tr><td class="cell-left">${_('fluss')}</td><td>${c['attributes']['fluss']}</td></tr>
<tr><td class="cell-left">${_('station')}</td><td>${c['attributes']['station']}</td></tr>
<tr><td class="cell-left">${_('institut')}</td><td>${c['attributes']['institut']}</td></tr>
<tr><td class="cell-left">${_('amt')}</td><td>${c['attributes']['amt']}</td></tr>
<tr><td class="cell-left">${_('link')}</td>
    <td>
    % if c['attributes']['pdf_file']:
      <a href="https://dav0.bgdi.admin.ch/kogis_web/downloads/bafu/geschiebemessnetz/${c['attributes']['pdf_file']}" target="_blank">${_('link')}</a>
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
<th class="cell-left">${_('x')}</th>
<td>${int(c['attributes']['rechtswert']) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('y')}</th>
<td>${int(c['attributes']['hochwert']) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('gsch_n')}</th>
<td>${c['attributes']['gsch_n'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('lk')}</th>
<td>${c['attributes']['lk'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('lage')}</th>
    % if lang in ('fr','it'):
<td>${c['attributes']['lage_fr'] or '-'}</td>
    % else:
<td>${c['attributes']['lage_de'] or '-'}</td>
    %endif
</tr>
<tr>
<th class="cell-left">${_('fn')}</th>
<td>${c['attributes']['fn'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('hmax')}</th>
<td>${c['attributes']['hmax'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('hmin')}</th>
<td>${c['attributes']['hmin'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('hmed')}</th>
<td>${c['attributes']['hmed'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('exp')}</th>
<td>${c['attributes']['exp'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('form')}</th>
<td>${c['attributes']['form'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('geologie_fr_de')}</th>
<td>${c['attributes']['geologie'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('platz')}</th>
    % if lang in ('fr','it'):
<td>${c['attributes']['platz_fr'] or '-'}</td>
    % else:
<td>${c['attributes']['platz_de'] or '-'}</td>
    %endif
</tr>
<tr>
<th class="cell-left">${_('fluss')}</th>
<td>${c['attributes']['fluss'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('station')}</th>
<td>${c['attributes']['station'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('institut')}</th>
<td>${c['attributes']['institut'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('amt')}</th>
<td>${c['attributes']['amt'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('abteilung')}</th>
<td>${c['attributes']['abteilung'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('sektion')}</th>
<td>${c['attributes']['sektion'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('kontakt_name')}</th>
<td>${c['attributes']['kontakt_name'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('strasse_fr_de')}</th>
<td>${c['attributes']['strasse'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('plz_fr_de')}</th>
<td>${c['attributes']['plz'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('ort_fr_de')}</th>
<td>${c['attributes']['ort'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('sachbearb')}</th>
<td>${c['attributes']['sachbearb'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('telephon_fr_de')}</th>
<td>${c['attributes']['telephon'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('fax')}</th>
<td>${c['attributes']['fax'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('emailadresse1')}</th>
<td>${c['attributes']['emailadresse1'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('emailadresse2')}</th>
<td>${c['attributes']['emailadresse2'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('link')}</th>
<td>
    % if c['attributes']['pdf_file']:
      <a href="https://dav0.bgdi.admin.ch/kogis_web/downloads/bafu/geschiebemessnetz/${c['attributes']['pdf_file']}" target="_blank">${_('link')}</a>
    % else:
      -
    % endif
</td>
</tr>
</table>
</%def>
