<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    c['stable_id'] = True
    lang = lang if lang in ('fr','it','en') else 'de'
    ei_hdyn = 'ei_hdyn_%s' % lang
    ei_type = 'ei_type_%s' % lang
%>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-unterirdische_fliesswege.ei_type', lang)}</td>       <td>${c['attributes'][ei_type] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.karst-unterirdische_fliesswege.ei_hdyn', lang)}</td>      <td>${c['attributes'][ei_hdyn] or '-'}</td></tr>
</%def>

