<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

  <%
     lang = lang if lang in ('fr', 'it', 'en') else 'de'
     layerid = c['layerBodId']
  %>

<tr>
  <td class="cell-left">${_(layerid + '.name')}</td>
  <td>${c['attributes']['name'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_(layerid + '.standard')}</td>
  <td>${c['attributes']['standard'] or '-'}</td>
</tr>

</%def>


<%def name="extended_info(c, lang)">

  <%
     lang = lang if lang in ('fr', 'it', 'en') else 'de'
     layerid = c['layerBodId']
     standard = c['attributes']['standard']
  %>

<table class="table-with-border kernkraftwerke-extended" cellpadding="5">

  % if standard=='snbs_area' :
    % if lang=='it' :
    <tr><img class="image" src="https://api3.geo.admin.ch/featureattachments/ch.bfe.energiestaedte-nachhaltige_areale/svg/snbs_quartiere.svg" alt=""/></tr>
    % elif lang=='fr' :
    <tr><img class="image" src="https://api3.geo.admin.ch/featureattachments/ch.bfe.energiestaedte-nachhaltige_areale/svg/snbs_quartier.svg" alt=""/></tr>
    % else :
    <tr><img class="image" src="https://api3.geo.admin.ch/featureattachments/ch.bfe.energiestaedte-nachhaltige_areale/svg/snbs_areal.svg" alt=""/></tr>
    %endif
  % elif standard=='minergie_area' :
    % if lang=='it' :
    <tr><img class="image" src="https://api3.geo.admin.ch/featureattachments/ch.bfe.energiestaedte-nachhaltige_areale/svg/minergie_areal_it.svg" alt=""/></tr>
    % elif lang=='fr' :
    <tr><img class="image" src="https://api3.geo.admin.ch/featureattachments/ch.bfe.energiestaedte-nachhaltige_areale/svg/minergie_areal_fr.svg" alt=""/></tr>
    % else :
    <tr><img class="image" src="https://api3.geo.admin.ch/featureattachments/ch.bfe.energiestaedte-nachhaltige_areale/svg/minergie_areal_de.svg" alt=""/></tr>
    %endif
  % elif standard=='zweitausendwatt_area':
    % if lang=='it' :
    <tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-2000watt-areal/Sub-Logo_2000Watt_i.png" alt=""/></tr>
    % elif lang=='fr' :
    <tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-2000watt-areal/Sub-Logo_2000Watt_f.png" alt=""/></tr>
    % elif lang=='en' :
    <tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-2000watt-areal/Sub-Logo_2000Watt_e.png" alt=""/></tr>
    % else :
    <tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-2000watt-areal/Sub-Logo_2000Watt_d.png" alt=""/></tr>
    %endif
  % endif
  
  <tr>
    <th class="cell-meta">${_(layerid + '.name')}</th>
    <td>${c['attributes']['name'] or '-'}</td>
  </tr>

  <tr>
    <th class="cell-meta">${_(layerid + '.status')}</th>
    <td>${c['attributes']['status'] or '-'}</td>
  </tr>

  <tr>
    <th class="cell-meta">${_(layerid + '.ort')}</th>
    <td>${c['attributes']['gemeinde'] or '-'}</td>
  </tr>


  % if standard == 'snbs_area':

    <tr>
      <th class="cell-meta" colspan="2">
        ${_(layerid + '.text')}
      </th>
    </tr>

    <tr>
      <td class="cell-meta" colspan="2">
        <p align="justify">${_(layerid + '.text_snbs')}</p>
      </td>
    </tr>

    % if lang == 'it':
      <tr>
        <th class="cell-meta">${_(layerid + '.link')}</th>
        <td class="cell-meta">
          <a target="_blank"
              href="https://www.snbs-edificio.ch/standards/snbs-quartiere/">
            SNBS-Quartiere
          </a>
        </td>
      </tr>

    % elif lang == 'fr':
      <tr>
        <th class="cell-meta">${_(layerid + '.link')}</th>
        <td class="cell-meta">
          <a target="_blank"
              href="https://www.snbs-batiment.ch/standards/snbs-quartier/">
            SNBS-Quartier
          </a>
        </td>
      </tr>

    % else:
      <tr>
        <th class="cell-meta">${_(layerid + '.link')}</th>
        <td class="cell-meta">
          <a target="_blank"
              href="https://www.snbs-hochbau.ch/standards/snbs-areal/">
            SNBS-Areal
          </a>
        </td>
      </tr>

    % endif


  % elif standard == 'minergie_area':

    <tr>
      <th class="cell-meta" colspan="2">
         ${_(layerid + '.text')}
      </th>
     </tr>

     <tr>
       <td class="cell-meta" colspan="2">
         <p align="justify">${_(layerid + '.text_minergie')}</p>
      </td>
     </tr>

    % if lang == 'it':
       <tr>
         <th class="cell-meta">${_(layerid + '.link')}</th>
         <td class="cell-meta">
           <a target="_blank"
              href="https://www.minergie.ch/it/standard/nuove-costruzioni/minergie-quartiere/">
             Minergie-Quartiere
           </a>
        </td>
      </tr>
     % elif lang == 'fr':
      <tr>
        <th class="cell-meta">${_(layerid + '.link')}</th>
        <td class="cell-meta">
          <a target="_blank"
             href="https://www.minergie.ch/fr/standards/nouvelle-construction/minergie-quartier/">
            Minergie-Quartier
           </a>
        </td>
       </tr>
    % else:
       <tr>
        <th class="cell-meta">${_(layerid + '.link')}</th>
         <td class="cell-meta">
           <a target="_blank"
              href="https://www.minergie.ch/de/standards/neubau/minergie-areal/">
             Minergie-Areal
           </a>
         </td>
       </tr>
     % endif


  % elif standard == 'zweitausendwatt_area':

     <tr>
      <th class="cell-meta" colspan="2">
        ${_(layerid + '.text')}
      </th>
    </tr>

    <tr>
       <td class="cell-meta" colspan="2">
         <p align="justify">${_(layerid + '.text_2000w')}</p>
      </td>
     </tr>

     <tr>
      <th class="cell-meta">${_(layerid + '.link')}</th>
       <td>-</td>
    </tr>

   % endif

</table>

</%def>