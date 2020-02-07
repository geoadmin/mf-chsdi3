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
%if c['attributes']['min_z']:
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_1')}</th>
    </tr>
  </table> 
%endif

  <table class="table-with-border kernkraftwerke-extended">
%if c['attributes']['min_z']:   
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.min_z')}</td>
      <td>${c['attributes']['min_z'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['max_z']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.max_z')}</td>
      <td>${c['attributes']['max_z'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['mean_z']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.mean_z')}</td>
      <td>${c['attributes']['mean_z'] or '-'}</td>     
    </tr>
%endif

%if c['attributes']['min_z']:
  </table>
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_2')}</th>
    </tr>
  </table>
%endif

  <table class="table-with-border kernkraftwerke-extended">
%if c['attributes']['anteil_ch']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.anteil_ch')}</td>
      <td>${c['attributes']['anteil_ch'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['as_siedlungsflaechen']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_siedlungsflaechen')}</td>
      <td>${c['attributes']['as_siedlungsflaechen'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['as_landwirtschaftsflaechen']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_landwirtschaftsflaechen')}</td>
      <td>${c['attributes']['as_landwirtschaftsflaechen'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['as_bestockteflaechen']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_bestockteflaechen')}</td>
      <td>${c['attributes']['as_bestockteflaechen'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['as_unproduktiveflaechen']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.as_unproduktiveflaechen')}</td>
      <td>${c['attributes']['as_unproduktiveflaechen'] or '-'}</td>     
    </tr>
%endif
  </table>

%if c['attributes']['as_unproduktiveflaechen']:
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_3')}</th>
    </tr>
  </table>
%endif

  <table class="table-with-border kernkraftwerke-extended">
    <tr>
%if c['attributes']['clc_bebauteflaechen']:
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_bebauteflaechen')}</td>
      <td>${c['attributes']['clc_bebauteflaechen'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['clc_landwirtschaft']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_landwirtschaft')}</td>
      <td>${c['attributes']['clc_landwirtschaft'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['clc_waelder']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_waelder')}</td>
      <td>${c['attributes']['clc_waelder'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['clc_feuchtflaechen']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_feuchtflaechen')}</td>
      <td>${c['attributes']['clc_feuchtflaechen'] or '-'}</td>     
    </tr>
%endif
%if c['attributes']['clc_wasserflaechen']:
    <tr>
      <td class="cell-meta">${_('ch.bafu.wasser-teileinzugsgebiete_2.clc_wasserflaechen')}</td>
      <td>${c['attributes']['clc_wasserflaechen'] or '-'}</td>     
    </tr>
%endif
  </table>

%if c['attributes']['clc_wasserflaechen']:
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <th width="100%">${_('ch.bafu.wasser-teileinzugsgebiete_2.ext_info_4')}</th>
    </tr>
  </table>
%endif

</%def>
