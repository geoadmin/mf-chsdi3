<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it') else 'de'
        name_text = 'plname_%s' %lang
        meastype_text = 'meastype_text_%s' %lang
        coordlevel_text = 'coordlevel_text_%s' %lang
        plstatus_text = 'plstatus_text_%s' %lang
        description_text = 'description_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.pl_name')}</td>
        <td>${c['attributes'][name_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.pl_meastype')}</td>
        <td>${c['attributes'][meastype_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.pl_coordlevel')}</td>
        <td>${c['attributes'][coordlevel_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.pl_status')}</td>
        <td>${c['attributes'][plstatus_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.pl_validfrom')}</td>
        <td>${c['attributes']['validfrom'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.pl_validuntil')}</td>
        <td>${c['attributes']['validuntil'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.description')}</td>
        <td>${c['attributes'][description_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.web')}</td>
        <td>${c['attributes']['doc_web'] or '-'}</td>
    </tr>
</%def>
