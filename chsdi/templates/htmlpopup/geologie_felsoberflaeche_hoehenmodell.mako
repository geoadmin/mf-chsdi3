<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
height = round(c['attributes']['height'],2)
if height < 0.0:
  height = '-'
%>
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-felsoberflaeche_hoehenmodell.height')}</td>           <td>${height}</td></tr>
</%def>

