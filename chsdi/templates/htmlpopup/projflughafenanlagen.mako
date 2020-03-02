<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    zonekind_text = 'zonekind_text_%s' % lang
    legalstatus_text = 'legalstatus_text_%s' % lang

%>
    <tr><td class="cell-left">${t.Translator.translate('kindofzone', lang)}</td>    <td>${c['attributes'][zonekind_text] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('applicant', lang)}</td>                  <td>${c['attributes']['applicant'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('gemkanton', lang)}</td>                  <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('betrgemeinde', lang)}</td>               <td>${c['attributes']['municipality'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('bazlrechtstatus', lang)}</td>            <td>${c['attributes'][legalstatus_text] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('modif_validfrom', lang)}</td>            <td>${c['attributes']['validfrom'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('durationofeffect', lang)}</td>           <td>${c['attributes']['durationofeffect'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('descriptionText', lang)}</td>            <td>${c['attributes']['description'] or '-'}</td></tr>
%if c['attributes']['weblink_origin']:
    <tr><td class="cell-left">${t.Translator.translate('legalregulationlink', lang)}</td>        <td><a target="_blank" href="${c['attributes']['weblink_origin']}">${_('legalregulationlink') or '-'}</a></td></tr>
% else:
    <tr><td class="cell-left">${t.Translator.translate('legalregulationlink', lang)}</td>        <td> - </td></tr>
%endif
</%def>
