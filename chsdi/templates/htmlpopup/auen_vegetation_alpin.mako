<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    lang = lang if lang in ('fr','it') else 'de'
    veg = 'vegetation_%s' %lang
    conf = 'conflict_%s' %lang
    %>

    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_vegetation_alpin.objnummer')}</td>       <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_vegetation_alpin.objname')}</td>           <td>${c['attributes']['objname']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_vegetation_alpin.vegetation')}</td>            <td>${c['attributes'][veg] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_vegetation_alpin.conflict')}</td>            <td>${c['attributes'][conf] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-auen_vegetation_alpin.refobjblatt')}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

