<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang != 'rm' else 'de'
    layerBodId = c['layerBodId']
    accidenttype = 'accidenttype_%s' % lang
    accidentday = 'accidentday_%s' % lang
    accidentmonth = 'accidentmonth_%s' % lang
    severitycategory = 'severitycategory_%s' % lang
    roadtype = 'roadtype_%s' % lang
    pedestrian_yes_no = (layerBodId + '.yes') if c['attributes']['involving_pedestrian'] else (layerBodId + '.no')
    bicycle_yes_no = (layerBodId + '.yes') if c['attributes']['involving_bicycle'] else (layerBodId + '.no')
    motorcycle_yes_no = (layerBodId + '.yes') if c['attributes']['involving_motorcycle'] else (layerBodId + '.no')
%>
<% c['stable_id'] = True %>
      <td class="cell-left">${h.translate(layerBodId + '.accidenttype_de', lang)}</td>
      <td>${c['attributes'][accidenttype] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.severitycategory_de', lang)}</td>
      <td>${c['attributes'][severitycategory] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.accidentyear', lang)}</td>
      <td>${c['attributes']['accidentyear'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.accidentmonth_de', lang)}</td>
      <td>${c['attributes'][accidentmonth] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.accidentday_de', lang)}</td>
      <td>${c['attributes'][accidentday] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.accidenthour_text', lang)}</td>
      <td>${c['attributes']['accidenthour_text'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.roadtype_de', lang)}</td>
      <td>${c['attributes'][roadtype] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.canton', lang)}</td>
      <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.fsocommunecode', lang)}</td>
      <td>${c['attributes']['fsocommunecode'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.involving_pedestrian', lang)}</td>
      <td>${h.translate(pedestrian_yes_no, lang)}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.involving_bicycle', lang)}</td>
      <td>${h.translate(bicycle_yes_no, lang)}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate(layerBodId + '.involving_motorcycle', lang)}</td>
      <td>${h.translate(motorcycle_yes_no, lang)}</td>
    </tr>

</%def>

