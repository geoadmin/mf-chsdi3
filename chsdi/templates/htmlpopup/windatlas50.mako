<%inherit file="base.mako"/>
<%!
import requests
def getAltitude(baseUrl, center):
    fullUrl = 'http:' + baseUrl +'/rest/services/height'
    response = requests.get(
        fullUrl + '?easting=%s&northing=%s&elevation_model=COMB' % (center[0], center[1]),
        headers={'Referer': fullUrl})
    result = response.json()
    return result['height']
%>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<%
from gatilegrid.grid import Grid
from chsdi.models.grid import get_grid_spec
altitude = int(c['layerBodId'].split('ch.bfe.windenergie-geschwindigkeit_h')[1])

# center coordinates and dhm altitude from feature id
gridSpec = get_grid_spec(c['layerBodId'])
col, row = [int(x) for x in c['featureId'].split("_")]
grid = Grid(gridSpec.get('extent'), gridSpec.get('resolutionX'), gridSpec.get('resolutionY'))
extent = grid.cellExtent(col,row)
center = [(extent[0] + extent[2])/2,(extent[1] + extent[3])/2]
baseUrl = request.registry.settings['api_url']
dhm_altitude = getAltitude(baseUrl, center)
center = ', '.join([str(round(center[0], 2)), str(round(center[1], 2))])

props = c['properties']
%>
<!-- html output -->
    <tr>
      <th class="cell-left">${_('tt_bfe_hoehe_ueber_grund')}</th>
      <td>${altitude or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('tt_bfe_koordinaten')}</th>
      <td>${center}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('tt_bfe_hoehe_gelaende')}</th>
      <td>${dhm_altitude or '-'}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('tt_bfe_geschw_wind_durchschnitt')}</th>
      <td>${round(props['v_mean'], 2)}</td>
    </tr>
    <tr>
      <th class="cell-left">${_('tt_bfe_windrose')}</th>
      <td >
        <iframe src="${baseUrl}/rest/services/all/MapServer/${c['layerBodId']}/${c['featureId']}/extendedHtmlPopup?lang=${lang}&iframe=true" width="100%" height="230" frameborder="0" style="border: 0" scrolling="no"></iframe>
      </td>
    </tr>
</%def>


<%def name="extended_info(c, lang)">
<%
coordinates = c['geometry']['coordinates'][0]
bottomLeft = coordinates[0]
topRight = coordinates[2]
center = [(bottomLeft[0] + topRight[0]) / 2, (bottomLeft[1] + topRight[1]) / 2]
baseUrl = request.registry.settings['api_url']
dhm_altitude = getAltitude(baseUrl, center)
center = ', '.join([str(round(center[0], 2)), str(round(center[1], 2))])
altitude = int(c['layerBodId'].split('ch.bfe.windenergie-geschwindigkeit_h')[1])

props = c['properties']

freq_total = props['freq_0']    + props['freq_30']
freq_total += props['freq_60']  + props['freq_90']
freq_total += props['freq_120'] + props['freq_150']
freq_total += props['freq_180'] + props['freq_210']
freq_total += props['freq_240'] + props['freq_270']
freq_total += props['freq_300'] + props['freq_330']

# gracefully check if url request has get parameter iframe
try:
    iframe = request.GET['iframe'] if request.GET['iframe'] else False
except:
    iframe=False
    pass

%>
<!-- html output -->
<title>${c['fullName']}</title>

<!-- custom css for windrose/weibull -->
<style>
.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}
.bar {
  fill: orange;
}
.solidArc:hover {
  fill: orangered;
}
.solidArc {
  -moz-transition: all 0.3s;
  -o-transition: all 0.3s;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.x.axis path {
  display: none;
}
.aster-score {
  line-height: 1;
  font-weight: bold;
  font-size: 500%;
}
.d3-tip {
  line-height: 1;
  font-weight: bold;
  padding: 12px;
  background: rgba(0, 0, 0, 0.8);
  color: #fff;
  border-radius: 2px;
  font-size: small;
  font-family: sans-serif;
}
/* Creates a small triangle extender for the tooltip */
.d3-tip:after {
  box-sizing: border-box;
  display: inline;
  font-size: 10px;
  width: 100%;
  line-height: 1;
  color: rgba(0, 0, 0, 0.8);
  content: "\25BC";
  position: absolute;
  text-align: center;
}
/* Style northward tooltips differently */
.d3-tip.n:after {
  margin: -1px 0 0 0;
  top: 100%;
  left: 0;
}
.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}
.x.axis path {
  display: none;
}
.line {
  fill: none;
  stroke: steelblue;
  stroke-width: 1.5px;
}
#windrichtung {
  border-collapse: collapse;
  font-size: initial;
}
#weibull {
  margin-bottom: 20px;
}
td.inner-table {
  padding: 10px !important;
}
</style>


