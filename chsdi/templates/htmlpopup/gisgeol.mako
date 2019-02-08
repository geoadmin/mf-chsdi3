<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    c['stable_id'] = False
%>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.with_pdf')}</td><td>${c['attributes']['count_pdf']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.without_pdf')}</td><td>${c['attributes']['count_without_pdf']}</td></tr>
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
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.with_pdf')}</th><td>${c['attributes']['count_pdf']}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2.without_pdf')}</th><td>${c['attributes']['count_without_pdf']}</td></tr>
   % for i in range(int(nodocuments)):
    <tr><th class="cell-left" colspan=2 style="marging-top: 50px; padding-top: 10px">${_('dokument')} ${i+1}</th></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2.sgd_nr')}</th><td>${sgd_nr[i] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-gisgeol-punkte.orig_id')}</th><td>${orig_id[i] or '-'}</td></tr>
    <tr><th class="cell-left">${_('title')}</th><td>${title[i] or '-'}</td></tr>
    <tr><th class="cell-left">${_('author')}</th><td>${author[i] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-gisgeol-punkte.report_structure')}</th><td>${report_structure[i] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.geologie-gisgeol-punkte.aux_info')}</th><td>${aux_info[i] or '-'}</td></tr>
    <tr><th class="cell-left">${_('doccreation_date')}</th><td>${doccreation[i] or '-'}</td></tr>
    <tr>
    % if pdf_url[i]!= '-':
    <tr>
          <th class="cell-left">${_('pdf_url')}</th>
          <td>
            <a href="${pdf_url[i]}" target="_blank" title="Download ${sgd_nr[i]}.pdf - ${pdf_size[i]}" target="_blank">
              ${sgd_nr[i]}.pdf - ${pdf_size[i]}
            </a>
            <br>
          </td>
    </tr>
    <tr><th class="cell-left">${_('gisgeol_auskunft')}</th>
          <td>
            <a href="mailto:geolinfo@swisstopo.ch?subject=Query InfoGeol no.: ${sgd_nr[i]}" target="_blank">
              geolinfo@swisstopo.ch - InfoGeol no.: ${sgd_nr[i]}
            </a>
          </td>
    </tr>
    % else:
          <th class="cell-left">${_('pdf_url')}</th>
          <td> -
          </td>
    </tr>

        % if (copy_avail[i]) == 'free' and (view_avail[i]) == 'free':
                <tr><th class="cell-left">${_('gisgeol_auskunft')}</th>
          <td>
            <a href="mailto:geolinfo@swisstopo.ch?subject=Query InfoGeol no.: ${sgd_nr[i]}" target="_blank">
              geolinfo@swisstopo.ch - InfoGeol no.: ${sgd_nr[i]}
            </a>
          </td>
    </tr>
        % else:
    <tr><th class="cell-left">${_('gisgeol_auskunft')}</th>
          <td class="cell-left">
            ${_('gisgeol_auskunft_info')}
          </td>
    </tr>
        % endif
    % endif
   %endfor
</table>
</%def>

