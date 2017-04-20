<%inherit file="base.mako"/> 

<%def name="table_body(c, lang)">
<tr>
  <td class="cell-left">${_('ch.bfe.energiestaedte-2000watt-aufdemweg.name')}</td>
  <td>${c['attributes']['name'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('status')}</td>
 % if c['attributes']['kategorie'] == 'kew1':
  <td>
    ${_('energiestadt_auf_dem_weg_kew1')}
  </td>
 % elif c['attributes']['kategorie'] == 'kew2':
  <td>
    ${_('energiestadt_auf_dem_weg_kew2')}
  </td>
 % elif c['attributes']['kategorie'] == 'kew3':
  <td>
    ${_('energiestadt_auf_dem_weg_kew3')}
  </td>
 % elif c['attributes']['kategorie'] == 'kew4':
  <td>
    ${_('energiestadt_auf_dem_weg_kew4')}
  </td>
 % endif
  </tr>
</%def>
<%def name="extended_info(c, lang)">
<table class="table-with-border kernkraftwerke-extended" cellpadding="5">
  <tr>
    <th class="cell-meta">
      ${_('auf_dem_weg_gemeinde')}
    </th>
    <td>
      ${c['attributes']['name']}
    </td>
  </tr>
<tr>
  <th class="cell-meta">${_('status')}</th>
 % if c['attributes']['kategorie'] == 'kew1':
  <td>
    ${_('energiestadt_auf_dem_weg_kew1')}
  </td>
 % elif c['attributes']['kategorie'] == 'kew2':
  <td>
    ${_('energiestadt_auf_dem_weg_kew2')}
  </td>
 % elif c['attributes']['kategorie'] == 'kew3':
  <td>
    ${_('energiestadt_auf_dem_weg_kew3')}
  </td>
 % elif c['attributes']['kategorie'] == 'kew4':
  <td>
    ${_('energiestadt_auf_dem_weg_kew4')}
  </td>
 % endif
  </tr>
  <tr>
    <th class="cell-meta">
      ${_('berater')}
    </th>
  % if c['attributes']['linkberater'] is None:
    <td class="cell-meta"> - </td>
  % else:
    <td class="cell-meta">
      <a target="_blank" href="${c['attributes']['linkberater']}">${c['attributes']['berater']}</a>
    </td>
  % endif
  </tr>
  <tr>
    <th class="cell-meta">
      ${_('faktenblatt')}
    </th>
  % if c['attributes']['linkfaktenblatt'] is None:
    <td class="cell-meta"> - </td>
  % else:
    <td class="cell-meta">
       <a target="_blank" href="${c['attributes']['linkfaktenblatt']}">${_('link')}</a>
    </td>
  % endif
  </tr>
  <tr>
    <th class="cell-meta" colspan="2">
      ${_('kurzerklaerung')}
    </th>
  </tr>
  <tr>
  % if lang=='fr':
    <td class="cell-meta" colspan="2"><p align="justify">
La société à 2000 watts reflète la volonté de construire un avenir communautaire, équitable et attrayant. Cette stratégie est axée sur deux pôles: les besoins en énergie et les émissions de gaz à effet de serre. A moyen terme, chaque habitant ne devrait consommer durablement que 2000 watts d’énergie et ne produire qu’une tonne de CO2 par an. De nombreuses villes et communes se sont engagées au cours des dernières années à respecter ces objectifs et les ont intégrés à leurs directives de politique énergétique.<br />
<br />
<u>Label</u>: le label «Cité de l’énergie ouvrant la voie vers la société à 2000 watts» est octroyé aux Cités de l’énergie qui se distinguent par des objectifs visionnaires et exemplaires dans le cadre de la philosophie de la société à 2000 watts. Une version pilote du certificat a été établie en 2014 conjointement par l’Office fédéral de l’énergie et par l’association Cité de l’énergie.<br />
<a href="http://www.2000watt.ch/fr/pour-les-villes-et-les-communes/fit-pour-2000-watts/" target="_blank">http://www.2000watt.ch/fr/pour-les-villes-et-les-communes/fit-pour-2000-watts/</a><br />
<br />
<u>Communes pionnières</u>: ces dernières années, plusieurs villes et communes ont creusé l’idée d’une société à 2000 watts et ont marqué son développement de leur empreinte par leurs actions volontaristes et progressistes.<br />
<a href="http://www.2000watt.ch/fr/pour-les-villes-et-les-communes/retrospective-pionniers/" target="_blank">http://www.2000watt.ch/fr/pour-les-villes-et-les-communes/retrospective-pionniers/</a>
    </p></td>
    </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.2000watt.ch/fr/pour-les-villes-et-les-communes/">Cité de l'énergie vers 2000 watts</a>
    </td>
  % elif lang=='it':
    <td class="cell-meta" colspan="2"><p align="justify">
La società a 2000 Watt è il progetto di uno scenario futuro comune, equo e allettante. Gli indicatori principali su cui si basa sono il «fabbisogno energetico» e le «emissioni di CO2»: a medio termine ogni abitante potrà consumare 2000 Watt ed emettere 1 tonnellata di CO2 l'anno. Negli ultimi anni molti Comuni e città si sono impegnati a raggiungere gli obiettivi della società a 2000 Watt e li hanno integrati nelle loro direttive in materia di politica energetica.<br />
<br />
<u>Label</u>: il label «Città dell'energia verso la Società a 2000 Watt» è un riconoscimento che viene conferito a Città dell'energia selezionate per i loro obiettivi innovatori di ordine generale ai sensi della filosofia a 2000 Watt. Nel 2014 l'Ufficio federale dell'energia (UFE) e l'Associazione Città dell'energia hanno rilasciato una versione pilota del certificato.<br />
<br />
<a href="http://www.2000watt.ch/it/per-citta-e-comuni/in-forma-per-i-2000-watt/" target="_blank">http://www.2000watt.ch/it/per-citta-e-comuni/in-forma-per-i-2000-watt/</a><br />
<br />
<u>Città e Comuni pionieri</u>: negli ultimi anni, singole città e Comuni hanno dato un'impronta determinante e hanno contribuito allo sviluppo dell'idea di una società a 2000 Watt attraverso misure innovatrici e lungimiranti.<br />
<a href="http://www.2000watt.ch/it/per-citta-e-comuni/retrospettiva-i-pionieri/" target="_blank">http://www.2000watt.ch/it/per-citta-e-comuni/retrospettiva-i-pionieri/</a><br />
    </p></td>
    </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.2000watt.ch/it/per-citta-e-comuni/">Città dell’energia verso 2000 Watt</a>
    </td>
  % elif lang=='en' :
    <td class="cell-meta" colspan="2"><p align="justify">
The idea of a “2000-watt society” is a vision for a shared, just and attractive future. The concept focuses on the two central indicators, “energy demand” and “greenhouse gas emissions”. According to the defined vision, in the medium term each resident is entitled to a permanent energy consumption of 2000 watts and an annual level of CO2 emissions of not more than 1 tonne. In the past few years, a large number of municipalities and cities have undertaken a commitment to these 2000-watt goals and incorporated them into their energy policy guidelines.<br />
<br />
<u>Label</u>: The Energy City on the Path Towards a “2000-Watt Society” label is awarded to municipalities that pursue visionary overlying objectives in line with the 2,000-watt philosophy. The certificate was issued jointly in 2014 as a pilot version by the Swiss Federal Office of Energy and the Energy City Association.<br />
<a href="http://www.2000watt.ch/fuer-staedte-und-gemeinden/fit-fuer-2000-watt/" target="_blank">http://www.2000watt.ch/fuer-staedte-und-gemeinden/fit-fuer-2000-watt/</a><br />
<br />
<u>Pioneering approach</u>: In the past few years, a number of cities and municipalities have significantly influenced and codetermined the development of the 2000-watt concept through their progressive actions and forward-looking approach. <br />
<a href="http://www.2000watt.ch/fuer-staedte-und-gemeinden/rueckblick-pioniere/" target="_blank">http://www.2000watt.ch/fuer-staedte-und-gemeinden/rueckblick-pioniere/</a>
    </p></td>
    </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.2000watt.ch/de/fuer-staedte-und-gemeinden/">Energy Cities on the Path 2000-Watt</a>
    </td>
  % else :
    <td class="cell-meta" colspan="2"><p align="justify">
Die 2000-Watt-Gesellschaft ist eine Vision für eine gemeinschaftliche, gerechte und attraktive Zukunft. Der Fokus dieses Zukunftskonzepts liegt dabei auf den beiden Leitindikatoren «Energiebedarf» und «Treibhausgasemissionen». Jedem Einwohner und jeder Einwohnerin stehen demnach mittelfristig ein dauerhafter Energiebezug von 2000 Watt und die Emissionen von 1 Tonne CO2 pro Jahr zu. Viele Gemeinden und Städte haben sich in den letzten Jahren diesen 2000-Watt-Zielen verpflichtet und sie in ihre energiepolitischen Leitlinien integriert.<br />
<br />
<u>Label</u>: Das Label "Energiestadt auf dem Weg in die 2000-Watt-Gesellschaft" würdigt auserlesene Energiestädte für ihre visionären, übergeordneten Zielsetzungen im Sinne der 2000-Watt-Philosophie. Das Zertifikat wurde 2014 gemeinsam vom Bundesamt für Energie und vom Trägerverein Energiestadt in einer Pilot-Version ausgestellt.<br />
<a target="_blank" href="http://www.2000watt.ch/fuer-staedte-und-gemeinden/fit-fuer-2000-watt/">http://www.2000watt.ch/fuer-staedte-und-gemeinden/fit-fuer-2000-watt/</a><br />
<br />
<u>Pionier</u>: Einzelne Städte und Gemeinden haben die Entwicklung der 2000-Watt-Idee durch ihr fortschrittliches und vorausdenkendes Handeln in den letzten Jahren massgeblich mitgeprägt und mitgestaltet.<br />
<a target="_blank" href="http://www.2000watt.ch/fuer-staedte-und-gemeinden/rueckblick-pioniere/">http://www.2000watt.ch/fuer-staedte-und-gemeinden/rueckblick-pioniere/</a>
    </p></td> 
    </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.2000watt.ch/fuer-staedte-und-gemeinden/">Energiestädte auf dem Weg 2000-Watt</a>
    </td>
%endif
  </tr>
  % if lang=='fr' :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-2000watt-aufdemweg/Sub-Logo_2000Watt_f.png" alt=""/></tr>
  % elif lang=='it' :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-2000watt-aufdemweg/Sub-Logo_2000Watt_i.png" alt=""/></tr>
  % else :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-2000watt-aufdemweg/Sub-Logo_2000Watt_d.png" alt=""/></tr>
  % endif
</table>
</%def>
