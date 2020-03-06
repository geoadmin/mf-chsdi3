<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${h.translate('kanton', lang)}</td>          <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('kantoncode', lang)}</td>         <td>${c['attributes']['kantoncode'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('rwknr', lang)}</td>          <td>${c['attributes']['rwknr'] or '-'}</td></tr>
</%def>

