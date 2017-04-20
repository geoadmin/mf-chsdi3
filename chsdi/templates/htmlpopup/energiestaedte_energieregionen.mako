<%inherit file="base.mako"/> 

<%def name="table_body(c, lang)">
<tr>
  <td class="cell-left">${_('ch.bfe.energiestaedte-energieregionen.name')}</td>
  <td>${c['attributes']['name'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('status')}</td>
 % if c['attributes']['kategorie'] == 'ker1':
  <td>
    ${_('energiestadt_region_ker1')}
  </td>
 % elif c['attributes']['kategorie'] == 'ker2':
  <td>
    ${_('energiestadt_region_ker2')}
  </td>
 % elif c['attributes']['kategorie'] == 'ker3':
  <td>
    ${_('energiestadt_region_ker3')}
  </td>
 % endif
  </tr>
</%def>
<%def name="extended_info(c, lang)">
<table class="table-with-border kernkraftwerke-extended" cellpadding="5">
  <tr>
    <th class="cell-meta">
      ${_('ch.bfe.energiestaedte-energieregionen')}
    </th>
    <td>
      ${c['attributes']['name']}
    </td>
  </tr>
  <tr>
    <th class="cell-meta">
      ${_('status')}
    </th>
  % if c['attributes']['kategorie'] == 'ker1':
    <td>
      ${_('energiestadt_region_ker1')}
    </td>
  % elif c['attributes']['kategorie'] == 'ker2':
    <td>
      ${_('energiestadt_region_ker2')}
    </td>
  % elif c['attributes']['kategorie'] == 'ker3':
    <td>
      ${_('energiestadt_region_ker3')}
    </td>
  % endif
  </tr>
  <tr>
    <th class="cell-meta">
      ${_('bet_energiestaedte')}
    </th>
    <td>
      ${c['attributes']['bet_energiestaedte'] or '-'}
    </td>
  </tr>
  <tr>
    <th class="cell-meta" >
      ${_('bet_traegerverein')}
    </th>
    <td class="cell-meta">
      ${c['attributes']['bet_traegerverein'] or '-'}
    </td>
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
    <th class="cell-meta" colspan="2">
      ${_('kurzerklaerung')}
    </th>
  </tr>
  <tr>
  % if lang=='fr' :
    <td class="cell-meta" colspan="2"><p align="justify">
Le projet des Régions-Energie permet à des communes de mener une politique énergétique exemplaire au sens de la Stratégie énergétique 2050. Il encourage une planification et une promotion ciblées des énergies renouvelables et des mesures d’efficacité à l’échelle régionale. Les Régions-Energie peuvent poursuivre divers objectifs et stratégies à long terme allant de l’augmentation du degré d’auto-approvisionnement (remplacement des agents énergétiques fossiles importés) à l’exportation d’énergie ou de technologies par des entreprises locales. Les activités des Régions-Energie favorisent le développement économique régional et peuvent par exemple engendrer une plus-value régionale et la création d’emplois.<br />
<br />
Les Régions-énergie qui participent au programme d’encouragement «Région-énergie 2016-2019» opèrent via un organisme intercommunal, investissent dans des projets innovants et intègrent l’économie locale et la population à leurs activités.<br />
<br />
L’OFEN encourage des projets concrets et finance le suivi et le coaching par des conseillers spécialisés Région-énergie ainsi que le soutien accordé par l’antenne Région-énergie.<br />
<br />
Afin d’introduire le programme Région-énergie, l’OFEN a élaboré de 2012 à 2015 un programme de soutien limité dans le temps pour les régions intéressées.<br />
<br />
Pendant la réalisation du projet, les conseillers ont analysé l’économie énergétique du moment et les potentiels, en collaboration avec les communes concernées. A cet égard, <a href="http://www.energie-region.ch/fr/outil-de-bilan/" target="_blank">l’outil de bilan pour communes et régions</a> remanié permet, une fois toutes les données pertinentes saisies, d’établir un bilan spécifique à la région.<br />
    </p>
    </td>
  </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.energie-region.ch/fr/le-concept/">Région-Energie</a>
    </td>
  % elif lang=='it' :
    <td class="cell-meta" colspan="2"><p align="justify">
Il progetto «Regione-Energia» consente ai Comuni che vi partecipano di diventare regioni all'avanguardia nel settore energetico ai sensi della Strategia energetica 2050. In questo ambito vengono pianificate e promosse in modo mirato le energie rinnovabili e le misure di efficienza energetica a livello regionale. Le Regioni-Energia possono perseguire nel lungo periodo diversi obiettivi e strategie: dall’aumento del proprio grado di autoapprovvigionamento (mediante la sostituzione dei vettori energetici di origine fossile importati) all’esportazione di energia o tecnologia da parte delle aziende locali. Le attività delle Regioni-Energia rappresentano delle opportunità di sviluppo dell’economia regionale che a sua volta può creare valore aggiunto e nuovi posti di lavoro nella Regione.<br />
<br />
Le Regioni-Energia che partecipano al programma di sostegno «Regione-Energia 2016-2019» operano mediante un ente intercomunale, investono in progetti innovativi e coinvolgono nelle loro attività le imprese d’artigianato e commerciali locali e la popolazione.<br />
<br />
L'UFE promuove progetti concreti, finanzia l'accompagnamento e il coaching da parte di consulenti specializzati nell'ambito delle Regioni-Energia, nonché il sostegno ad opera del centro di competenza «Regione-Energia».<br />
<br />
Per lanciare il nuovo programma «Regione-Energia» nel 2012-2015, l’UFE ha elaborato misure di sostegno di durata limitata per le regioni interessate.<br />
<br />
Nel corso dello svolgimento del programma i consulenti, in collaborazione con i rispettivi Comuni, hanno effettuato un’analisi dell’economia energetica e dei potenziali. A tal fine si utilizza lo <a href="http://www.region-energie.ch/it/strumento-di-bilancio/" target="_blank">strumento rielaborato di bilancio per Comuni e regioni</a> con cui, dopo aver inserito tutti i dati rilevanti, può essere redatto il bilancio della regione.<br />
    </p>
    </td>
  </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.region-energie.ch/it/lidea/">Regione-Energia</a>
    </td>
  % elif lang=='en' :
    <td class="cell-meta" colspan="2"><p align="justify">
The Energy-Region concept is intended to enable the involved municipalities to evolve into progressive regions in accordance with Energy Strategy 2050. Here, renewable energy use and energy efficiency measures are planned and promoted in a targeted manner at the regional level. An Energy-Region can pursue different strategies and objectives over the long term. These may range from increasing the degree of autonomous supply (through the use of imported fossil-based fuels) through to energy and technology export by companies domiciled in the region. The activities of an Energy-Region represent opportunities for regional economic development which can give rise to local value-added and the creation of jobs.<br />
<br />
The energy regions participating in the SFOE’s “Energy Region 2016-2019” support programme operate on the basis of an inter-municipal patronage, invest in innovative projects and integrate local businesses and residents into their activities. The SFOE promotes specific projects and finances support and coaching provided by specialised Energy Region consultants, as well as support from the Energy Region coordination centre.<br />
<br />
In order to efficiently introduce its Energy Region programme, in the period from 2012 to 2015 the SFOE drew up a limited duration support programme for the involved regions.<br />
<br />
During the project implementation stage, together with the respective municipalities the consultants analysed the current situation and potentials of the energy industry. For this purpose a revised <a href="http://www.energie-region.ch/de/bilanzierungs-tool/" target="_blank">calculation tool for municipalities and regions</a> is now available that can be used for compiling a customised balance for a given region, based on all entered relevant data.<br />
    </p>
    </td>
  </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.energie-region.ch/de/die-idee/">Energy-Region</a>
    </td>
  % else :
    <td class="cell-meta" colspan="2"><p align="justify">
Das Konzept der Energie-Region ermöglicht es den beteiligten Gemeinden, sich im Energiebereich zu fortschrittlichen Regionen im Sinne der Energiestrategie 2050 zu entwickeln. Dabei werden erneuerbare Energien und Effizienzmassnahmen gezielt auf der Stufe der Region geplant und gefördert. Energie-Regionen können langfristig unterschiedliche Strategien und Ziele verfolgen. Diese reichen von der Erhöhung des eigenen Selbstversorgungsgrads (durch Ersatz von importierten fossilen Energieträgern) bis hin zum Energie- oder Technologie-Export durch ansässige Unternehmen. Die Aktivitäten von Energie-Regionen sind Chancen für eine regionalökonomische Entwicklung, welche zu regionaler Wertschöpfung und neuen Arbeitsplätzen führen können.<br />
<br />
Die beim BFE-Unterstützungsprogramm „Energie-Region 2016-2019“ teilnehmenden Energie-Regionen operieren über eine interkommunale Trägerschaft, investieren in innovative Projekte und binden das ansässige Gewerbe sowie Bevölkerung in ihre Aktivitäten ein.<br />
<br />
Das BFE fördert konkrete Projekten, finanziert Begleitung und Coaching durch spezialisierte Energie-Regionen-BeraterInnen sowie Unterstützung durch die Fachstelle Energie-Region.<br /><br />
Um das Programm „Energie-Region" einzuführen, erarbeitete das BFE 2012-2015 ein zeitlich limitiertes Unterstützungsprogramm für interessierte Regionen. Während der Projektdurchführung analysierten die Beraterinnen und Berater in Zusammenarbeit mit den jeweiligen Gemeinden die gegenwärtige Energiewirtschaft und die Potenziale. Dafür steht das <a href="http://www.energie-region.ch/de/bilanzierungs-tool/" target="_blank" überarbeitete Bilanzierungs-Tool für Gemeinden und Regionen</a>, mit welchem sich nach der Erfassung aller relevanten Daten eine auf die Region zugeschnittene Bilanz erstellen lässt, zur Verfügung.<br />
    </p>
    </td>
  </tr>
    <th class="cell-meta">
      ${_('link')}
    </th>
    <td class="cell-meta">
      <a target="_blank" href="http://www.energie-region.ch/de/die-idee/">Energie-Region</a>
    </td>
%endif
  </tr>
  % if lang=='fr' :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-energieregionen/Sub-Logo_Energieregion_f.png" alt=""/></tr>
  % elif lang=='it' :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-energieregionen/Sub-Logo_Energieregion_i.png" alt=""/></tr>
  % else :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-energieregionen/Sub-Logo_Energieregion_d.png" alt=""/></tr>
  % endif
</table>
</%def>