% if iframe:
<style>
.chsdi-htmlpopup-container {
    visibility: hidden;
}
.htmlpopup-header {
    visibility: hidden;
}
.htmlpopup-content {
    visibility: hidden;
}
.htmlpopup-footer {
    visibility: hidden;
}
#rose {
    color: blue;
    visibility: visible;
    position: fixed;
    top: 0;
}
</style>
% endif

<body>
<table class="table-with-border kernkraftwerke-extended">
  <tr>
    <th class="cell-left">${_('tt_bfe_hoehe_ueber_grund')}</th>
    <td>${altitude or '-'}</td>
  </tr>
  <tr>
    <th class="cell-left">${_('tt_bfe_koordinaten')}</th>
    <td>${center or '-'}</td>
  </tr>
  <tr>
    <th class="cell-left">${_('tt_bfe_hoehe_gelaende')}</th>
    <td>${dhm_altitude or '-'}</td>
  </tr>
  <tr>
    <th class="cell-left">${_('tt_bfe_geschw_wind_durchschnitt')}</th>
    <td>${props['v_mean']}</td>
  </tr>
  <tr>
    <td class="inner-table" colspan="2"><b>${_('tt_bfe_windrose_geschwverteilung')}</b><br/>${_('tt_bfe_windrose_help')}<br/><div id="rose"></div>
      <table id="windrichtung">
        <tr>
          <th>${_('tt_bfe_windrichtung')}</th>
          <th>${_('tt_bfe_haeufigkeit')}</th>
          <th>${_('tt_bfe_mittlere_geschw')}</th>
          <th>A</th>
          <th>k</th>
        </tr>
        <tr>
          <td>total</td>
          <td>${round(freq_total, 3)} %</td>
          <td>${round(props['v_mean'], 3)}</td>
          <td>${round(props['wei_a'], 3)}</td>
          <td>${round(props['wei_k'], 3)}</td>
        </tr>
        <tr>
          <td>345° - 15°</td>
          <td>${round(props['freq_0'], 3)} %</td>
          <td>${round(props['v_mean_0'], 3)}</td>
          <td>${round(props['wei_a_0'], 3)}</td>
          <td>${round(props['wei_k_0'], 3)}</td>
        </tr>
        <tr>
          <td>15° - 45°</td>
          <td>${round(props['freq_30'], 3)} %</td>
          <td>${round(props['v_mean_30'], 3)}</td>
          <td>${round(props['wei_a_30'], 3)}</td>
          <td>${round(props['wei_k_30'], 3)}</td>
        </tr>
        <tr><td>45° - 75°</td>
          <td>${round(props['freq_60'], 3)} %</td>
          <td>${round(props['v_mean_60'], 3)}</td>
          <td>${round(props['wei_a_60'], 3)}</td>
          <td>${round(props['wei_k_60'], 3)}</td>
        </tr>
        <tr>
          <td>75° - 105°</td>
          <td>${round(props['freq_90'], 3)} %</td>
          <td>${round(props['v_mean_90'], 3)}</td>
          <td>${round(props['wei_a_90'], 3)}</td>
          <td>${round(props['wei_k_90'], 3)}</td>
        </tr>
        <tr>
          <td>105° - 135°</td>
          <td>${round(props['freq_120'], 3)} %</td>
          <td>${round(props['v_mean_120'], 3)}</td>
          <td>${round(props['wei_a_120'], 3)}</td>
          <td>${round(props['wei_k_120'], 3)}</td>
        </tr>
        <tr>
          <td>135° - 165°</td>
          <td>${round(props['freq_150'], 3)} %</td>
          <td>${round(props['v_mean_150'], 3)}</td>
          <td>${round(props['wei_a_150'], 3)}</td>
          <td>${round(props['wei_k_150'], 3)}</td>
        </tr>
        <tr>
          <td>165° - 195°</td>
          <td>${round(props['freq_180'], 3)} %</td>
          <td>${round(props['v_mean_180'], 3)}</td>
          <td>${round(props['wei_a_180'], 3)}</td>
          <td>${round(props['wei_k_180'], 3)}</td>
        </tr>
        <tr>
          <td>195° - 225°</td>
          <td>${round(props['freq_210'], 3)} %</td>
          <td>${round(props['v_mean_210'], 3)}</td>
          <td>${round(props['wei_a_210'], 3)}</td>
          <td>${round(props['wei_k_210'], 3)}</td>
        </tr>
        <tr>
          <td>225° - 255°</td>
          <td>${round(props['freq_240'], 3)} %</td>
          <td>${round(props['v_mean_240'], 3)}</td>
          <td>${round(props['wei_a_240'], 3)}</td>
          <td>${round(props['wei_k_240'], 3)}</td>
        </tr>
        <tr>
          <td>255° - 285°</td>
          <td>${round(props['freq_270'], 3)} %</td>
          <td>${round(props['v_mean_270'], 3)}</td>
          <td>${round(props['wei_a_270'], 3)}</td>
          <td>${round(props['wei_k_270'], 3)}</td>
        </tr>
        <tr>
          <td>285° - 315°</td>
          <td>${round(props['freq_300'], 3)} %</td>
          <td>${round(props['v_mean_300'], 3)}</td>
          <td>${round(props['wei_a_300'], 3)}</td>
          <td>${round(props['wei_k_300'], 3)}</td></tr>
        <tr>
          <td>315° - 345°</td>
          <td>${round(props['freq_330'], 3)} %</td>
          <td>${round(props['v_mean_330'], 3)}</td>
          <td>${round(props['wei_a_330'], 3)}</td>
          <td>${round(props['wei_k_330'], 3)}</td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td class="inner-table" colspan="2">
      <b>${_('tt_bfe_windrichtung_weibullverteilung')}</b><br/>${_('tt_bfe_windstaerke_info')}<br/><div id="weibull"></div>
      <table id="windrichtung">
        <tr>
          <th>${_('tt_bfe_geschwindigkeit')}</th>
          <th style="text-align:right">${_('tt_bfe_haeufigkeit')}</th>
        </tr>
        <tr>
          <td>0 m/s</td>
          <td style="text-align:right">
            <div id="wind0"></div>
          </td>
        </tr>
        <tr>
          <td>1 m/s</td>
          <td style="text-align:right">
            <div id="wind1"></div>
          </td>
        </tr>
        <tr>
          <td>2 m/s</td>
          <td style="text-align:right">
            <div id="wind2"></div>
          </td>
        </tr>
        <tr>
          <td>3 m/s</td>
          <td style="text-align:right">
            <div id="wind3"></div>
          </td>
        </tr>
        <tr>
          <td>4 m/s</td>
          <td style="text-align:right">
            <div id="wind4"></div>
          </td>
        </tr>
        <tr>
          <td>5 m/s</td>
          <td style="text-align:right">
            <div id="wind5"></div>
          </td>
        </tr>
        <tr>
          <td>6 m/s</td>
          <td style="text-align:right">
            <div id="wind6"></div>
          </td>
        </tr>
        <tr>
          <td>7 m/s</td>
          <td style="text-align:right">
            <div id="wind7"></div>
          </td>
        </tr>
        <tr>
          <td>8 m/s</td>
          <td style="text-align:right">
            <div id="wind8"></div>
          </td>
        </tr>
        <tr>
          <td>9 m/s</td>
          <td style="text-align:right">
            <div id="wind9"></div>
          </td>
        </tr>
        <tr>
          <td>10 m/s</td>
          <td style="text-align:right">
            <div id="wind10"></div>
          </td>
        </tr>
        <tr>
          <td>11 m/s</td>
          <td style="text-align:right">
            <div id="wind11"></div>
          </td>
        </tr>
        <tr>
          <td>12 m/s</td>
          <td style="text-align:right">
            <div id="wind12"></div>
          </td>
        </tr>
        <tr>
          <td>13 m/s</td>
          <td style="text-align:right">
            <div id="wind13"></div>
          </td>
        </tr>
        <tr>
          <td>14 m/s</td>
          <td style="text-align:right">
            <div id="wind14"></div>
          </td>
        </tr>
        <tr>
          <td>15 m/s</td>
          <td style="text-align:right">
            <div id="wind15"></div>
          </td>
        </tr>
        <tr>
          <td>16 m/s</td>
          <td style="text-align:right">
            <div id="wind16"></div>
          </td>
        </tr>
        <tr>
          <td>17 m/s</td>
          <td style="text-align:right">
            <div id="wind17"></div>
          </td>
        </tr>
        <tr>
          <td>18 m/s</td>
          <td style="text-align:right">
            <div id="wind18"></div>
          </td>
        </tr>
        <tr>
          <td>19 m/s</td>
          <td style="text-align:right">
            <div id="wind19"></div>
          </td>
        </tr>
        <tr>
          <td>20 m/s</td>
          <td style="text-align:right">
            <div id="wind20"></div>
          </td>
        </tr>
        <tr>
          <td>Summe</td>
          <td style="text-align:right">
            <div id="windsumme"></div>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<script>
