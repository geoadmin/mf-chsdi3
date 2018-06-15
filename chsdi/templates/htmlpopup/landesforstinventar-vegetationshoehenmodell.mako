<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.bafu.landesforstinventar-vegetationshoehenmodell.year')}</td>           <td>${c['attributes']['year'] or '-'}</td></tr>
</%def>
