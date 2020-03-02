<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr><td class="cell-left">${Translator.translate('tt_shb_objekt', lang)}</td>     <td>${c['attributes']['objekt'] or '-'}</td></tr>
  <tr><td class="cell-left">${Translator.translate('tt_shb_objtyp', lang)}</td>     <td>${c['attributes']['obtyp'] or '-'}</td></tr>
  <tr><td class="cell-left">${Translator.translate('tt_shb_ort', lang)}</td>        <td>${c['attributes']['ort'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    objteil = c['attributes']['objektteil'].split('##')
    alter =  c['attributes']['age'].split('##')
    gesteinart =  c['attributes']['gestart'].split('##')
    referenz =  c['attributes']['referenz'].split('##')
    link =  c['attributes']['hyperlink'].split('##')
    bemerkung =  c['attributes']['bemerkung'].split('##')
    abbauort =  c['attributes']['abbauort'].split('##')

    arr_len = len(objteil)
%>

    <table class="table-with-border">
    <tr><td width="100%" valign="top" colspan="2"><h1 class="tooltip_large_titel">${Translator.translate('tt_shb_objekt', lang)}</h1></tr>
    <tr><td width="150">${Translator.translate('tt_shb_objekt', lang)}</td>    <td>${c['attributes']['objekt']}</td></tr>
    <tr><td width="150">${Translator.translate('tt_shb_objtyp', lang)}</td>    <td>${c['attributes']['obtyp'] or '-'}</td></tr>
    <tr><td width="150">${Translator.translate('tt_shb_ort', lang)}</td>       <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><td width="100%" valign="top" colspan="2">&nbsp;</td></tr>

% for i in range(arr_len):
    <tr><td valign="top"><h1 stile="bold">${Translator.translate('tt_shb_objteil', lang)}</h1></td><td><h2 stile="bold">${objteil[i] or '-'}</h2></td></tr>
    <tr><td width="150">${Translator.translate('tt_shb_alter', lang)}</td>     <td>${alter[i] or '-'}</td></tr>
    <tr><td width="150">${Translator.translate('tt_shb_gart', lang)}</td>      <td>${gesteinart[i] or '-'}</td></tr>
    <tr><td width="150">${Translator.translate('tt_shb_ref', lang)}</td>       <td>${referenz[i] or '-'}</td></tr>
    <tr><td width="150">${Translator.translate('tt_shb_abbauort', lang)}</td>  <td>${abbauort[i] or '-'}</td></tr>
    <tr><td width="150">${Translator.translate('tt_shb_bemerkung', lang)}</td> <td>${bemerkung[i] or '-'}</td></tr>
    % if link[i] == '-':
        <tr><td width="150">${Translator.translate('tt_shb_link', lang)}</td>      <td>-</td></tr>
    % else:
        <tr><td width="150">${Translator.translate('tt_shb_link', lang)}</td>      <td><a href=${link[i]} target="_blank">PDF</a></td></tr>
    % endif:
    <tr><td width="100%" valign="top" colspan="2">&nbsp;</td></tr>
% endfor
  </table>
</%def>
