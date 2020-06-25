<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it') else 'de'
    primaervegetation = 'primaervegetation_%s' % lang
%>

    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.obj_nummer')}</td>                <td>${c['attributes']['obj_nummer']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.name')}</td>                      <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.kartierjahr')}</td>               <td>${c['attributes']['kartierjahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.primaervegetation')}</td>         <td>${c['attributes'][primaervegetation] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.code_primaervegetation')}</td>    <td>${c['attributes']['code_primaervegetation'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.ref_obj_blatt')}</td>             <td><a href="${c['attributes']['ref_obj_blatt']}" target="_blank">${_('link')}</a></td></tr>
    <tr><td class="cell-left">${_('ch.bafu.auen-vegetationskarten.area_ha')}</td>                   <td>${c['attributes']['area_ha'] or '-'}</td></tr>

</%def>

