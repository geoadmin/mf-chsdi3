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
%>
<% c['stable_id'] = True %>
      <td class="cell-left">${_(layerBodId + '.accidenttype_de')}</td>
      <td>${c['attributes'][accidenttype] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.severitycategory_de')}</td>
      <td>${c['attributes'][severitycategory] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.accidentyear')}</td>
      <td>${c['attributes']['accidentyear'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.accidentmonth_de')}</td>
      <td>${c['attributes'][accidentmonth] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.accidentday_de')}</td>
      <td>${c['attributes'][accidentday] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.accidenthour_text')}</td>
      <td>${c['attributes']['accidenthour_text'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.roadtype_de')}</td>
      <td>${c['attributes'][roadtype] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.canton')}</td>
      <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_(layerBodId + '.fsocommunecode')}</td>
      <td>${c['attributes']['fsocommunecode'] or '-'}</td>
    </tr>
% if c['attributes']['involving_pedestrian']:
    <tr>
      <td class="cell-left" colspan="2">${_(layerBodId + '.involving_pedestrian')}</td>
    </tr>
% endif
% if c['attributes']['involving_bicycle']:
    <tr>
      <td class="cell-left" colspan="2">${_(layerBodId + '.involving_bicycle')}</td>
    </tr>
% endif
% if c['attributes']['involving_motorcycle']:
    <tr>
      <td class="cell-left" colspan="2">${_(layerBodId + '.involving_motorcycle')}</td>
    </tr>
% endif

</%def>