//WINDROSE DATA
var data = [
  {"speed":${props['v_mean_0']},"frequency":${props['freq_0']},"weight":1,"color":"#045a8d","orientation":"345° – 15°"},
  {"speed":${props['v_mean_30']},"frequency":${props['freq_30']},"weight":1,"color":"#bdc9e1","orientation":"15° – 45°"},
  {"speed":${props['v_mean_60']},"frequency":${props['freq_60']},"weight":1,"color":"#2b8cbe","orientation":"45° – 75°"},
  {"speed":${props['v_mean_90']},"frequency":${props['freq_90']},"weight":1,"color":"#74a9cf","orientation":"75° – 105°"},
  {"speed":${props['v_mean_120']},"frequency":${props['freq_120']},"weight":1,"color":"#f1eef6","orientation":"105° – 135°"},
  {"speed":${props['v_mean_150']},"frequency":${props['freq_150']},"weight":1,"color":"#2b8cbe","orientation":"135° – 165°"},
  {"speed":${props['v_mean_180']},"frequency":${props['freq_180']},"weight":1,"color":"#2b8cbe","orientation":"165° – 195°"},
  {"speed":${props['v_mean_210']},"frequency":${props['freq_210']},"weight":1,"color":"#f1eef6","orientation":"195° – 225°"},
  {"speed":${props['v_mean_240']},"frequency":${props['freq_240']},"weight":1,"color":"#74a9cf","orientation":"225° – 255°"},
  {"speed":${props['v_mean_270']},"frequency":${props['freq_270']},"weight":1,"color":"#f1eef6","orientation":"255° – 285°"},
  {"speed":${props['v_mean_300']},"frequency":${props['freq_300']},"weight":1,"color":"#045a8d","orientation":"285° –315°"},
  {"speed":${props['v_mean_330']},"frequency":${props['freq_330']},"weight":1,"color":"#f1eef6","orientation":"315° – 345°"},
];


