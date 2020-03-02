<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   % if "fineltra_LV" in c['attributes']['type']:
    % if lang == 'de' or lang == 'rm' or lang == 'en':
      <tr><td class="cell-left">${t.translate('type_dreieck', lang)}</td><td>FINELTRA LV</td></tr>
    % else:
      <tr><td class="cell-left">${t.translate('type_dreieck', lang)}</td><td>FINELTRA MN</td></tr>
    % endif
   % else:
      <tr><td class="cell-left">${t.translate('type_dreieck', lang)}</td><td>${c['attributes']['type'] or '-'}</td></tr>
   % endif
   <tr><td class="cell-left">${t.translate('num_dreieck', lang)}</td><td>${c['attributes']['num'] or '-'}</td></tr>
   <tr><td class="cell-left">${t.translate('nom_dreieck', lang)}</td><td>${c['attributes']['nom'] or '-'}</td></tr>
</%def>
