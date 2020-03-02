<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>

<%
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

    if c['attributes']['address1']: arr_address.append(c['attributes']['address1'])
    if c['attributes']['address2']: arr_address.append(c['attributes']['address2'])
    if c['attributes']['postofficebox']: arr_address.append(c['attributes']['postofficebox'])

    address = text_creator(arr_address)
%>

    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.wpsm-qualifizierte_firmen.company', lang)}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.wpsm-qualifizierte_firmen.contactperson', lang)}</td>
        <td>${c['attributes']['contactperson'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.wpsm-qualifizierte_firmen.address', lang)}</td>
        <td>${address}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.wpsm-qualifizierte_firmen.pc_place', lang)}</td>
        <td>${c['attributes']['pc_place'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.wpsm-qualifizierte_firmen.telephonenumber', lang)}</td>
        <td>${c['attributes']['telephonenumber'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.wpsm-qualifizierte_firmen.mail', lang)}</td>
          % if c['attributes']['mail'] == None:
            <td>-</td>
          % else:
            <td><a href="mailto:${c['attributes']['mail']}">${_(c['attributes']['mail'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.wpsm-qualifizierte_firmen.webaddress', lang)}</td>
          % if c['attributes']['webaddress'] == None:
            <td>-</td>
          % else:
            <td><a target="_blank" href="${c['attributes']['webaddress']}">${_(c['attributes']['webaddress'])}</a></td>
          % endif
    </tr>
</%def>
