<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
	  <tr><td class="cell-left">${_('tilenumber')}</td><td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${_('sheetname')}</td><td>${c['attributes']['lk_name']}</td></tr>
    <tr><td class="cell-left">${_('Datenstand')}</td><td>${c['attributes']['release'] or '-'}</td></tr>
</%def>

