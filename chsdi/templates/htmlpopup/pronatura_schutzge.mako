<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('tt_wrz_select_obj')}</td>                         <td>${c['attributes']['nummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_kkw_name')}</td>                         <td>${c['attributes']['name'] or '-'}</td></tr>
</%def>

