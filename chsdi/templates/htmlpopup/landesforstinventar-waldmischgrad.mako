<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.bafu.landesforstinventar-waldmischungsgrad.year')}</td>           <td>${c['attributes']['datenstand'] or '-'}</td></tr>
</%def>

