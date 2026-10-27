<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <%
      lang = lang if lang in ('fr','it', 'en') else 'de'
   %>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.profilnumm')}</td>
      <td>${c['attributes']['profilnumm'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.link_profi')}</td>
      % if c['attributes']['link_profi'] and c['attributes']['link_profi'].startswith('http'):
         <td><a href="${c['attributes']['link_profi']}" target="_blank">${_('link')}</a></td>
      % else:
         <td>-</td>
      % endif
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.document')}</td>
      % if c['attributes']['document_' + lang] and c['attributes']['document_' + lang].startswith('http'):
         <td><a href="${c['attributes']['document_' + lang]}" target="_blank">${_('link')}</a></td>
      % else:
         <td>-</td>
      % endif
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.viewer')}</td>
      % if c['attributes']['viewer'] and c['attributes']['viewer'].startswith('http'):
         <td><a href="${c['attributes']['viewer']}" target="_blank">${_('link')}</a></td>
      % else:
         <td>-</td>
      % endif
   </tr>
</%def>
