<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
 <%
   c['stable_id'] = True
   lang = {'rm': 'de'}.get(lang, lang)
   sub_category = 'sub_category_' + lang
   plant_type = 'plant_type_' + lang
   orientation_lang = 'detail_orientation_' + lang
   list_orientation =  [elem for elem in c['attributes'][orientation_lang] if elem]
   orientation = ", ".join(str(element) for element in list_orientation)
   list_inclination = [elem for elem in c['attributes']['detail_inclination'] if elem]
   inclination = ", ".join(str(element) for element in list_inclination)
 %>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.sub_category')}</td>           <td>${c['attributes'][sub_category] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.address')}</td>                <td>${c['attributes']['address'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.egid')}</td>                   <td>${c['attributes']['egid'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.beginning_of_operation')}</td> <td>${c['attributes']['beginning_of_operation'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.initial_power')}</td>          <td>${c['attributes']['initial_power'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.total_power')}</td>            <td>${c['attributes']['total_power'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.plant_type')}</td>             <td>${c['attributes'][plant_type] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.orientation')}</td>            <td>${orientation or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bfe.elektrizitaetsproduktionsanlagen.inclination')}</td>            <td>${inclination or '-'}</td></tr>
</%def>