//WINDROSE
% if iframe:
var width = 175,
    height = 175,
% else:
var width = 300,
    height = 300,
% endif
    radius = Math.min(width, height) / 2,
    innerRadius = 0.05 * radius;

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.width; });

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([0, 0])
  .html(function(d) {
    return d.data.orientation + ": <br><span style='color:orangered'>" + d.data.frequency.toFixed(2) + " %<br>" + d.data.speed.toFixed(2) + " m/s</span>";
  });

//Kuchenstuecke definieren
var arc = d3.svg.arc()
  .innerRadius(innerRadius)
  .outerRadius(function (d) {
    return (radius - innerRadius) * (d.data.frequency / 20) + innerRadius; //Aussenlinie gleich 20%
  })
  .startAngle(function(d) { return d.startAngle + Math.PI*1.9166667; }) //Alle um 345 schieben
  .endAngle(function(d) { return d.endAngle + Math.PI*1.9166667; }); //Alle um 345 schieben

//svg definieren
var svg = d3.select("#rose").append("svg")
% if iframe:
    .attr("width", width + 58) 
% else:
    .attr("width", width + 48 + 140) //+140 damit rechts noch Legende Platz hat
% endif
    .attr("height", height + 48)
    .append("g")
    .attr("transform", "translate(" + (width + 48) / 2 + "," + (height + 48) / 2 + ")");

