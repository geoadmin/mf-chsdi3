<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
%>

    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.auveg_obj')}</td>    <td>${c['attributes']['auveg_obj']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.auveg_name')}</td>   <td>${c['attributes']['auveg_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.auveg_jahr')}</td>   <td>${c['attributes']['auveg_jahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.auveg_k22')}</td>    <td>${c['attributes']['auveg_k22'] or '-'}</td></tr>
</%def>

