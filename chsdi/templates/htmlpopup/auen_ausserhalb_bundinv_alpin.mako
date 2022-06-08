<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr', 'it') else 'de'
  biobedeutung = '%s_biobedeutung' % lang
  geobedeutung = '%s_geobedeutung' % lang
  qualitaet = '%s_qualitaet' % lang
%>
    <tr>
        <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.name')}</td> 
        <td>${c['attributes']['name'] or '-'}<td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.objnummer')}</td>
        <td>${c['attributes']['objnummer'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.auentyp')}</td>
        <td>${c['attributes']['auentyp'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.biobedeutung')}</td>
        <td>${c['attributes'][biobedeutung] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.geobedeutung')}</td>
        <td>${c['attributes'][geobedeutung] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.qualitaet')}</td>
        <td>${c['attributes'][qualitaet] or '-'}</td>
    </tr>
    <tr>
        % if c['attributes']['shape_area']:
            <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.shape_area')}</td>
            <td>${round(c['attributes']['shape_area'], 1)}</td>
        % else:
            <td class="cell-left">${_('ch.bafu.auen-ausserhalb_bundesinventar_alpin.shape_area')}</td>
            <td>-</td>
        % endif
    </tr>
</%def>

