<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr', 'it') else 'de'
    consultant_cat = 'consultant_cat_%s' % lang
    language = 'language_%s' % lang

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

    if c['attributes']['street_streetnumber']: arr_address.append(c['attributes']['street_streetnumber'])
    if c['attributes']['pc_place']: arr_address.append(c['attributes']['pc_place'])

    address = text_creator(arr_address)
%>
    <tr>
        <td class="cell-left">${t.translate('ch.bfe.erneuerbarheizen.company', lang)}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bfe.erneuerbarheizen.firstname_name', lang)}</td>
        <td>${c['attributes']['firstname_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bfe.erneuerbarheizen.email', lang)}</td>
          % if c['attributes']['email'] == None:
            <td>-</td>
          % else:
            <td><a href="mailto:${c['attributes']['email']}">${_(c['attributes']['email'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bfe.erneuerbarheizen.phonenumber', lang)}</td>
        <td>${c['attributes']['phonenumber'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bfe.erneuerbarheizen.pc_place', lang)}</td>
        <td>${address}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bfe.erneuerbarheizen.language', lang)}</td>
        <td>${c['attributes'][language] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.translate('ch.bfe.erneuerbarheizen.consultant_cat', lang)}</td>
        <td>${c['attributes'][consultant_cat] or '-'}</td>
    </tr>
</%def>

