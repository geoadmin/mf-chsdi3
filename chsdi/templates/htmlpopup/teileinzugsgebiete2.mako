<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
 <%
   lang = lang if lang in ('fr','it','en') else 'de'
   nebenarm = '%s_nebenarm' % lang
 %>
 <% c['stable_id'] = False %>
    <tr>
      <td class="cell-left">${_('ch.bafu.wasser-teileinzugsgebiete_2.ezgnr')}</td>
      <td>${c['attributes']['ezgnr'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.wasser-teileinzugsgebiete_2.gewaessername')}</td>
      <td>${c['attributes']['gewaessername'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.wasser-teileinzugsgebiete_2.gesamtflaeche')}</td>
      <td>${c['attributes']['gesamtflaeche'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.wasser-teileinzugsgebiete_2.de_nebenarm')}</td>
      <td>${c['attributes'][nebenarm] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_1')}</th>
    </tr>
  </table> 

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.min_z')}</tr>
      <td>${c['attributes']['min_z'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.max_z')}</tr>
      <td>${c['attributes']['max_z'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.mean_z')}</tr>
      <td>${c['attributes']['mean_z'] or '-'}</td>     
    </tr>
  </table>

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_2')}</th>
    </tr>
  </table>

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.anteil_ch')}</tr>
      <td>${c['attributes']['anteil_ch'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_siedlungsflaechen')}</tr>
      <td>${c['attributes']['as_siedlungsflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_landwirtschaftsflaechen')}</tr>
      <td>${c['attributes']['as_landwirtschaftsflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_bestockteflaechen')}</tr>
      <td>${c['attributes']['as_bestockteflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_unproduktiveflaechen')}</tr>
      <td>${c['attributes']['as_unproduktiveflaechen'] or '-'}</td>     
    </tr>
  </table>

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_3')}</th>
    </tr>
  </table>

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_bebauteflaechen')}</tr>
      <td>${c['attributes']['clc_bebauteflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_landwirtschaft')}</tr>
      <td>${c['attributes']['clc_landwirtschaft'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_waelder')}</tr>
      <td>${c['attributes']['clc_waelder'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_feuchtflaechen')}</tr>
      <td>${c['attributes']['clc_feuchtflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <tr class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_wasserflaechen')}</tr>
      <td>${c['attributes']['clc_wasserflaechen'] or '-'}</td>     
    </tr>
  </table>

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_4')}</th>
    </tr>
  </table>

</%def>
