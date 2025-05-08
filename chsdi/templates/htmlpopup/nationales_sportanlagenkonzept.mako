<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.baspo.nationales-sportanlagenkonzept.nasak_nr')}</td>                  <td>${c['attributes']['nasak_nr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.baspo.nationales-sportanlagenkonzept.kategorie_de')}</td>              <td>${c['attributes']['kategorie_de'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.baspo.nationales-sportanlagenkonzept.sportaktivitaet')}</td>           <td>${c['attributes']['sportaktivitaet'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.baspo.nationales-sportanlagenkonzept.name_der_anlage')}</td>           <td>${c['attributes']['name_der_anlage'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.baspo.nationales-sportanlagenkonzept.ort')}</td>                       <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.baspo.nationales-sportanlagenkonzept.website')}</td>
      % if c['attributes']['website']:
        <td><a target="_blank" href="http://${c['attributes']['website'].replace("http://","")}">${c['attributes']['website']}</a></td</tr>
      % else:
        <td>-</td></tr>
      % endif
</%def>
