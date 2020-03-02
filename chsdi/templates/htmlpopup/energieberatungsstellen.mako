<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%c['stable_id'] = True %>

<%
    lang = lang if lang in ('fr', 'it') else 'de'
    category = 'category_text_%s' % lang

    arr_client = []
    arr_topic = []
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

    if c['attributes']['clientprivatepersons']: arr_client.append(_('ch.bfe.energieberatungsstellen.clientprivatepersons'))
    if c['attributes']['clientcompanies']: arr_client.append(_('ch.bfe.energieberatungsstellen.clientcompanies'))
    if c['attributes']['clientmunicipalities']: arr_client.append(_('ch.bfe.energieberatungsstellen.clientmunicipalities'))
    if c['attributes']['topicbuildings']: arr_topic.append(_('ch.bfe.energieberatungsstellen.topicbuildings'))
    if c['attributes']['topicelectricdeviceslighting']: arr_topic.append(_('ch.bfe.energieberatungsstellen.topicelectricdeviceslighting'))
    if c['attributes']['topicmobility']: arr_topic.append(_('ch.bfe.energieberatungsstellen.topicmobility'))
    if c['attributes']['address1']: arr_address.append(c['attributes']['address1'])
    if c['attributes']['address2']: arr_address.append(c['attributes']['address2'])
    if c['attributes']['postofficebox']: arr_address.append(c['attributes']['postofficebox'])

    client = text_creator(arr_client)
    topic = text_creator(arr_topic)
    address = text_creator(arr_address)
%>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.name', lang)}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.management', lang)}</td>
        <td>${c['attributes']['management'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.category', lang)}</td>
        <td>${c['attributes'][category] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.address', lang)}</td>
        <td>${address}</td>
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.pc_place', lang)}</td>
        <td>${c['attributes']['pc_place'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.telephonenumber', lang)}</td>
        <td>${c['attributes']['telephonenumber'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.mail', lang)}</td>
          % if c['attributes']['mail'] == None:
            <td>-</td>
          % else:
            <td><a href="mailto:${c['attributes']['mail']}">${_(c['attributes']['mail'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.webaddress', lang)}</td>
          % if c['attributes']['webaddress'] == None:
            <td>-</td>
          % else:
            <td><a target="_blank" href="${c['attributes']['webaddress']}">${_(c['attributes']['webaddress'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.client', lang)}</td>
        <td>${client}</td>
    </tr>
    <tr>
        <td class="cell-left">${Translator.translate('ch.bfe.energieberatungsstellen.themen', lang)}</td>
        <td>${topic}</td>
    </tr>
</%def>

