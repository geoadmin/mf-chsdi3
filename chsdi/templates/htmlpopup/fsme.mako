# -*- coding: utf-8 -*-                                                                                                                    
<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

    <tr><td class="cell-left">${_('tt_fsme_gemname')}</td>    <td>${c['attributes']['gemname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_fsme_gemnr')}</td>      <td>${c['attributes']['bfsnr'] or '-'}</td></tr>
</%def>
