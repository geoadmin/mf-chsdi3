# -*- coding: utf-8 -*-                                                                                                                    
<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

    <tr><td class="cell-left">${_('ch.swisstopo.images-swissimage.metadata-kartenblatt_nummer')}</td>   <td>${c['id'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.images-swissimage.metadata-kartenblatt')}</td>    <td>${c['attributes']['datenstand'] or '-'}</td></tr>
</%def>
