# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.babs.kulturgueter.zkob')}</td>   <td>${c['attributes']['zkob']}</td></tr>
    <tr>
        <td class="cell-left">${_('x')}</td>
        % if c['attributes']['x']:
            <td>${int(round(c['attributes']['x']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('y')}</td>
        % if c['attributes']['y']:
            <td>${int(round(c['attributes']['y']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr><td class="cell-left">${_('gemeinde')}</td>       <td>${c['attributes']['gemeinde'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('kanton')}</td>         <td>${c['attributes']['kt_kz'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
    <%
        c['stable_id'] = True
        objarts = c['attributes']['objektart'].split(',')
        gemeinde_ehemalig = c['attributes']['gemeinde_ehemalig'] if str(c['attributes']['gemeinde_ehemalig']).startswith("(") else "("+c['attributes']['gemeinde_ehemalig']+")"
        import csv
        dataGeoAdminHost = request.registry.settings['datageoadminhost']
        csv_url = dataGeoAdminHost + "/" + c['layerBodId']  + "/image/meta.txt"
        csv_file = None
        # TODO python2 clean-up
        try:
            from urllib2 import urlopen
            csv_file = urlopen(csv_url)
            reader = csv.reader(csv_file, delimiter =';')  # creates the reader object
            next(reader) # Skip header
            pic_list = [map(lambda x: x.decode("utf-8"), row) for row in reader if int(row[0]) == c['featureId']]
            csv_file.close()
        except ImportError:
            # Python3 fallback
            from urllib.request import urlopen
            csv_file = urlopen(csv_url).read().decode('utf-8')
            reader = csv.reader(csv_file.splitlines(), delimiter =';')  # creates the reader object
            next(reader) # Skip header
            pic_list = [ row for row in reader if int(row[0]) == c['featureId'] ]
    %>
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


    <table class="table-with-border kernkraftwerke-extended">
        <tr>
            <th class="cell-left">${_('name')}</th>
            <td>${c['attributes']['zkob'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('kategorie')}</th>
            <td>${c['attributes']['kategorie'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('tt_kbs_objektart')}</th>
            <td>
                % for i, objart in enumerate(objarts):
                    ${_('kultur' + objart) + ' / ' if (i+1<len(objarts)) else _('kultur' + objart)}
                % endfor
            </td>
        </tr>
        <tr>
            <th class="cell-left">${_('tt_kbs_nbr')}</th>
            <td>${c['featureId'] or '-'}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('grundadresse')}</th>
            <td>${c['attributes']['adresse'] or ''} ${c['attributes']['hausnr'] or ''}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('tt_kbs_gemeinde')} (${_('tt_kbs_gemeinde_ehemalige')})</th>
            <td>${c['attributes']['gemeinde'] or ''} ${gemeinde_ehemalig if c['attributes']['gemeinde_ehemalig'] not in [Null, ""] else ''}</td>
        </tr>
        <tr>
            <th class="cell-left">${_('Coordinates')}</th>
            % if c['attributes']['x']:
                <td>${int(round(c['attributes']['x']))} / ${int(round(c['attributes']['y']))}</td>
            % else:
                <td>-</td>
            % endif
        </tr>
    % if c['attributes']['pdf_list'] not in [None, ""]:
        <tr>
            <th class="cell-left">${_('Feature tooltip')}:</th>
            <td>
	        % for pdf in c['attributes']['pdf_list'].split(','):
                <a href="${dataGeoAdminHost}/ch.babs.kulturgueter/PDF/${pdf}" target="_blank">${pdf}</a><br />
	        % endfor
            </td>
	    </tr>
    %endif
    % if c['attributes']['link_uri'] not in [None, ""]:
        <tr>
          <th class="cell-left">${_('legalregulationlink')}</th>
            <td><a href="${c['attributes']['link_uri']}">${c['attributes']['link_title']}</a></td>
        </tr>
    % endif
    % if c['attributes']['link_2_uri'] not in [None, ""]:
        <tr>
          <th class="cell-left">${_('legalregulationlink')}</th>
          <td><a href="${c['attributes']['link_2_uri']}">${c['attributes']['link_2_title']}</a></td>
        </tr>
    % endif
    % if c['attributes']['link_3_uri'] not in [None, ""]:
        <tr>
          <th class="cell-left">${_('legalregulationlink')}</th>
          <td><a href="${c['attributes']['link_3_uri']}">${c['attributes']['link_3_title']}</a></td>
        </tr>
    % endif
    </table>
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
            %for pic in pic_list:
                <div class="thumbnail">
                    <a href="${dataGeoAdminHost}/ch.babs.kulturgueter/image/kgs_${pic[0]}_${pic[1]}.jpg">
                        <img class="image" src="${dataGeoAdminHost}/ch.babs.kulturgueter/image/kgs_${pic[0]}_${pic[1]}.jpg" />
                    </a>
                    <div>${pic[3] or ''} - ${pic[2] or ''}</div>
                </div>
            %endfor
            </div>
        </div>
    <table class="kernkraftwerke-extended">
    % if c['attributes']['kurztexte'] not in [None, ""]:
        <tr>
          <td>${c['attributes']['kurztexte']}</td>
        </tr>
    % endif
    </table>
</%def>


<%def name="extended_resources(c, lang)">
  <link rel="stylesheet" type="text/css" href="${request.static_url('chsdi:static/css/blueimp-gallery.min.css')}"/>
  <script src="${request.static_url('chsdi:static/js/jquery.min.js')}"></script>
  <script src="${request.static_url('chsdi:static/js/blueimp-gallery.min.js')}"></script>
</%def>
