<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.nummer')}</td>
      <td>${c['attributes']['nummer'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.betriebsbeginn')}</td>
      <td>${c['attributes']['betriebsbeginn'] or '-'}</td>
    </tr>
    <tr>
      % if c['attributes']['einzugsgebietsflaeche']:
          <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.einzugsgebietsflaeche')}</td>
          <td>${round(c['attributes']['einzugsgebietsflaeche'], 2)}</td>
      % else:
          <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.einzugsgebietsflaeche')}</td>
          <td>-</td>
      % endif
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.bilanzgebietsnummer')}</td>
      <td>${c['attributes']['bilanzgebietsnummer'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.vergletscherung')}</td>
      <td>${c['attributes']['vergletscherung']}</td>
    </tr>
</%def>


<%def name="extended_info(c, lang)">

<table>
  <tr>
      <td class="cell-meta">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.datenherkunft')}</td>
      <td class="cell-meta">${c['attributes']['datenherkunft'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.nummer')}</td>
    <td class="cell-meta">${c['attributes']['nummer'] or '-'}</td>
  </tr>
  <tr>
    % if c['attributes']['rechtswert']:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.rechtswert')}</td>
      <td>${round(c['attributes']['rechtswert'], 2)}</td>
    % else:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.rechtswert')}</td>
      <td>-</td>
    % endif
  </tr>
  <tr>
    % if c['attributes']['hochwert']:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.hochwert')}</td>
      <td>${round(c['attributes']['hochwert'], 2)}</td>
    % else:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.hochwert')}</td>
      <td>-</td>
    % endif
  </tr>
  <tr>
    % if c['attributes']['hoehe']:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.hoehe')}</td>
      <td>${round(c['attributes']['hoehe'], 2)}</td>
    % else:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.hoehe')}</td>
      <td>-</td>
    % endif
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.betriebsbeginn')}</td>
    <td class="cell-meta">${c['attributes']['betriebsbeginn'] or '-'}</td>
  </tr>
  <tr>
    % if c['attributes']['einzugsgebietsflaeche']:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.einzugsgebietsflaeche')}</td>
      <td>${round(c['attributes']['einzugsgebietsflaeche'], 2)}</td>
    % else:
      <td class="cell-left">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.einzugsgebietsflaeche')}</td>
      <td>-</td>
    % endif
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.bilanzgebietsnummer')}</td>
    <td class="cell-meta">${c['attributes']['bilanzgebietsnummer'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bafu.hydrologischer-atlas_kantonale-messstationen.vergletscherung')}</td>
    <td class="cell-meta">${c['attributes']['vergletscherung']}</td>
  </tr>
</table>
</%def>
