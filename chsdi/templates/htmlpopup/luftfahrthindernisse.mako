<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.registrationnumber')}</td>              <td>${c['attributes']['registrationnumber']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.airport')}</td>              <td>${c['attributes']['airport']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.obstacletype')}</td>              <td>${c['attributes']['obstacletype']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.maxheightagl')}</td>              <td>${c['attributes']['maxheightagl']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.topelevationamsl')}</td>              <td>${c['attributes']['topelevationamsl']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.radius')}</td>              <td>${c['attributes']['radius']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.effectivedate')}</td>              <td>${c['attributes']['effectivedate']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.marking')}</td>              <td>${c['attributes']['marking']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.lighting')}</td>              <td>${c['attributes']['lighting']}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.luftfahrthindernis.group')}</td>              <td>${c['attributes']['group']}</td></tr>
</%def>
