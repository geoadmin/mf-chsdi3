<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${h.translate('nffirmenname', lang)}</td>    <td>${c['attributes']['firmenname'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('nfname', lang)}</td>    <td>${c['attributes']['name'] or '-'}
      % if c['attributes']['stellvertreter']:
           (${h.translate('ch.swisstopo-vd.geometa-nfgeom.stellvertreter', lang)})
      % endif
    </td></tr>
    <tr><td class="cell-left">${h.translate('grundadresse', lang)}</td>
      % if c['attributes']['adresse'].strip() == '#':
           <td>-</td>
      % else:  
           <td>
        % for address in c['attributes']['adresse'].split('#'):
          ${address or '-'} <br>
        % endfor
      </td>
      % endif
    </tr>
    <tr><td class="cell-left">${h.translate('grundtel', lang)}</td>    <td>${c['attributes']['telefon'] or '-'}</td></tr>
     <tr><td class="cell-left">${h.translate('grundurl', lang)}</td>
      % if c['attributes']['email'] == None:
       <td>-</td>
      % elif "@" in c['attributes']['email']:
           <td><a href="mailto:${c['attributes']['email']}">${_(c['attributes']['email']) or '-'}</a></td>
      % elif "http" in c['attributes']['email']:
           <td><a target="_blank" href="${c['attributes']['email']}">${c['attributes']['email'] or '-'}</a></td>
      </tr>
      % endif
</%def>
