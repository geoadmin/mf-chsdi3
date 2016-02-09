<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    from pyramid.url import route_url
    protocol = request.scheme
    lang = request.lang
    topic = request.matchdict.get('map')
    host = h.make_agnostic(request.host_url + request.uscript_name)
    type_station = c['attributes']['betriebspunkttyp']
    id = c['featureId']
    c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
    host = request.registry.settings['api_url']
%>
<style>
  tr:last-child {
    display:none;
  }
  .oev-info {
    height:24px;
    margin:0px;
  }
  .col-label {
    text-align: center;
    width: 35px !important;
  }
  .col-destination, .col-departures, .col-time-diff {
     vertical-align: middle !important;
  } 
  .col-label p {
    border: 1px solid #D8D8D8;
    border-radius: 4px;
    width: 30px;
  }
  .col-label p, .col-destination p, .col-departures p, .col-time-diff p {
     padding-top: 5px;
     margin-bottom: 2px;
  }
</style>

% if type_station == 'Bedienpunkt' :

    <p><b>${c['attributes']['name'] or '-'}</b></p> 
    <p>${_('ch.bav.haltestellen-oev.bedienpunkt')}</p>

% elif type_station == 'Anschlusspunkt' : 

   <p><b>${c['attributes']['name'] or '-'}</b></p>
   <p>${_('ch.bav.haltestellen-oev.anschlusspunkt')}</p>

% elif type_station == 'reiner_Betriebspunkt' :

   <p><b>${c['attributes']['name'] or '-'}</b></p>
   <p>${_('ch.bav.haltestellen-oev.reiner_betriebspunkt')}</p>

% else:

<script>

$(document).ready(function() {
  var refresh;
  var id = '${id}';
  var select = $('#selectDestination' + id);
  var numeroCol = $('#numero' + id);
  var destinationCol = $('#destination' + id);
  var departuresCol = $('#departures' + id);
  var timeDiffCol = $('#timeDiff' + id);
    
  select.change(function() {
    onSelect(this.value);
  });

  // Get infos for a specific destination
  var timesRun = 0;
  var dest;
  var getInfos = function(val){
    timesRun += 1;
    if (val) {
      dest = val;
    }
    if(timesRun === 20){
      clearInterval(refresh);
    }
    $.getJSON( "${host}/stationboard/stops/${id}?destination=" + encodeURIComponent(dest), function(result2){
      var numero = '';
      var destination = '';
      var departures = '';
      var timeDiff = '';
      for (var i = 0; i < result2.length; i++) {
        if (dest == 'nodata' || result2[i].destination == 'nodata'){
          destination += '<p style="height:24px; margin:0px;">${_("ch.bav.haltestellen-oev.nodata2")}</p>';
        } else {
          var now = result2[i].currentDate;
          var then = result2[i].departureDate;
          var diff = moment(then,"DD/MM/YYYY HH:mm").diff(moment(now,"DD/MM/YYYY HH:mm"));
          var d = moment.duration(diff);
          var s = Math.floor(d.asMinutes()) + moment.utc(diff).format("[']", -1);
          numero += '<p class="oev-info">' + result2[i].label + '</p>';
          destination += '<p class="oev-info">' + result2[i].destinationName + '</p>';
          departures += '<p class="oev-info">' + result2[i].time + '</p>';
          timeDiff += '<p class="oev-info"><b>' + s +'</b></p>';
        }
      };
      numeroCol.html(numero);
      destinationCol.html(destination);
      departuresCol.html(departures);
      timeDiffCol.html(timeDiff);
    }); 
  };

  var onSelect = function(val) {
    if (refresh) {
      clearInterval(refresh);
    }
    getInfos(val); 
    refresh = setInterval(getInfos, 60000);
  };

  $.getJSON( "${host}/stationboard/stops/${id}/destinations", function(result){
    var selectDestination = '';
    for (var i = 0; i < result.length; i++) {
      if (result[i].destination == 'nodata') {
        selectDestination += '<option value="' + result[i].destination + '">${_("ch.bav.haltestellen-oev.nodata")}</option>';
      } else { 
        selectDestination += '<option value="' + result[i].name + '">' + result[i].name + '</option>';
      }
    };
    select.append(selectDestination);
    onSelect('all');
  });
});

</script>
    <br />
    <p><b>${c['attributes']['name'] or '-'}</b>, ${_('ch.bav.haltestellen-oev.next_departures')}:</p>
    <select id="selectDestination${id}">
      <option value="all">${_('ch.bav.haltestellen-oev.all_departures')}</option>
    </select>
    <br />
    <tr>
        <td id="numero${id}" class="col-label"></td>
        <td id="destination${id}" class="col-destination"></td>
        <td id="departures${id}" class="col-departures"></td>
        <td id="timeDiff${id}" class="col-time-diff"></td>
    </tr>
% endif
    <tr>
      <td></td>
      <td> 
        <p style="margin:10px 0 0 0;">
          <a href="${h.make_agnostic(request.route_url('extendedHtmlPopup', map=topic, layerId=c['layerBodId'], featureId=str(c['featureId'])))}?lang=${lang}"
             target="_blank">${_('zusatzinfo')}&nbsp;<img src="${h.versioned(request.static_url('chsdi:static/images/ico_extern.gif'))}" />
          </a>
        </p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>
        <p style="margin:0;">
          <a href="${''.join((c['baseUrl'], '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic, '&showTooltip=true'))}" target="new">
            ${_('Link to object')}
          </a>
        </p>
      </td>
    </tr>
</%def>

<%def name="extended_info(c, lang)">
    <%
        protocol = request.scheme
        lang = request.lang
        topic = request.matchdict.get('map')
        var_verkehrsmittel = '<i>haltestellen_' + c['attributes']['verkehrsmittel'] + '</i>'
        verkehr = var_verkehrsmittel.lower()
        type_station = c['attributes']['betriebspunkttyp']
        c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
    %>
<table>
  <tr>
      <td class="cell-meta">${_('ch.bav.haltestellen-oev.id')}</td>
      <td class="cell-meta">${c['featureId'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.name')}</td>
    <td class="cell-meta">${c['attributes']['name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.tuabkuerzung')}</td>
    <td class="cell-meta">${c['attributes']['tuabkuerzung'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.betriebspunkttyp')}</td>

% if type_station == 'Bedienpunkt' :

    <td class="cell-meta">${_('ch.bav.haltestellen-oev.bedienpunkt')}</td>

% elif type_station == 'Anschlusspunkt' :

   <td class="cell-meta">${_('ch.bav.haltestellen-oev.anschlusspunkt')}</td>

% elif type_station == 'reiner_Betriebspunkt' :

   <td class="cell-meta">${_('ch.bav.haltestellen-oev.reiner_betriebspunkt')}</td>

% elif type_station == 'Haltestelle' :

    <td class="cell-meta">${_('ch.bav.haltestellen-oev.haltestelle')}</td>

% endif
  </tr>
  <tr>
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.verkehrsmittel')}</td>
    <td class="cell-meta">${_(verkehr)}</td>
  </tr>
  <tr>
      <td class="cell-meta"></td>
      <td class="cell-meta"><p><a href="${''.join((c['baseUrl'], '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic, '&showTooltip=true'))}" target="new">
        ${_('Link to object')}
      </a></p></td>
  </tr> 
</table>
<br />
<div>
 <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
</div>
</%def>
