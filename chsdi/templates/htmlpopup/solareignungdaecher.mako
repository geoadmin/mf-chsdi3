<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
<%
    lang = lang if lang != 'rm' else 'de'
%>

    <tr><td class="cell-left">${_('tt_klasse')}</td>                     <td>${c['attributes']['klasse'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_flaeche')}</td>                     <td>${c['attributes']['flaeche'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_ausrichtung')}</td>                     <td>${c['attributes']['ausrichtung'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_neigung')}</td>                     <td>${c['attributes']['neigung'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_finanzertrag')}</td>                     <td>${c['attributes']['finanzertrag'] or '-'}</td></tr>
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
  <table class="table-with-border">
    <tr><th class="cell-left">${_('tt_klasse')}</th>                     <td>${c['attributes']['klasse'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_flaeche')}</th>                     <td>${c['attributes']['flaeche'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_ausrichtung')}</th>                     <td>${c['attributes']['ausrichtung'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_neigung')}</th>                     <td>${c['attributes']['neigung'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_finanzertrag')}</th>                     <td>${c['attributes']['finanzertrag'] or '-'}</td></tr>
  </table>
  <div class="chsdi-map-container table-with-border">
    <div id="barChart"></div>
  </div>


</body>
</%def>
