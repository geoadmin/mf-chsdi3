<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.landesforstinventar-vegetationshoehenmodell.year', lang)}</td>           <td>${c['attributes']['datenstand'] or '-'}</td></tr>
</%def>
