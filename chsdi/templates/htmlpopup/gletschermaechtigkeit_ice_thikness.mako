<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.swisstopo.geologie-gletschermaechtigkeit.'
%>
<tr><td class="cell-left">${_(layer + 'pk_sgi')}</td> <td>${c['attributes']['pk_sgi'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'mean_thik')}</td> <td>${c['attributes']['mean_thik'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'max_thik')}</td> <td>${c['attributes']['max_thik'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'volume')}</td> <td>${c['attributes']['volume'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'year_mode')}</td> <td>${c['attributes']['year_mode'] or '-'}</td></tr>
</%def>

