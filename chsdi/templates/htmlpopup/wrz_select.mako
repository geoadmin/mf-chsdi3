<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    schutzs = 'schutzs_%s' % lang
    bestimmung = 'best_%s' % lang
%>
    <tr><td class="cell-left">${h.translate('ch.bafu.wrz-jagdbanngebiete_select.jb_name', lang)}</td>               <td>${c['attributes']['jb_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_wrz_select_schutz', lang)}</td>             <td>${c['attributes'][schutzs] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_wrz_select_best', lang)}</td>               <td>${c['attributes'][bestimmung] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_wrz_select_zusatz', lang)}</td>             <td>${c['attributes']['zusatzinformation'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_wrz_select_schutzzeit', lang)}</td>         <td>${c['attributes']['schutzzeit'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('tt_wrz_select_grundlage', lang)}</td>          <td>${c['attributes']['grundlage'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wrz-jagdbanngebiete_select.beschlussjahr', lang)}</td>          <td>${c['attributes']['beschlussjahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.wrz-jagdbanngebiete_select.kanton', lang)}</td>             <td>${c['attributes']['kanton'] or '-'}</td></tr>
    % if c['attributes']['url_kanton'] and c['attributes'] :
    <tr><td class="cell-left">${h.translate('ch.bafu.wrz-jagdbanngebiete_select.ref_kanton', lang)}</td><td><a href="${c['attributes']['url_kanton']}" target="_blank">Link</a></td></tr>
    % else:
    <tr><td class="cell-left">${h.translate('ch.bafu.wrz-jagdbanngebiete_select.ref_kanton', lang)}</td><td>-</td></tr>
    % endif
</%def>

