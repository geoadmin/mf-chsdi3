<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it','en') else 'de'
  enersource_main = '%s_enersource_main' % lang
%>


<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.bfe.thermische-netze.name')}</td> <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.thermische-netze.operator')}</td><td>${c['attributes']['operator'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.thermische-netze.beginningofoperation')}</td><td>${c['attributes']['beginningofoperation'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.thermische-netze.power')}</td><td>${c['attributes']['power'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.thermische-netze.de_enersource_main')}</td><td>${c['attributes'][enersource_main] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.thermische-netze.feedback')}</td><td><a target="_blank" href="https://www.uvek-gis.admin.ch/BFE/storymaps/EE_ThermischeNetze_Feedback/?&name=${c['attributes']['name']}&place=${c['attributes']['place']}&long=${c['attributes']['x']}&lat=${c['attributes']['y']}&lang=${lang}">${_('ch.bfe.thermische-netze.sendfeedback')}</a></td></tr>

</%def>

<%def name="extended_info(c, lang)">

<%
  lang = lang if lang in ('fr','it','en') else 'de'
  energysource = '%s_energysource' % lang
  positionaccuracy = '%s_positionaccuracy' %lang
%>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.zip')}</td>
      <td>${c['attributes']['zip'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.place')}</td>
      <td>${c['attributes']['place'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.operator')}</td>
      <td>${c['attributes']['operator'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.operatoraddress')}</td>
      <td>${c['attributes']['operatoraddress'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.phone')}</td>
      <td>${c['attributes']['phone'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.web')}</td>
          % if c['attributes']['web'] == None:
            <td>-</td>
          % else:
            <td><a target="_blank" href=${c['attributes']['web']}>${c['attributes']['web']}</a></td>
          % endif
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.mail')}</td>
          % if c['attributes']['mail'] == None:
            <td>-</td>
          % else:
            <td><a target="_blank" href=mailto:${c['attributes']['mail']}>${c['attributes']['mail']}</a></td>
          % endif
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.beginningofoperation')}</td>
      <td>${c['attributes']['beginningofoperation'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.power')}</td>
      <td>${c['attributes']['power'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.energy')}</td>
      <td>${c['attributes']['energy'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.houseconnections')}</td>
      <td>${c['attributes']['houseconnections'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.netlength')}</td>
      <td>${c['attributes']['netlength'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.de_energysource')}</td>
      <td>${c['attributes'][energysource] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-meta">${_('ch.bfe.thermische-netze.de_positionaccuracy')}</td>
      <td>${c['attributes'][positionaccuracy] or '-'}</td>
    </tr>
  </table>
</%def>
