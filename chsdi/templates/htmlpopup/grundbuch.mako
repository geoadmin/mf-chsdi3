<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
     <tr><td class="cell-left">${t.translate('grundfuehrung', lang)}</td>
     % if lang == 'de' or lang == 'rm' or lang == 'en':
          <td>${c['attributes']['grundbuchfuehrung_d'] or '-'}</td>
     % elif lang == 'fr':
          <td>${c['attributes']['grundbuchfuehrung_f'] or '-'}</td>
     % elif lang == 'it':
          <td>${c['attributes']['grundbuchfuehrung_i'] or '-'}</td>
     % endif
    </tr>
    <tr><td class="cell-left">${t.translate('grundgemeinde', lang)}</td>    <td>${c['attributes']['ortsteil_grundbuch'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('grundkreis', lang)}</td>    <td>${c['attributes']['grundbuchkreis'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('grundadresse', lang)}</td>
    % if c['attributes']['adresse'].strip() == "#":
       <td>-</td>
    % else:
      <td>
      % for address in c['attributes']['adresse'].split('#'):
      ${address or '-'} <br>
      % endfor
      </td>
    % endif
    </tr>
    <tr><td class="cell-left">${t.translate('grundtel', lang)}</td>    <td>${c['attributes']['telefon'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('grundurl', lang)}</td>
      % if c['attributes']['email'] == None:
        <td>-</td>
      % else:
        <td><a href="mailto:${c['attributes']['email']}">${_(c['attributes']['email']) or '-'}</a></td>
        </tr>
      % endif
</%def>
