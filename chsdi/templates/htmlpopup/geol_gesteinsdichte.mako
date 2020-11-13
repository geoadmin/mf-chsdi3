<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.saphyr_n')}</td><td class="cell-left">${c['attributes']['saphyr_n'] or '-'}</td></tr>
<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.rhob_anz')}</td><td class="cell-left">${c['attributes']['rhob_anz'] or '-'}</td></tr>
<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.rhob_m'  )}</td><td class="cell-left">${c['attributes']['rhob_m']   or '-'}</td></tr>
<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.rhob_sd' )}</td><td class="cell-left">${c['attributes']['rhob_sd']  or '-'}</td></tr>
<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.rhob_p05')}</td><td class="cell-left">${c['attributes']['rhob_p05'] or '-'}</td></tr>
<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.rhob_p25')}</td><td class="cell-left">${c['attributes']['rhob_p25'] or '-'}</td></tr>
<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.rhob_p75')}</td><td class="cell-left">${c['attributes']['rhob_p75'] or '-'}</td></tr>
<tr><td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.rhob_p95')}</td><td class="cell-left">${c['attributes']['rhob_p95'] or '-'}</td></tr>

<tr>
<td class="cell-left" style="white-space:nowrap">${_('ch.swisstopo.geologie-gesteinsdichte.saphyr_pdf')}</td>
% if c['attributes']['saphyr_pdf'] == None or c['attributes']['saphyr_pdf'] == "-":
    <td>-</td>
% else:
    <td><a href="${c['attributes']['saphyr_pdf']}" target="_blank">pdf</a></td>
% endif
</tr>

</%def>

