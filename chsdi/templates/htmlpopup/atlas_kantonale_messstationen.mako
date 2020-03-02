<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.nummer', lang)}</td>
      <td>${c['attributes']['nummer'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.betriebsbeginn', lang)}</td>
      <td>${c['attributes']['betriebsbeginn'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.einzugsgebietsflaeche', lang)}</td>
      <td>${round(c['attributes']['einzugsgebietsflaeche'],2) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.bilanzgebietsnummer', lang)}</td>
      <td>${c['attributes']['bilanzgebietsnummer'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.vergletscherung', lang)}</td>
      <td>${c['attributes']['vergletscherung']}</td>
    </tr>
</%def>


<%def name="extended_info(c, lang)">

<table>
  <tr>
      <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.datenherkunft', lang)}</td>
      <td class="cell-meta">${c['attributes']['datenherkunft'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.nummer', lang)}</td>
    <td class="cell-meta">${c['attributes']['nummer'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.rechtswert', lang)}</td>
    <td class="cell-meta">${round(c['attributes']['rechtswert'],2) or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.hochwert', lang)}</td>
    <td class="cell-meta">${round(c['attributes']['hochwert'],2) or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.hoehe', lang)}</td>
    <td class="cell-meta">${round(c['attributes']['hoehe'],2) or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.betriebsbeginn', lang)}</td>
    <td class="cell-meta">${c['attributes']['betriebsbeginn'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.einzugsgebietsflaeche', lang)}</td>
    <td class="cell-meta">${round(c['attributes']['einzugsgebietsflaeche'],2) or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.bilanzgebietsnummer', lang)}</td>
    <td class="cell-meta">${c['attributes']['bilanzgebietsnummer'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologischer-atlas_kantonale-messstationen.vergletscherung', lang)}</td>
    <td class="cell-meta">${c['attributes']['vergletscherung']}</td>
  </tr>
</table>
</%def>
