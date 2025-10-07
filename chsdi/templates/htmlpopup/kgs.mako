<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <tr>
        <td class="cell-left">${_('ch.babs.kulturgueter.objekt_nr')}</td>
        <td>${c['id'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.babs.kulturgueter.beschreibung')}</td>
        <td>${c['attributes']['beschreibung'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.babs.kulturgueter.x')}</td>
        % if c['attributes']['x']:
            <td>${int(round(c['attributes']['x']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.babs.kulturgueter.y')}</td>
        % if c['attributes']['y']:
            <td>${int(round(c['attributes']['y']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.babs.kulturgueter.gemeinde')}</td>
        <td>${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.babs.kulturgueter.kanton')}</td>
        <td>${c['attributes']['kanton'] or '-'}</td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
    <%
        c['stable_id'] = True

        lang = lang if lang in ('fr','it') else 'de'

        import os

        NO_DATA_VALUES = ['', None]

        def text_separation(csv_value, sep='/'):
            return sep.join(csv_value.split(','))

        objektart_list = 'objektart_%s_list' % lang

        if c['attributes'][objektart_list] in NO_DATA_VALUES:
            objektart_text = '-'
        else:
            objektart_text = text_separation(c['attributes'][objektart_list], ' / ')

        bild_urls = c['attributes']['bild_url_list'].split(',')
        bild_nrs = c['attributes']['bild_nr_list'].split(',')
        copyright_text = c['attributes']['copyright']
        fotograf_text = c['attributes']['fotograf']

        if c['attributes']['pdf_files_list'] in NO_DATA_VALUES:
            pdf_files_text = '-'
        else:
            pdf_files = c['attributes']['pdf_files_list'].split(',')
            pdf_files_text = text_separation(
                ','.join(f'<a href="{pdf_file}" target="_blank">{os.path.basename(pdf_file)}</a>' for pdf_file in pdf_files),
                '<br />'
            )

        if c['attributes']['weblinks_list'] in NO_DATA_VALUES:
            weblinks_text = '-'
        else:
            weblinks = c['attributes']['weblinks_list'].split(',')
            bemerkungen = c['attributes']['bemerkung_list'].split(',')
            weblinks_text = text_separation(
                ','.join(f'<a href="{link}" target="_blank">{remark}</a>' for link, remark in zip(weblinks, bemerkungen)),
                '<br />'
            )
    %>
    <table class="table-with-border kernkraftwerke-extended">
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.beschreibung')}</th>
            <td>${c['attributes']['beschreibung'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.objektart')}</th>
            <td>${_(objektart_text)}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.objekt_nr')}</th>
            <td>${c['featureId'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.adresse')}</th>
            <td>${c['attributes']['adresse_list'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.ehemalige_gemeinde')}</th>
            <td>${c['attributes']['ehemaligegemeinde'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.kanton')}</th>
            <td>${c['attributes']['kanton'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.x')}</th>
            % if c['attributes']['x']:
                <td>${int(round(c['attributes']['x']))}</td>
            % else:
                <td>-</td>
            % endif
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.y')}</th>
            % if c['attributes']['y']:
                <td>${int(round(c['attributes']['y']))}</td>
            % else:
                <td>-</td>
            % endif
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.pdf_file')}</th>
            <td>${_(pdf_files_text)|n}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('ch.babs.kulturgueter.weblink')}</th>
            <td>${_(weblinks_text)|n}</td>
        </tr>
    </table>

    <script>
        $(document).ready(function(){
            $('.thumbnail-container').on('click', function (event) {
            event = event || window.event;
                event.preventDefault();
            var target = event.target || event.srcElement,
                link = target.src ? target.parentNode : target,
                options = {index: link, event: event, onslide: function(index, slide){
                    /** a "beautiful" line of code which sets the title of the gallery to the current copyright + photographer of the current photo**/
                    $('#blueimp-gallery-title').html(($($('.thumbnail-container').children('.thumbnail')[index]).children('div').html()));
                }},
                links = this.getElementsByTagName('a');
            blueimp.Gallery(links, options);
            });
        });
    </script>
    <div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls">
        <div class="slides"></div>
        <div class="title" id="blueimp-gallery-title"></div>
        <a class="prev">&lsaquo;</a>
        <a class="next">&rsaquo;</a>
        <a class="close">x</a>
        <a class="play-pause"></a>
        <ol class="indicator"></ol>
    </div>
    <div class="kgs-thumbnails">
        <div class="thumbnail-container">
            %for bild_url, bild_nr in zip(bild_urls, bild_nrs):
                %if bild_url:
                    <div class="thumbnail">
                        <a href="${bild_url}"><img class="image" src="${bild_url}" /></a>
                        <div style="padding-top:10px">${copyright_text or ''} - ${fotograf_text}</div>
                    </div>
                %endif
            %endfor
        </div>
    </div>

    % if c['attributes']['kurztext']:
        <table class="table-with-border kernkraftwerke-extended">
            <tr>
                <td>${c['attributes']['kurztext'] or '-'}</td>
            </tr>
        </table>
    % endif

</%def>

<%def name="extended_resources(c, lang)">
  <link rel="stylesheet" type="text/css" href="${request.static_url('chsdi:static/css/blueimp-gallery.min.css')}"/>
  <script src="${request.static_url('chsdi:static/js/jquery.min.js')}"></script>
  <script src="${request.static_url('chsdi:static/js/blueimp-gallery.min.js')}"></script>
</%def>
