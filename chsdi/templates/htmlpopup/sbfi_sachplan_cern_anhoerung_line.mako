<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it') else 'de'
        name_text = 'objname_%s' %lang
        fackind_text = 'fackind_text_%s' %lang
        facstatus_text = 'facstatus_text_%s' %lang
        description_text = 'description_%s' %lang
        title_text = 'title_%s' %lang
        doc_web_text = 'doc_web_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.fac_name')}</td>
        <td>${c['attributes'][name_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.fac_kind')}</td>
        <td>${c['attributes'][fackind_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.fac_status')}</td>
        <td>${c['attributes'][facstatus_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.fac_validfrom')}</td>
        <td>${c['attributes']['validfrom'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.description')}</td>
        <td>${c['attributes'][description_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.sbfi.sachplan-cern_anhoerung.web')}</td>
        % if c['attributes'][doc_web_text].startswith('http'):
            <td><a href="${c['attributes'][doc_web_text]}" target="_blank">${c['attributes'][title_text]}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>

