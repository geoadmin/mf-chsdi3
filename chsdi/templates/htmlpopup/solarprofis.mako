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
        technologyheat = ('ch.bfe.solarprofis.technologyheat')
    else :
        technologyheat = '-'

    if c['attributes']['technologyelectricity'] == True:
        technologyelectricity = ('ch.bfe.solarprofis.technologyelectricity')
    else :
        technologyelectricity = '-'

    if c['attributes']['technologyconstruction'] == True:
        technologyconstruction = ('ch.bfe.solarprofis.technologyconstruction')
    else :
        technologyconstruction = '-'

    if c['attributes']['serviceconsultingplanning'] == True:
        serviceconsultingplanning = ('ch.bfe.solarprofis.serviceconsultingplanning')
    else :
        serviceconsultingplanning = '-'

    if c['attributes']['serviceimplementation'] == True:
        serviceimplementation = ('ch.bfe.solarprofis.serviceimplementation')
    else :
        serviceimplementation = '-'

    if c['attributes']['serviceproductiondistribution'] == True:
        serviceproductiondistribution = ('ch.bfe.solarprofis.serviceproductiondistribution')
    else :
        serviceproductiondistribution = '-'

    technology = technologyheat + ' / ' + technologyelectricity + ' / ' + technologyconstruction
    service = serviceconsultingplanning +  ' / ' + serviceconsultingplanning + ' / ' + serviceimplementation




%>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.company')}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.solarprofis.address')}</td>
        <td>${c['attributes']['address1'] or '-'}, ${c['attributes']['address2'] or '-'}</td>
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

