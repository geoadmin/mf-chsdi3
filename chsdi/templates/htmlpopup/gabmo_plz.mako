<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${Translator.translate('ch.swisstopo-vd.ortschaftenverzeichnis_plz.plz', lang)}</td>    <td>${c['attributes']['plz'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('zusziff', lang)}</td>
        % if len(str(c['attributes']['zusziff'])) == 1:
        <td>${'0' + str(c['attributes']['zusziff'])}</td>
        % else:
        <td>${c['attributes']['zusziff'] or '00'}</td>
        % endif
        </tr>
    <tr><td class="cell-left">${Translator.translate('langtext', lang)}</td>    <td>${c['attributes']['langtext']}</td></tr>
</%def>
