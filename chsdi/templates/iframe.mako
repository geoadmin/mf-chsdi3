<h1>Iframe</h1>
<style type="text/css">
    iframe {
        width:60%;
        height:350px;
    }
    .element {
        background-color: white;
        padding-left: 8px;
        padding-bottom: 8px;
        padding-top: 8px;
        width: 220px;
        color: #555;
        font: 11px tahoma,arial,verdana,sans-serif;
    }
    .title {
        margin-top: -4px;
        font-weight: bold;
    }
</style>

<%!
  from pyramid.url import route_url
  import chsdi.lib.helpers as h
%>
<%
    defaultImageDisplay = '400,600,96'
    api_url = 'http:' + request.registry.settings['api_url']
    geoadmin_url = 'https://' + request.registry.settings['geoadminhost']
    param = request.params.get('param', defaultImageDisplay)
%>    
Parametre API : ${api_url}<br />
Paramètre Geoadmin : ${geoadmin_url}
Paramètre : ${param}

% if param=='opacity':
<li> layer opacity (sans paramètre): <br />
<iframe src="${geoadmin_url}/embed.html?catalogNodes=9900&layers=ch.bafu.hydroweb-messstationen_gefahren&layers_opacity=0.8" name="IframeGeoadmin_1"></iframe>
<br />
<li> avec opacity = 0.2: <br />
<iframe src="${geoadmin_url}/embed.html?catalogNodes=9900&layers=ch.bafu.hydroweb-messstationen_gefahren&layers_opacity=0.2" name="IframeGeoadmin_2"></iframe>
<br />
% elif param=='topic':

<li> Topic funksender (with default layers) <br />
<iframe src="${geoadmin_url}/embed.html?lang=fr&topic=funksender" name="IframeGeoadmin_3"></iframe>
<br />
% endif
