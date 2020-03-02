<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr', 'it') else 'de'
    project_title = 'project_title_%s' % lang
    description = 'description_%s' % lang
    topic = 'topic_%s' % lang
    sponsor_type = 'sponsor_type_%s' % lang
    status = 'status_%s' % lang
%>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.komo-projekte.project_title', lang)}</td>
        <td>${c['attributes'][project_title] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.komo-projekte.description', lang)}</td>
        <td>${c['attributes'][description] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.komo-projekte.topic', lang)}</td>
        <td>${c['attributes'][topic] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.komo-projekte.project_sponsor', lang)}</td>
        <td>${c['attributes']['project_sponsor'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.komo-projekte.sponsor_type', lang)}</td>
        <td>${c['attributes'][sponsor_type] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.komo-projekte.amount_sponsored', lang)}</td>
% if c['attributes']['amount_sponsored']:
     <td>${int(c['attributes']['amount_sponsored'])} CHF </td>
% else:
     <td>-</td>
% endif
    </tr>
    <tr>
        <td class="cell-left">${t.Translator.translate('ch.bfe.komo-projekte.status', lang)}</td>
        <td>${c['attributes'][status] or '-'}</td>
    </tr>
</%def>

