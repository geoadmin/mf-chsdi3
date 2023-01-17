<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  c['stable_id'] = True
  lang = {'rm': 'de'}.get(lang, lang)
  sub_category = 'sub_category_' + lang
  plant_type = 'plant_type_' + lang
%>
    <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.sub_category')}</td>           <td>${c['attributes'][sub_category] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.address')}</td>                <td>${c['attributes']['address'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.beginning_of_operation')}</td> <td>${c['attributes']['beginning_of_operation'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.initial_power')}</td>          <td>${c['attributes']['initial_power'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.total_power')}</td>            <td>${c['attributes']['total_power'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.plant_type')}</td>             <td>${c['attributes'][plant_type] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%

  lang = {'rm': 'de'}.get(lang, lang)
  main_category = 'main_category_' + lang
  sub_category = 'sub_category_' + lang
  plant_type = 'plant_type_' + lang
  detail_orientation = 'detail_orientation_' + lang
  detail_plant_type = 'detail_plant_type_' + lang

%>
  <table>
    <tr><th colspan=5>${_('ch.bfe.elektrizitaetsproduktionsanlagen.plant')}</th></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.address')}</td>                <td class="cell-meta" colspan=3>${c['attributes']['address'] or '-'}</td></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.canton')}</td>                 <td class="cell-meta" colspan=3>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.beginning_of_operation')}</td> <td class="cell-meta" colspan=3>${c['attributes']['beginning_of_operation'] or '-'}</td></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.initial_power')}</td>          <td class="cell-meta" colspan=3>${c['attributes']['initial_power'] or '-'}</td></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.total_power')}</td>            <td class="cell-meta" colspan=3>${c['attributes']['total_power'] or '-'}</td></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.main_category')}</td>          <td class="cell-meta" colspan=3>${c['attributes'][main_category] or '-'}</td></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.sub_category')}</td>           <td class="cell-meta" colspan=3>${c['attributes'][sub_category] or '-'}</td></tr>
    <tr><td colspan=2 class="cell-meta">${_('ch.bfe.elektrizitaetsproduktionsanlagen.plant_type')}</td>             <td class="cell-meta" colspan=3>${c['attributes'][plant_type] or '-'}</td></tr>
  </table>
</%def>
