# -*- coding: utf-8 -*-                                                                                                                    
<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

    <tr><td class="cell-left">${h.translate('tt_fsme_gemname', lang)}</td>    <td>${c['attributes']['gemname'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_fsme_gemnr', lang)}</td>      <td>${c['attributes']['bfsnr'] or '-'}</td></tr>
</%def>
