<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<%
dataHost = request.registry.settings['datageoadminhost']
dataPath = 'ch.bafu.hydrogeologische-karte_100/legends'
pdf_links = []
if c['attributes']['pdf_list']:
  pdf_links = [l for l in c['attributes']['pdf_list'].split('##')]
%>
<tr>
  <td class="cell-left">${_('tt_document')}</td>
  <td class="cell-meta-big">
% if pdf_links != '':
% for link in pdf_links:
        <a href="https://${dataHost}/${dataPath}/${link}"  target="_blank">${link}</a><br />
% endfor
% endif
% if not pdf_links:
 -
% endif
  </td>
</tr>
</%def>

