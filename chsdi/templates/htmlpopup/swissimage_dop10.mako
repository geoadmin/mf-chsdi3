# -*- coding: utf-8 -*-                                                                                                                    
<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.images-swissimage-dop10.metadata-kartenblatt_nummer', lang)}</td>   <td>${c['id'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.images-swissimage-dop10.metadata-kartenblatt', lang)}</td>    <td>${c['attributes']['datenstand'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.images-swissimage-dop10.metadata-resolution', lang)}</td>    <td>${c['attributes']['resolution'] or '-'}</td></tr>
</%def>
