<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>

    <tr><td class="cell-left">${Translator.translate('kanton', lang)}</td>       <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('kantoncode', lang)}</td>   <td>${c['attributes']['kantoncode'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('rwknr', lang)}</td>        <td>${c['attributes']['rwknr']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ent_gew', lang)}</td>      <td>${c['attributes']['ent_gew'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('pdf', lang)}</td>          <td>
    % if c['attributes']['link']:
      <a href="https://www.ubst.bafu.admin.ch/wasser/restwasser/data/data/er/${lang}/${c['attributes']['link']}" target="_blank">${Translator.translate('link', lang)}</a>
    % else:
        -
    % endif
    </td></tr>
</%def>

