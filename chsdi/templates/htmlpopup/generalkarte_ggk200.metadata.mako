<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
	<tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-generalkarte-ggk200.metadata.nr', lang)}</td> <td>${c['attributes']['nr'] or '-'}</td></tr>
	<tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-generalkarte-ggk200.metadata.titel', lang)}</td> <td>${c['attributes']['titel'] or '-'}</td></tr>
	<tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-generalkarte-ggk200.metadata.autor', lang)}</td> <td>${c['attributes']['autor'].replace('&dagger;',u"\u2020")}</td></tr>
	<tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-generalkarte-ggk200.metadata.jahr', lang)}</td> <td>${c['attributes']['jahr'] or '-'}</td></tr>
</%def>
