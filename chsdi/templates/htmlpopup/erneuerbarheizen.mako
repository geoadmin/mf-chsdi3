<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr', 'it') else 'de'
    consultant_cat = '%s_consultant_cat' % lang
    language = '%s_language' % lang

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
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.company')}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.firstname_name')}</td>
        <td>${c['attributes']['firstname_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.email')}</td>
          % if c['attributes']['email'] == None:
            <td>-</td>
          % else:
            <td><a href="mailto:${c['attributes']['email']}">${_(c['attributes']['email'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.phonenumber')}</td>
        <td>${c['attributes']['phonenumber'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.pc_place')}</td>
        <td>${address}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.consultingcosts')}</td>
        % if c['attributes']['consultingcosts'] == None:
            <td>${_('ch.bfe.erneuerbarheizen.onrequest')}<td>
        % else:
            <td>${c['attributes']['consultingcosts']}</td>
        %endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.language')}</td>
        <td>${c['attributes'][language] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.erneuerbarheizen.consultant_cat')}</td>
        <td>${c['attributes'][consultant_cat] or '-'}</td>
    </tr>
</%def>

