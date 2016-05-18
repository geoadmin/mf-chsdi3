<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<%
     if c['attributes']['pdf_list']:
        pdf_link = c['attributes']['pdf_list'].split('##')
     else :
        pdf_link = ''

%>
<tr>
  <td class="cell-left">${_('tt_document')}</td>
  <td class="cell-meta-big">
% if pdf_link != '':
% for link in pdf_link:
        <a href="http://data.geo.admin.ch/ch.bafu.hydrogeologische-karte_100/legends/${link}"  target="_blank">${link}</a><br />
% endfor
% else:
-
% endif
  </td>
</tr>
</%def>

