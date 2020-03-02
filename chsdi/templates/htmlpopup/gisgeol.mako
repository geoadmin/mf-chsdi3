<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    c['stable_id'] = False
%>
    <tr><td class="cell-left" width="60%">${t.translate('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.with_pdf', lang)}</td><td width="40%">${c['attributes']['count_pdf']}</td></tr>
    <tr><td class="cell-left" width="60%">${t.translate('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.without_pdf', lang)}</td><td width="40%">${c['attributes']['count_without_pdf']}</td></tr>
</%def>
<%def name="extended_info(c,lang)">
<%
    nodocuments = c['attributes']['count_total']
    sgd_nr = c['attributes']['sgd_nr'].split('##')
    orig_id = c['attributes']['orig_id'].split('##')
    title = c['attributes']['title'].split('##')
    author = c['attributes']['author'].split('##')
    report_structure = c['attributes']['report_structure'].split('##')
    aux_info = c['attributes']['aux_info'].split('##')
    doccreation = c['attributes']['doccreation'].split('##')
    pdf_url = c['attributes']['pdf_url'].split('##')
    pdf_size = c['attributes']['pdf_size'].split('##')
    copy_avail = c['attributes']['copy_avail'].split('##')
    view_avail = c['attributes']['view_avail'].split('##')

%>
<table class="table-with-border gisgeol-extended">
    <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.with_pdf', lang)}</th><td>${c['attributes']['count_pdf']}</td></tr>
    <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.without_pdf', lang)}</th><td>${c['attributes']['count_without_pdf']}</td></tr>
   % for i in range(int(nodocuments)):
    <tr><th class="cell-left" colspan=2 style="marging-top: 50px; padding-top: 10px">${t.translate('dokument', lang)} ${i+1}</th></tr>
    <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2.sgd_nr', lang)}</th><td>${sgd_nr[i] or '-'}</td></tr>
    <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-gisgeol-punkte.orig_id', lang)}</th><td>${orig_id[i] or '-'}</td></tr>
    <tr><th class="cell-left">${t.translate('title', lang)}</th><td>${title[i] or '-'}</td></tr>
    <tr><th class="cell-left">${t.translate('author', lang)}</th><td>${author[i] or '-'}</td></tr>
    <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-gisgeol-punkte.report_structure', lang)}</th><td>${report_structure[i] or '-'}</td></tr>
    <tr><th class="cell-left">${t.translate('ch.swisstopo.geologie-gisgeol-punkte.aux_info', lang)}</th><td>${aux_info[i] or '-'}</td></tr>
    <tr><th class="cell-left">${t.translate('doccreation_date', lang)}</th><td>${doccreation[i] or '-'}</td></tr>
    <tr>
    % if pdf_url[i]!= '-':
    <tr>
          <th class="cell-left">${t.translate('pdf_url', lang)}</th>
          <td>
            <a href="${pdf_url[i]}" target="_blank" title="Download ${sgd_nr[i]}.pdf - ${pdf_size[i]}" target="_blank">
              ${sgd_nr[i]}.pdf - ${pdf_size[i]}
            </a>
            <br>
          </td>
    </tr>
    <tr><th class="cell-left">${t.translate('gisgeol_auskunft', lang)}</th>
          <td>
            <a href="mailto:geolinfo@swisstopo.ch?subject=Query InfoGeol no.: ${sgd_nr[i]}" target="_blank">
              geolinfo@swisstopo.ch - InfoGeol no.: ${sgd_nr[i]}
            </a>
          </td>
    </tr>
    % else:
          <th class="cell-left">${t.translate('pdf_url', lang)}</th>
          <td> -
          </td>
    </tr>

        % if (copy_avail[i]) == 'free' and (view_avail[i]) == 'free':
                <tr><th class="cell-left">${t.translate('gisgeol_auskunft', lang)}</th>
          <td>
            <a href="mailto:geolinfo@swisstopo.ch?subject=Query InfoGeol no.: ${sgd_nr[i]}" target="_blank">
              geolinfo@swisstopo.ch - InfoGeol no.: ${sgd_nr[i]}
            </a>
          </td>
    </tr>
        % else:
    <tr><th class="cell-left">${t.translate('gisgeol_auskunft', lang)}</th>
          <td class="cell-left">
            ${t.translate('gisgeol_auskunft_info', lang)}
          </td>
    </tr>
        % endif
    % endif
   %endfor
</table>
</%def>

