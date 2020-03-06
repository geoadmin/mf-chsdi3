<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td width="150">${h.translate('tt_gsk_meta_name', lang)}</td>    <td>${c['attributes']['titel'] or '-'}</td></tr>
    <tr><td width="150">${h.translate('tt_gsk_meta_nummer', lang)}</td>    <td>${c['attributes']['nr'] or '-'}</td></tr>
    <tr><td width="150">${h.translate('tt_gsk_meta_author', lang)}</td>    <td>${c['attributes']['authoren'] or '-'}</td></tr>
    <tr><td width="150">${h.translate('tt_gsk_meta_publikation', lang)}</td>    <td>${c['attributes']['jahrgang'] or '-'}</td></tr>
    <tr><td width="150">${h.translate('tt_gsk_meta_massstab', lang)}</td>    <td>${c['attributes']['massstab'] or '-'}</td></tr>
    <tr><td width="150">${h.translate('tt_gsk_meta_formate', lang)}</td>
        % if lang == 'fr' or lang =='it':
            <td>${c['attributes']['format_fr'] or '-'}</td>
        % else :
            <td>${c['attributes']['format_de'] or '-'}</td>
        % endif
    </tr>
</%def>

