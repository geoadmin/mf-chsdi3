<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    link_text = "link_%s" % lang
%>

    <tr><td class="cell-left">${_('kanton')}</td>       <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('kantoncode')}</td>   <td>${c['attributes']['kantoncode'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('rwknr')}</td>        <td>${c['attributes']['rwknr']}</td></tr>
    <tr><td class="cell-left">${_('ent_gew')}</td>      <td>${c['attributes']['ent_gew'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('pdf')}</td>          <td>
    % if c['attributes']['link']:
      <a href="${c['attributes'][link_text]}" target="_blank">${_('link')}</a>
    % else:
        -
    % endif
    </td></tr>
</%def>

