<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

 <%
    lang = lang if lang in ('fr','it','en') else 'de'
    bezeichnung_kat = 'bezeichnung_kat_%s' % lang

 %>

<tr>
  <td class="cell-left">${Translator.translate('ch.bfe.energiestaedte-energieregionen.name', lang)}</td>
  <td>${c['attributes']['name'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${Translator.translate('ch.bfe.energiestaedte-energieregionen.kategorie', lang)}</td>
  <td>${c['attributes'][bezeichnung_kat] or '-'}</td>
</tr>
<tr>
</%def>
<%def name="extended_info(c, lang)">

  <%
     lang = lang if lang in ('fr','it','en') else 'de'
     bezeichnung_kat = 'bezeichnung_kat_%s' % lang
     projektportraittext = c['attributes']['projektportraittext_%s' % lang]
     projektportraitlink = c['attributes']['projektportraitlink_%s' % lang]
     projektportraittext_split = []
     projektportraitlink_split = []
     if projektportraittext is not None:
        projektportraittext_split = projektportraittext.split('###')
        projektportraitlink_split = projektportraitlink.split('###')

  %>

<table class="table-with-border kernkraftwerke-extended" cellpadding="5">
  <tr>
    <th class="cell-meta">
      ${Translator.translate('ch.bfe.energiestaedte-energieregionen.name', lang)}
    </th>
    <td>
      ${c['attributes']['name']}
    </td>
  </tr>
  <tr>
    <th class="cell-meta">
      ${Translator.translate('ch.bfe.energiestaedte-energieregionen.kategorie', lang)}
    </th>
    <td>
      ${c['attributes'][bezeichnung_kat] or '-'}
    </td>
  </tr>
  <tr>
    <th class="cell-meta">
      ${Translator.translate('ch.bfe.energiestaedte-energieregionen.beteiligtegemeinden', lang)}
    </th>
    <td>
      ${c['attributes']['beteiligtegemeinden'] or '-'}
    </td>
  </tr>
  <tr>
    <th class="cell-meta" colspan="2">
      ${Translator.translate('ch.bfe.energiestaedte-energieregionen.erklaerung', lang)}
    </th>
  </tr>
  <tr>
  % if lang=='fr' :
    <td class="cell-meta" colspan="2"><p align="justify">
Le projet des Régions-Energie permet à des communes de mener une politique énergétique exemplaire au sens de la Stratégie énergétique 2050. Il encourage une planification et une promotion ciblées des énergies renouvelables et des mesures d’efficacité à l’échelle régionale. Les Régions-Energie peuvent poursuivre divers objectifs et stratégies à long terme allant de l’augmentation du degré d’auto-approvisionnement (remplacement des agents énergétiques fossiles importés) à l’exportation d’énergie ou de technologies par des entreprises locales. Les activités des Régions-Energie favorisent le développement économique régional et peuvent par exemple augmenter la plus-value régionale et préserver des emploi.<br />
<br />
Les Régions-Energie qui participent au programme d’encouragement «Région-Energie 2016-2019» opèrent via un organisme intercommunal, investissent dans des projets innovants et intègrent l’économie locale et la population à leurs activités.<br />
<br />
L’OFEN encourage des projets concrets et finance le suivi et le coaching par des conseillers spécialisés Région-Energie ainsi que le soutien accordé par l’antenne Région-Energie. Le calculateur  <a href="https://www.local-energy.swiss/fr/profibereich/profi-instrumente/2000-watt-gesellschaft/gemeinden-und-staedte.html#/" target="_blank"> énergie et climats</a> mis à disposition permet en outre de calculer la consommation d’énergie et d’évaluer le potentiel des projets.<br />
     </p>
     </td>
   </tr>
   <th class="cell-meta">
    ${Translator.translate('ch.bfe.energiestaedte-energieregionen.erklaerungslink', lang)}
   </th>
    <td class="cell-meta">
    <a target="_blank" href="http://www.region-energie.ch">${Translator.translate('link', lang)}</a>
   </td>
  % elif lang=='it' :
    <td class="cell-meta" colspan="2"><p align="justify">
Il progetto «Regione-Energia» consente ai Comuni che vi partecipano di diventare regioni all'avanguardia nel settore energetico ai sensi della Strategia energetica 2050. In questo ambito vengono pianificate e promosse in modo mirato le energie rinnovabili e le misure di efficienza energetica a livello regionale. Le Regioni-Energia possono perseguire nel lungo periodo diversi obiettivi e strategie: dall’aumento del proprio grado di autoapprovvigionamento (mediante la sostituzione dei vettori energetici di origine fossile importati) all’esportazione di energia o tecnologia da parte delle aziende locali. Le attività delle Regioni-Energia rappresentano delle opportunità di sviluppo dell’economia regionale, cosa che può condurre a un incremento del valore aggiunto e a mantenere posti di lavoro nella regione.<br />
<br />
Le Regioni-Energia che partecipano al programma di sostegno «Regione-Energia 2016-2019» operano mediante un ente intercomunale, investono in progetti inno-vativi e coinvolgono nelle loro attività le imprese d’artigianato e commerciali locali e la popolazione.<br />
<br />
L'UFE promuove progetti concreti, finanzia l'accompagnamento e il coaching da parte di consulenti specializzati nell'ambito delle Regioni-Energia, nonché il sostegno da parte del centro di competenza «Regione-Energia». Inoltre, per fare un bilancio del consumo di energia e stimare il potenziale, è a disposizione  <a href="https://www.local-energy.swiss/it/profibereich/profi-instrumente/2000-watt-gesellschaft/gemeinden-und-staedte.html#/" target="_blank">il calcolatore dell’energia e del clima.</a><br />
    </p>
    </td>
  </tr>
   <th class="cell-meta">
    ${Translator.translate('ch.bfe.energiestaedte-energieregionen.erklaerungslink', lang)}
   </th>
    <td class="cell-meta">
    <a target="_blank" href="http://www.regione-energia.ch">${Translator.translate('link', lang)}</a>
   </td>
  % elif lang=='en' :
    <td class="cell-meta" colspan="2"><p align="justify">
Under the Energy Regions concept, the local councils in the programme can evolve into progressive regions in accordance with the 2050 Energy Strategy.Renewable energy use and energy efficiency measures are planned at regional level to best suit local needs. An Energy Region can pursue different strategies and objectives over the long term which may range from increasing the degree of autonomous supply (by replacing imported fossil-based fuels) through to energy and technology exports by local companies. An Energy Region’s activities open up opportunities for regional economic development, giving rise to greater regional added value and preserving jobs in the region.<br />
<br />
The Energy Regions participating in the SFOE’s Energy Region 2016–2019 support programme operate under the auspices of an intercommunal umbrella body. They invest in innovative projects and encourage local businesses and residents to take part in their activities.<br />
<br />
The SFOE promotes specific projects and finances support and coaching provided by specialised Energy Region consultants. It alsofunds activities by the Energy Region Coordination Centre.  <a href="https://www.local-energy.swiss/profibereich/profi-instrumente/2000-watt-gesellschaft/gemeinden-und-staedte.html#/" target="_blank"> The Energy and Climate calculator</a> enables authorities to assess their energy use and potentials for efficiency and renewable energy use.<br />
    </p>
    </td>
  </tr>
   <th class="cell-meta">
    ${Translator.translate('ch.bfe.energiestaedte-energieregionen.erklaerungslink', lang)}
   </th>
    <td class="cell-meta">
    <a target="_blank" href="http://www.energie-region.ch">${Translator.translate('link', lang)}</a>
   </td>
  % else :
    <td class="cell-meta" colspan="2"><p align="justify">
Das Konzept der Energie-Region ermöglicht es den beteiligten Gemeinden, sich im Energiebereich zu fortschrittlichen Regionen im Sinne der Energiestrategie 2050 zu entwickeln. Dabei werden erneuerbare Energien und Effizienzmassnahmen gezielt auf der Stufe der Region geplant und gefördert. Energie-Regionen können langfristig unterschiedliche Strategien und Ziele verfolgen. Diese reichen von der Erhöhung des eigenen Selbstversorgungsgrads (durch Ersatz von importierten fossilen Energieträgern) bis hin zum Energie- oder Technologie-Export durch ansässige Unternehmen. Die Aktivitäten von Energie-Regionen sind Chancen für eine regionalökonomische Entwicklung, welche zu höherer regionaler Wertschöpfung und dem Erhalt von Arbeitsplätzen führen kann.<br />
<br />
Die beim BFE-Unterstützungsprogramm „Energie-Region 2016-2019“ teilnehmenden Energie-Regionen operieren über eine interkommunale Trägerschaft, investieren in innovative Projekte und binden das ansässige Gewerbe sowie Bevölkerung in ihre Aktivitäten ein.<br />
<br />
Das BFE fördert konkrete Projekte, finanziert Begleitung und Coaching durch spezialisierte Energie-Regionen-Beratende sowie Unterstützung durch die Fachstelle Energie-Region. Zudem steht <a href="https://www.local-energy.swiss/profibereich/profi-instrumente/2000-watt-gesellschaft/gemeinden-und-staedte.html#/" target="_blank">der Energie- und Klimakalkulator</a> für die Bilanzierung des Energieverbrauchs sowie für die Potenzialabschätzung zur Verfügung.<br />
<br />
   </p>
   </td>
   </tr>
   <th class="cell-meta">
    ${Translator.translate('ch.bfe.energiestaedte-energieregionen.erklaerungslink', lang)}
   </th>
    <td class="cell-meta">
    <a target="_blank" href="http://www.energie-region.ch">${Translator.translate('link', lang)}</a>
   </td>
 % endif
  </tr>
    <th class="cell-meta">
     ${Translator.translate('ch.bfe.energiestaedte-energieregionen.linkenergieregion', lang)}
  </th>
 % if c['attributes']['linkenergieregion'] is None:
   <td class="cell-meta"> - </td>
 % else:
   <td class="cell-meta">
     <a target="_blank" href="${c['attributes']['linkenergieregion']}">${Translator.translate('link', lang)}</a>
  </td>
 % endif
   </tr>
   <tr>
    <th class="cell-meta">
     ${Translator.translate('ch.bfe.energiestaedte-energieregionen.berater', lang)}
  </th>
 % if c['attributes']['mailberater'] is None:
   <td class="cell-meta"> - </td>
 % else:
   <td class="cell-meta">
     <a href="mailto:${c['attributes']['mailberater']}">${_(c['attributes']['berater']) or '-'}</a>
   </td>
 % endif
  </tr>
  <tr>
   <th class="cell-meta">
      ${Translator.translate('ch.bfe.energiestaedte-energieregionen.projektportrait', lang)}
  </th>
 % if len(projektportraitlink_split) > 0:
   <td class="cell-meta">
  % for i in range(len(projektportraitlink_split)):
    % if i > 0:
      <br/>
    % endif
      <a target="_blank" href="${projektportraitlink_split[i]}">${projektportraittext_split[i]}</a>
   % endfor
   </td>
 </tr>
 % else:
   <td class="cell-meta"> - </td>
 % endif
   <tr>
 % if lang=='fr' :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-energieregionen/Sub-Logo_Energieregion_f.png" alt=""/></tr>
 % elif lang=='it' :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-energieregionen/Sub-Logo_Energieregion_i.png" alt=""/></tr>
 % else :
<tr><img class="image" src="http://www.uvek-gis.admin.ch/BFE/bilder/ch.bfe.energiestaedte-energieregionen/Sub-Logo_Energieregion_d.png" alt=""/></tr>
 % endif
</table>
</%def>
