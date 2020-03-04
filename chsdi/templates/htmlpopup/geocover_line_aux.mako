<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = 'de' if lang in ('de', 'rm', 'en') else 'fr'
    basisdatensatz = 'basisdatensatz_%s' % lang
    description = 'description_%s' % lang
    spec_description = 'spec_description_%s' % lang
%>
	<tr><td class="cell-left">${mod_translate.Translator.translate('geocover_basisdatensatz', lang)}</td><td>${c['attributes'][basisdatensatz] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('geocover_description', lang)}</td><td>${c['attributes'][description] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('geocover_spec_description', lang)}</td><td>${c['attributes'][spec_description] or '-'}</td></tr>
</%def>
