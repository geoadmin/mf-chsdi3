<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr','it','en') else 'de'
    typ_text = 'typ_%s' % lang
    status_text = 'status_%s' % lang
%>

    <tr><td class="cell-left">${t.translate('typ', lang)}</td>                                                  <td>${c['attributes'][typ_text] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('status', lang)}</td>                                               <td>${c['attributes'][status_text] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('gemkanton', lang)}</td>                                            <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('name', lang)}</td>                                                 <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('tt_source', lang)}</td>                                            <td>${c['attributes']['source'] or '-'}</td></tr>

</%def>

