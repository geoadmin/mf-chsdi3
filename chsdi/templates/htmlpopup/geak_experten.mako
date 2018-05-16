<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>

<%
  lang = lang if lang in ('fr', 'it') else 'de'
  experience = 'experience_text_%s' % lang
%>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.name_expert')}</td>
        <td>${c['attributes']['name_expert'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.company')}</td>
        <td>${c['attributes']['company'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.experience')}</td>
        <td>${c['attributes'][experience] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.address')}</td>
        <td>${c['attributes']['address1'] or '-'}, ${c['attributes']['address2'] or '-'}, ${c['attributes']['postofficebox'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.pc_place')}</td>
        <td>${c['attributes']['pc_place'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.telephonenumber')}</td>
        <td>${c['attributes']['telephonenumber'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.mail')}</td>
          % if c['attributes']['mail'] == None:
            <td>-</td>
          % else:
            <td><a href="mailto:${c['attributes']['mail']}">${_(c['attributes']['mail'])}</a></td>
          % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.geak-experten.webaddress')}</td>
          % if c['attributes']['webaddress'] == None:
            <td>-</td>
          % else:
            <td><a target="_blank" href="${c['attributes']['webaddress']}">${_(c['attributes']['webaddress'])}</a></td>
          % endif
    </tr>
</%def>

