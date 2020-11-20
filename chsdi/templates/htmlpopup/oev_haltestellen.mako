<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
baseUrl = request.registry.settings['api_url']
%>
  <iframe src="${baseUrl}/rest/services/all/MapServer/${c['layerBodId']}/${c['featureId']}/iframeHtmlPopup?lang=${lang}" width="100%" height="165" frameborder="0" style="border: 0;" scrolling="no"></iframe>
</%def>


<%def name="iframe_content(c, lang)">
<%
    from pyramid.url import route_url
    protocol = request.scheme
    lang = request.lang
    topic = request.matchdict.get('map')
    host = h.make_agnostic(request.host_url + request.uscript_name)
    type_station = c['attributes']['betriebspunkttyp_de']
    id = c['featureId']
    c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
    host = request.registry.settings['api_url']
%>
<style>
  .${c['htmlpopup_class']} tr:last-child {
    display:none;
  }
  .${c['htmlpopup_class']} .oev-info {
    height:24px;
    margin:0px;
  }
  .${c['htmlpopup_class']} .oev-delay {
    color:red;
  }
  .${c['htmlpopup_class']} .col-label {
    text-align: center;
    width: 35px !important;
  }
  .${c['htmlpopup_class']} .col-destination, .${c['htmlpopup_class']} .col-departures, .${c['htmlpopup_class']} .col-time-diff, .${c['htmlpopup_class']} .col-delay {
     vertical-align: middle !important;
  }
  .${c['htmlpopup_class']} .col-label p {
    border: 1px solid #D8D8D8;
    border-radius: 4px;
    width: 30px;
  }
  .${c['htmlpopup_class']} .col-label p, .${c['htmlpopup_class']} .col-destination p, .${c['htmlpopup_class']} .col-departures p, .${c['htmlpopup_class']} .col-time-diff p, .${c['htmlpopup_class']} .col-delay p {
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
  $.ajaxSetup({ cache: false });
  var refresh;
  var id = '${id}';
  var numeroCol = $('#numero' + id);
  var destinationCol = $('#destination' + id);
  var departuresCol = $('#departures' + id);
  var timeDiffCol = $('#timeDiff' + id);
  var predictableDelayCol = $('#predictableDelay' + id);

  var timesRun = 0;
  var getInfos = function(val){
    timesRun += 1;
    if(timesRun === 20){
      clearInterval(refresh);
    }
    $.getJSON( '${host}/stationboard/stops/${id}', function(result){
      var numero = '';
      var destination = '';
      var departures = '';
      var timeDiff = '';
      var delay = '';
      var late = '';
      var classLate = '';
      for (var i = 0; i < result.length; i++) {
          var now = result[i].currentDate;
          var then = result[i].departureDate;
          var estimatedThen = result[i].estimatedDate;
          if (estimatedThen != 'nodata'){
            classLate = 'oev-delay';
            var lateDiff = moment(estimatedThen,'DD/MM/YYYY HH:mm').diff(moment(then,'DD/MM/YYYY HH:mm'));
            var lateD = moment.duration(lateDiff);
            late = '(+' + Math.floor(lateD.asMinutes()) + moment.utc(lateD).format('[\']', -1) + ')';
            if (late == '(+0\')'){ // do not show anything when the delay is 0
              late = '';
              classLate = '';
            }
            then = estimatedThen; // when there is a delay we take the estimated date
          }
          var label = result[i].label;
          if (label == null){ // some labels are null
            label = '-';
          }
          if (label.length > 2){ // some labels are too long
            label = label.substr(0, 3);
          }
          var time = moment(then, 'DD/MM/YYY HH:mm').format('HH:mm');
          var diff = moment(then,'DD/MM/YYYY HH:mm').diff(moment(now,'DD/MM/YYYY HH:mm'));
          var d = moment.duration(diff);
          var s = Math.floor(d.asMinutes()) + moment.utc(diff).format('[\']', -1);
          numero += '<p class="oev-info">' + label + '</p>';
          destination += '<p class="oev-info">' + result[i].destinationName + '</p>';
          departures += '<p class="oev-info ' + classLate + '">' + time + '</p>';
          timeDiff += '<p class="oev-info ' + classLate + '"><b>' + s +'</b></p>';
          delay += '<p class="oev-info oev-delay">' + late +'&nbsp;</p>';
      };
      numeroCol.html(numero);
      destinationCol.html(destination);
      departuresCol.html(departures);
      timeDiffCol.html(timeDiff);
      predictableDelayCol.html(delay);
    }).fail(function() {
      destinationCol.html('<p style="height:24px; margin:0px;">${_("ch.bav.haltestellen-oev.nodata2")}</p>');
    });
  };

  var Refresh = function(val) {
    if (refresh) {
      clearInterval(refresh);
    }
    getInfos(val);
    refresh = setInterval(getInfos, 60000);
  };
  Refresh();

});

</script>
    <p><b>${c['attributes']['name'] or '-'}</b>, ${_('ch.bav.haltestellen-oev.next_departures')}:</p>
  <table>
    <tr>
        <td id="numero${id}" class="col-label"></td>
        <td id="destination${id}" class="col-destination"></td>
        <td id="departures${id}" class="col-departures"></td>
        <td id="timeDiff${id}" class="col-time-diff"></td>
        <td id="predictableDelay${id}" class="col-delay"></td>
    </tr>
    <tr>
      <td colspan="5">&nbsp;</td>
    </tr>
  </table>
% endif
</%def>


<%def name="extended_info(c, lang)">
<%
    protocol = request.scheme
    lang = request.lang
    topic = request.matchdict.get('map')
    if c['attributes']['verkehrsmittel_de']:
      var_verkehrsmittel = '<i>haltestellen_' + c['attributes']['verkehrsmittel_de'] + '</i>'
    else:
      var_verkehrsmittel = '-'
    verkehr = var_verkehrsmittel.lower()
    type_station = c['attributes']['betriebspunkttyp_de']
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
    <td class="cell-meta">${_('ch.bav.haltestellen-oev.abkuerzung')}</td>
    <td class="cell-meta">${c['attributes']['abkuerzung'] or '-'}</td>
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
    <td class="cell-meta">${c['attributes']['verkehrsmittel_de'] or '-'}</td>
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

<%def name="extended_resources(c, lang)">
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.16.0/moment.min.js"></script>
</%def>
