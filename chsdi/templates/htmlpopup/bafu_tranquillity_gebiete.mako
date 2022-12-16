<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% 
        lang = 'fr' if lang in ('fr', 'it') else 'de'
        bln_gebiet = 'bln_gebiet_%s' % lang
        moorlandschaft = 'moorlandschaft_%s' % lang
        naturpark = 'naturpark_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.bgdi_id')}</td>
        <td>${c['attributes']['fid'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.gemeinde')}</td>
        <td>${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.kanton')}</td>
        <td>${c['attributes']['kanton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.naturpark')}</td>
        <td>${c['attributes'][naturpark] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.oev_erreichbarkeit')}</td>
        <td>${c['attributes']['oev_erreichbarkeit'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.bln_gebiet')}</td>
        <td>${c['attributes'][bln_gebiet] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.moorlandschaft')}</td>
        <td>${c['attributes'][moorlandschaft] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.tranquillity-gebiete.flaeche')}</td>
        <td>${c['attributes']['flaeche'] or '-'}</td>
    </tr>
</%def>
