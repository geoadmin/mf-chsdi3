# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<%
translate_type = c['attributes']['type'] + '_landesschwerenetz_type'
%>

    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.nr_lsn2004', lang)}</td>        <td>${c['attributes']['nr_lsn2004']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.name', lang)}</td>              <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.label', lang)}</td>             <td>${c['attributes']['label_tt']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.type', lang)}</td>              <td>${_(translate_type)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.lat_etrs', lang)}</td>          <td>${round(c['attributes']['lat_etrs'],3)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.lon_etrs', lang)}</td>          <td>${round(c['attributes']['lon_etrs'],3)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.y_lv03', lang)}</td>            <td>${int(round(c['attributes']['y_lv03']))}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.x_lv03', lang)}</td>            <td>${int(round(c['attributes']['x_lv03']))}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.h_ln02', lang)}</td>            <td>${c['attributes']['h_ln02'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.gravity', lang)}</td>           <td>${c['attributes']['gravity']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.rms', lang)}</td>               <td>${c['attributes']['rms']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.vert_grad', lang)}</td>         <td>${c['attributes']['vert_grad'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.link_hfp_title', lang)}</td>
    % if "http" in c['attributes']['link_hfp_url']:
        <td><a href="${c['attributes']['link_hfp_url']}" target="_blank">${c['attributes']['link_hfp_title'] or 'LinkHFP'}</a></td>
    % else:
        <td>-</td>
    % endif
    </tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.landesschwerenetz.link_lfp_title', lang)}</td>
    % if "http" in c['attributes']['link_lfp_url']:
        <td><a href="${c['attributes']['link_lfp_url']}" target="_blank">${c['attributes']['link_lfp_title'] or 'LinkLFP'}</a></td>
    % else:
        <td>-</td>
    % endif
    </tr>
</%def>
