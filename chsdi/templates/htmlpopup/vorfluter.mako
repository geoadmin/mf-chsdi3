# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
      <td class="cell-left-large">${h.translate('tezgnr40', lang)}</td>
      <td>${c['attributes']['teilezgnr'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left-large">${h.translate('klwkp_gwlnr', lang)}</td>
      <td>${c['attributes']['gwlnr'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left-large">${h.translate('tt_measure', lang)}</td>
      <td>${c['attributes']['measure'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left-large">${h.translate('tt_endmeasure', lang)}</td>
      <td>${c['attributes']['endmeasure'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left-large">${h.translate('gewaesser', lang)}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left-large">${h.translate('tt_regimenr', lang)}</td>
      <td>${c['attributes']['regimenr'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left-large">${h.translate('tt_regimetyp', lang)}</td>
      <td>${c['attributes']['regimetyp'] or '-'}</td>
    </tr>
</%def>