svg.call(tip);

  data.forEach(function(d) {
    d.speed  = +d.speed;
    d.weight = +d.weight;
    d.frequency  = +d.frequency;
    d.width  = +d.weight;
    d.orientation  =  d.orientation;
  });

  //Kuchenstuecke hinzufuegen
  var path = svg.selectAll(".solidArc")
      .data(pie(data))
    .enter().append("path")
      .attr("fill", function(d) {
        if (d.data.speed < 4.0) {
            return "rgb(201,233,246)";
        } else if (d.data.speed < 4.5 & d.data.speed >= 4.0) {
            return "rgb(122,212,241)";
        } else if (d.data.speed < 5.0 & d.data.speed >= 4.5) {
            return "rgb(78,200,244)";
        } else if (d.data.speed < 5.5 & d.data.speed >= 5.0) {
            return "rgb(47,144,225)";
        } else if (d.data.speed < 6.0 & d.data.speed >= 5.5) {
            return "rgb(54,105,188)";
        } else if (d.data.speed < 6.5 & d.data.speed >= 6.0) {
            return "rgb(133,86,148)";
        } else if (d.data.speed < 7.0 & d.data.speed >= 6.5) {
            return "rgb(155,77,101)";
        } else if (d.data.speed < 7.5 & d.data.speed >= 7.0) {
            return "rgb(181,56,75)";
        } else if (d.data.speed < 8.0 & d.data.speed >= 7.5) {
            return "rgb(204,30,24)";
        } else if (d.data.speed >= 8.0) {
            return "rgb(187,8,5)";
        }
      })
      .attr("class", "solidArc")
      .attr("stroke", "gray")
      .attr("d", arc)
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);

//Beschriftungen Windrose
    svg.append("text")
    .text("0°")
% if iframe:
    .attr("x", "0")
    .attr("y", (-3-radius))
% else:
    .attr("x", "-3")
    .attr("y", "-153")
% endif
    .style("font-size", "10px")
    .attr("fill", "grey");

    svg.append("text")
    .text("180°")
    .attr("x", "-10")
% if iframe:
    .attr("y", (10+radius))
% else:
    .attr("y", "161")
% endif
    .style("font-size", "10px")
    .attr("fill", "grey");

    svg.append("text")
    .text("90°")
% if iframe:
    .attr("x", (3+radius))
    .attr("y", "0")
% else:
    .attr("x", "153")
    .attr("y", "3")
% endif
    .style("font-size", "10px")
    .attr("fill", "grey");

    svg.append("text")
    .text("270°")
% if iframe:
    .attr("x", (-24-radius))
    .attr("y", "0")
% else:
    .attr("x", "-174")
    .attr("y", "3")
% endif
    .style("font-size", "10px")
    .attr("fill", "grey");

    svg.append("text")
    .text("${_('tt_bfe_haeufigkeit')}")
    .style("font-size", "10px")
    .style("text-align", "center")
    .attr("fill", "grey")
% if iframe:
    .attr("transform", "translate(67,-82) rotate(45)");
% else:
    .attr("transform", "translate(108,-126) rotate(45)");
% endif
    svg.append("text")
    .text("20 %")
    .style("font-size", "10px")
    .attr("fill", "grey")
% if iframe:
    .attr("transform", "translate(63,-63) rotate(45)");
% else:
    .attr("transform", "translate(108,-108) rotate(45)");
% endif
    svg.append("text")
    .text("15 %")
    .style("font-size", "10px")
    .attr("fill", "grey")
% if iframe:
    .attr("transform", "translate(47,-47) rotate(45)");
% else:
    .attr("transform", "translate(80,-80) rotate(45)");
% endif
    svg.append("text")
    .text("10 %")
    .style("font-size", "10px")
    .attr("fill", "grey")
% if iframe:
    .attr("transform", "translate(32,-32) rotate(45)");
% else:
    .attr("transform", "translate(55,-55) rotate(45)");
