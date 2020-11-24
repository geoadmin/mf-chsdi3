<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.swisstopo.geologie-gletschermaechtigkeit.'
%>
<tr><td class="cell-left">${_(layer + 'gpr_prf_name')}</td> <td>${c['attributes']['gpr_prf_name'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'gpr_max_thik')}</td> <td>${c['attributes']['gpr_max_thik'] or '-'}</td></tr>
</%def>

