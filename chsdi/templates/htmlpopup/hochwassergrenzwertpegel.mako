<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.name', lang)}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.einzugsgebietsflaeche', lang)}</td>
% if c['attributes']['einzugsgebietsflaeche']:
      <td>${round(c['attributes']['einzugsgebietsflaeche'],2) or '-'}</td>
% else:
    <td>-</td>
% endif
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.fluss', lang)}</td>
      <td>${c['attributes']['fluss'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.m_beginn', lang)}</td>
      <td>${c['attributes']['m_beginn']}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.m_ende', lang)}</td>
      <td>${c['attributes']['m_ende']}</td>
    </tr>
</%def>


<%def name="extended_info(c, lang)">

<table>
  <tr>
      <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.datenherkunft', lang)}</td>
      <td class="cell-meta">${c['attributes']['datenherkunft'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.nummer', lang)}</td>
    <td class="cell-meta">${c['attributes']['nummer'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.name', lang)}</td>
    <td class="cell-meta">${c['attributes']['name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.rechtswert', lang)}</td>
% if c['attributes']['rechtswert']:    
    <td class="cell-meta">${round(c['attributes']['rechtswert'],2) or '-'}</td>
% else:
    <td>-</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.hochwert', lang)}</td>
% if c['attributes']['hochwert']:
    <td class="cell-meta">${round(c['attributes']['hochwert'],2) or '-'}</td>
% else:
    <td>-</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.hoehe', lang)}</td>
% if c['attributes']['hoehe']:
    <td class="cell-meta">${round(c['attributes']['hoehe'],2) or '-'}</td>
% else:
    <td>-</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.einzugsgebietsflaeche', lang)}</td>
% if c['attributes']['einzugsgebietsflaeche']:    
    <td class="cell-meta">${round(c['attributes']['einzugsgebietsflaeche'],2) or '-'}</td>
% else:
    <td>-</td>
% endif
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.fluss', lang)}</td>
    <td class="cell-meta">${c['attributes']['fluss'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.m_beginn', lang)}</td>
    <td class="cell-meta">${c['attributes']['m_beginn']}</td>
  </tr>
  <tr>
    <td class="cell-meta">${t.Translator.translate('ch.bafu.hydrologie-hochwassergrenzwertpegel.m_ende', lang)}</td>
    <td class="cell-meta">${c['attributes']['m_ende']}</td>
  </tr>
</table>
</%def>
