<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it') else 'de'
        lebr_text = 'lebr_%s' %lang
        sublebr_text = 'sublebr_%s' %lang
        schutz_text = 'schutz_%s' %lang
        typ_text = 'typ_%s' %lang
        link_nla_col = 'link_nla_%s' %lang
        link_flyer_col = 'link_flyer_%s' %lang

        link_nla_text = c['attributes'][link_nla_col] or '-'
        link_flyer_text = c['attributes'][link_flyer_col] or '-'
    %>
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.standort')}</td>
        <td>${c['attributes']['standort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.nla_name')}</td>
        <td>${c['attributes']['nla_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.lebr')}</td>
        <td>${c['attributes'][lebr_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.sublebr')}</td>
        <td>${c['attributes'][sublebr_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.schutz')}</td>
        <td>${c['attributes'][schutz_text] or '-'}</td>
    </tr>
    %if c['attributes']['geom_type'] == 'ST_MultiPoint':
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.typ')}</td>
        <td>${c['attributes'][typ_text] or '-'}</td>
    </tr>
    %endif
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.link_nla')}</td>
        <td><a href="${link_nla_text}" target="_blank">${_('link')}</a></td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.armasuisse.natur-landschaft_armee.link_flyer')}</td>
        <td><a href="${link_flyer_text}" target="_blank">${_('link')}</a></td>
    </tr>

</%def>
