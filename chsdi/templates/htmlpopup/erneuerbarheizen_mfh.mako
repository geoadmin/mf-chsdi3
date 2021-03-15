<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
  layer = c['layerBodId']
%>
<%
    lang = lang if lang in ('fr', 'it') else 'de' #TODO
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
        <td class="cell-left">${_(layer +'.company')}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer +'.firstname_name')}</td>
        <td>${c['attributes']['firstname_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer +'.email')}</td>
          % if c['attributes']['email'] == None:
            <td>-</td>
          % else:
            <td><a href="mailto:${c['attributes']['email']}">${_(c['attributes']['email'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${_(layer +'.phonenumber')}</td>
        <td>${c['attributes']['phonenumber'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer +'.addres')}</td>
        <td>${address}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer +'.language')}</td>
        <td>${c['attributes'][language] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer +'.consultant_cat')}</td>
        <td>${c['attributes'][consultant_cat] or '-'}</td>
    </tr>
</%def>

