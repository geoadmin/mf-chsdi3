<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%c['stable_id'] = True %>

<%
    arr_technology = []
    arr_service = []
    arr_address = []

    def text_creator(arr_titles):
        i = 0
        display_text = ''
        for el in arr_titles:
            if i == 0:
              display_text = el
            else:
              display_text += ', %s' % el
            i += 1
        if display_text == '': display_text = '-'
        return display_text

    if c['attributes']['technologyheat']: arr_technology.append(_('ch.bfe.solarprofis.technologyheat'))
    if c['attributes']['technologyelectricity']: arr_technology.append(_('ch.bfe.solarprofis.technologyelectricity'))
    if c['attributes']['technologyconstruction']: arr_technology.append(_('ch.bfe.solarprofis.technologyconstruction'))
    if c['attributes']['serviceimplementation']: arr_service.append(_('ch.bfe.solarprofis.serviceimplementation'))
    if c['attributes']['serviceproductiondistribution']: arr_service.append(_('ch.bfe.solarprofis.serviceproductiondistribution'))
    if c['attributes']['serviceconsultingplanning']: arr_service.append(_('ch.bfe.solarprofis.serviceconsultingplanning'))
    if c['attributes']['address1']: arr_address.append(c['attributes']['address1'])
    if c['attributes']['address2']: arr_address.append(c['attributes']['address2'])

    service = text_creator(arr_service)
    technology = text_creator(arr_technology)
    address = text_creator(arr_address)
%>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.company')}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.address')}</td>
        <td>${address}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.pc_place')}</td>
        <td>${c['attributes']['pc_place'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.telephonenumber')}</td>
        <td>${c['attributes']['telephonenumber'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.mail')}</td>
          % if c['attributes']['mail'] == None:
            <td>-</td>
          % else:
            <td><a href="mailto:${c['attributes']['mail']}">${_(c['attributes']['mail'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.webaddress')}</td>
          % if c['attributes']['webaddress'] == None:
            <td>-</td>
          % else:
            <td><a target="_blank" href="${c['attributes']['webaddress']}">${_(c['attributes']['webaddress'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.technologie')}</td>
        <td>${technology}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.service')}</td>
        <td>${service}</td>
    </tr>
</%def>

