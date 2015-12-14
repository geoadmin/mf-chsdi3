<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
<%
    lang = lang if lang != 'rm' else 'de'
%>

    <tr><td class="cell-left">${_('df_uid')}</td>                     <td>${c['featureId'] or '-'}</td></tr>
% for a_param in c['attributes']['a_param']:
    <tr><td class="cell-left">${_('a_param')}</td>            <td>${a_param}</td></tr>
% endfor
</%def>


<%def name="extended_info(c, lang)">
<body>

  <script type="text/javascript" src="//d3js.org/d3.v3.min.js" charset="utf-8">
    function init() {
        var svgWidth = $('#barChart').width() - 40;
        var svgHeight = $('#barChart').height() - 40;
        var histoWidth = svgWidth - 20;
        var histoHeight = svgHeight - 10;

    }
    window.onload=init();
  </script>
<tr><td class="cell-left">${_('df_uid')}</td>                     <td>${c['featureId'] or '-'}</td></tr>

  <div class="chsdi-map-container table-with-border">
    <div id="barChart"></div>
  </div>


</body>
</%def>
