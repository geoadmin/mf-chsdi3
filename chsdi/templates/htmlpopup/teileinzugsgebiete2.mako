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
 
<%
   lang = lang if lang in ('fr','it','en') else 'de'
   nebenarm = '%s_nebenarm' % lang
 %>

<body onload="init()">

%if c['attributes'][nebenarm]:

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${c['attributes'][nebenarm] or '-'}</th>
    </tr>
  </table>

%else:

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_1')}</th>
    </tr>
  </table> 
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.min_z')}</td>
      <td>${c['attributes']['min_z'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.max_z')}</td>
      <td>${c['attributes']['max_z'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.mean_z')}</td>
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
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.anteil_ch')}</td>
      <td>${c['attributes']['anteil_ch'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_siedlungsflaechen')}</td>
      <td>${c['attributes']['as_siedlungsflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_landwirtschaftsflaechen')}</td>
      <td>${c['attributes']['as_landwirtschaftsflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_bestockteflaechen')}</td>
      <td>${c['attributes']['as_bestockteflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_unproduktiveflaechen')}</td>
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
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_bebauteflaechen')}</td>
      <td>${c['attributes']['clc_bebauteflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_landwirtschaft')}</td>
      <td>${c['attributes']['clc_landwirtschaft'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_waelder')}</td>
      <td>${c['attributes']['clc_waelder'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_feuchtflaechen')}</td>
      <td>${c['attributes']['clc_feuchtflaechen'] or '-'}</td>     
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_wasserflaechen')}</td>
      <td>${c['attributes']['clc_wasserflaechen'] or '-'}</td>     
    </tr>
  </table>
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_4')}</th>
    </tr>
  </table>

%endif

</%def>