% endif
    svg.append("circle")
    .attr("cx", "0")
    .attr("cy", "0")
    .attr("r", radius)
    .attr("stroke", "grey")
    .attr("stroke-width", "1")
    .attr("fill", "none");

    svg.append("circle")
    .attr("cx", "0")
    .attr("cy", "0")
    .attr("r", (radius / 2))
    .attr("stroke", "grey")
    .attr("stroke-width", "1")
    .attr("fill", "none");

    svg.append("circle")
    .attr("cx", "0")
    .attr("cy", "0")
    .attr("r", (radius / 4 * 3))
    .attr("stroke", "grey")
    .attr("stroke-width", "1")
    .attr("fill", "none");

//Legende rechts
    svg.append("rect")
    .attr("x", "190")
    .attr("y", "121") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(187,8,5)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 8.0 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,130)"); //0,-15
    svg.append("rect")
    .attr("x", "190")
    .attr("y", "106") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(204,30,24)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 7.5 – < 8.0 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,115)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "91") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(181,56,75)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 7.0 – < 7.5 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,100)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "76") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(155,77,101)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 6.5 – < 7.0 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,85)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "61") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(133,86,148)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 6.0 – < 6.5 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,70)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "46") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(54,105,188)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 5.5 – < 6.0 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,55)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "31") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(47,144,225)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 5.0 – < 5.5 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
     .attr("transform", "translate(215,40)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "16") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(78,200,244)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 4.5 – < 5.0 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,25)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "1") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(122,212,241)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("≥ 4.0 – < 4.5 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,10)"); //0,-15

    svg.append("rect")
    .attr("x", "190")
    .attr("y", "-14") //-15
    .attr("width", 20)
    .attr("height", 10)
    .style("fill", "rgb(201,233,246)")
    .style("stroke-width", "0");

    svg.append("text")
    .text("< 4.0 m/s")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(215,-5)"); //0,-15

    svg.append("text")
    .text("${_('tt_bfe_windgeschwindigkeit')}")
    .style("font-size", "10px")
    .attr("fill", "grey")
    .attr("transform", "translate(190,-20)");

//WEIBULL
// Daten fuer Darstellung der Weibull-Funktion generieren
var data = [],
    n = 10,
    k = ${props['wei_k']},
    A = ${props['wei_a']};
var probability;
var probabilitySum = 0;

for (var i = 0; i < 21; i++) {
    probability = (k/A) * Math.pow((i/A),(k-1)) * Math.pow(Math.E,-Math.pow((i/A),k));
    probabilitySum = probabilitySum + probability;
    data.push({x: i, y: probability});
    document.getElementById("wind" + i).innerHTML = (probability * 100).toFixed(2) + " %";
}
document.getElementById("windsumme").innerHTML = (Math.round(probabilitySum * 100)).toFixed(2) + " %";
// Ende Weibull-Daten
var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 488 - margin.left - margin.right,
    height = 250 - margin.top - margin.bottom;
var formatAsPercentage = d3.format("%");

var x = d3.scale.linear()
    .range([0, width]);
var y = d3.scale.linear()
    .range([height, 0]);
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");
var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(formatAsPercentage);
var line = d3.svg.line()
    .x(function(d) { return x(d.x); })
    .y(function(d) { return y(d.y); })
    .interpolate("cardinal");
var svg_weibull = d3.select("#weibull").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  x.domain(d3.extent(data, function(d) { return d.x; }));
  y.domain(d3.extent(data, function(d) { return d.y; }));
  svg_weibull.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);
  svg_weibull.append("g")
      .attr("class", "y axis")
      .call(yAxis);
  svg_weibull.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);
  svg_weibull.append("text")
    .text("${_('tt_bfe_haeufigkeit')}")
    .style("font-size", "10px")
    .style("text-align", "center")
    .attr("fill", "black")
    .attr("transform", "translate(-35,130) rotate(270)");

  svg_weibull.append("text")
    .text("${_('tt_bfe_windgeschwindigkeit')} [m/s]")
    .style("font-size", "10px")
    .style("text-align", "center")
    .attr("fill", "black")
    .attr("transform", "translate(140,228)");

</script>
</body>
</%def>


<%def name="extended_resources(c, lang)">
  <script src="${h.versioned(request.static_url('chsdi:static/js/d3.min.js'))}"></script>
  <script src="${h.versioned(request.static_url('chsdi:static/js/d3-tip.js'))}"></script>
</%def>
