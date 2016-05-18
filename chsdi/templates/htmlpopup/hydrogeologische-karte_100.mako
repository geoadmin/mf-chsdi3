<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('tt_document')}</td><td>&nbsp;</td></tr>
<%
     pdf_link_list = c['attributes']['pdf_list']
     if pdf_link_list:
        pdf_link = c['attributes']['pdf_list'].split('##')
        nb=len(pdf_link)
        pdf_link_new = []
        i = 0
        while i < nb:
          if pdf_link[i] not in pdf_link_new:
            pdf_link_new.append(pdf_link[i])
          endif
          i = i+1

        arr_len = len(pdf_link_new)  
     else:
        arr_len = 0
%>
<tr>
  <td class="cell-meta-small">&nbsp;</td>
  <td class="cell-meta-big">
% if pdf_link_list != None:
% for i in range(arr_len):
        <a href="http://data.geo.admin.ch/ch.bafu.hydrogeologische-karte_100/legends/${pdf_link_new[i]}"  target="_blank">${pdf_link_new[i]}</a><br />
% endfor
% else:
-
% endif
  </td>
</tr>
</%def>

