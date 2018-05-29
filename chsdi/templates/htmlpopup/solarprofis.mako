<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%c['stable_id'] = True %>

<%
    technologyheat = None
    technologyelectricity = None
    technologyconstruction = None
    serviceconsultingplanning = None
    serviceimplementation = None
    serviceproductiondistribution = None

    if c['attributes']['technologyheat'] == True:
        if c['attributes']['technologyelectricity'] == False and c['attributes']['technologyconstruction'] == False:
            technologyheat = _('ch.bfe.solarprofis.technologyheat')
        elif c['attributes']['technologyelectricity'] == True or c['attributes']['technologyconstruction'] == True:
            technologyheat = _('ch.bfe.solarprofis.technologyheat') + ', '
    else :
        technologyheat = ''

    if c['attributes']['technologyelectricity'] == True:
        if c['attributes']['technologyconstruction'] == True:
            technologyelectricity = _('ch.bfe.solarprofis.technologyelectricity') + ', '
        else :
            technologyelectricity = _('ch.bfe.solarprofis.technologyelectricity')
    else :
        technologyelectricity = ''

    if c['attributes']['technologyconstruction'] == True:
        technologyconstruction = _('ch.bfe.solarprofis.technologyconstruction')
    else :
        technologyconstruction = ''

    if c['attributes']['serviceconsultingplanning'] == True:
        if c['attributes']['serviceimplementation'] == True and c['attributes']['serviceproductiondistribution'] == True:
            serviceconsultingplanning = _('ch.bfe.solarprofis.serviceconsultingplanning')
        elif  c['attributes']['serviceimplementation'] == True or c['attributes']['serviceproductiondistribution'] == True:
            serviceconsultingplanning = _('ch.bfe.solarprofis.serviceconsultingplanning') + ', '
    else :
        serviceconsultingplanning = ''

    if c['attributes']['serviceimplementation'] == True:
        if c['attributes']['serviceproductiondistribution'] == True:
            serviceimplementation = _('ch.bfe.solarprofis.serviceimplementation') + ', '
        else:
            serviceimplementation = _('ch.bfe.solarprofis.serviceimplementation')
    else :
        serviceimplementation = ''

    if c['attributes']['serviceproductiondistribution'] == True:
        serviceproductiondistribution = _('ch.bfe.solarprofis.serviceproductiondistribution')
    else :
        serviceproductiondistribution = ''

    technology = technologyheat + technologyelectricity + technologyconstruction
    service = serviceconsultingplanning + serviceimplementation + serviceproductiondistribution

    if c['attributes']['technologyheat'] == False and c['attributes']['technologyelectricity'] == False and c['attributes']['serviceconsultingplanning'] == False:
        technology = '-'
    if c['attributes']['serviceconsultingplanning'] == False and c['attributes']['serviceimplementation'] == False and c['attributes']['serviceproductiondistribution'] == False:
        service = '-'


%>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.company')}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.address')}</td>
          % if c['attributes']['address1'] == None:
            <td>${c['attributes']['address2'] or '-'}</td>
          % elif c['attributes']['address2'] == None:
            <td>${c['attributes']['address1']}</td>
          % else:
            <td>${c['attributes']['address1']}, ${c['attributes']['address2']}</td>
          % endif
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

