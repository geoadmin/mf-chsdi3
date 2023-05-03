<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <%
      lang = lang if lang in ('fr','it', 'en') else 'de'
      kantonname = 'kantonname_%s' %lang
    %>
    <tr>
      <td class="cell-left">${_('ch.bafu.landesforstinventar-kantone.id')}</td>
      <td>${c['attributes']['kantonid'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.landesforstinventar-kantone.name')}</td>
      <td>${c['attributes'][kantonname] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.landesforstinventar-kantone.abb')}</td>
      <td>${c['attributes']['alternatename'] or '-'}</td>
    </tr>
</%def>

