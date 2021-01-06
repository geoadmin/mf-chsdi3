<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gwlnr')}</td>
  <td>${c['attributes']['gwlnr'] or '-'}</td>
</tr>
</%def>


<%def name="extended_info(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>
<table class="table-with-border kernkraftwerke-extended">
<colgroup>
  <col width=50%><col width=50%>
</colgroup>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gwlnr')}</td>
  <td>${c['attributes']['gwlnr'] or '-'}</td>
</tr>
</table>
</%def>
