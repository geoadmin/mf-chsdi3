<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
%>

    <tr><td class="cell-left">${Translator.translate('ch.bafu.auen-vegetationskarten.auveg_obj', lang)}</td>    <td>${c['attributes']['auveg_obj']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.auen-vegetationskarten.auveg_name', lang)}</td>   <td>${c['attributes']['auveg_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.auen-vegetationskarten.auveg_jahr', lang)}</td>   <td>${c['attributes']['auveg_jahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.auen-vegetationskarten.auveg_k22', lang)}</td>    <td>${c['attributes']['auveg_k22'] or '-'}</td></tr>
</%def>

