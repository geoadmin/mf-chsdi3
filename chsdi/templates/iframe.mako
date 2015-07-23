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

% if param=='opacity':
<li> layer opacity (sans paramètre): <br />
<iframe src="${geoadmin_url}/embed.html?catalogNodes=9900&layers=ch.bafu.hydroweb-messstationen_gefahren&layers_opacity=0.8" name="IframeGeoadmin_1"></iframe>
<br />
<li> avec opacity = 0.2: <br />
<iframe src="${geoadmin_url}/embed.html?catalogNodes=9900&layers=ch.bafu.hydroweb-messstationen_gefahren&layers_opacity=0.2" name="IframeGeoadmin_2"></iframe>
<br />

<!-- GESTION DES TOPICS -->
% elif param=='topic':

<li> Topic ARE (gray background) <br />
<iframe src="${geoadmin_url}/embed.html?topic=are" name="Iframei_Topic_1"></iframe>
<br />
<br />

<li> Topic AVIATION <br />
Default layer : ch.bazl.luftfahrthindernis<br />
<iframe src="${geoadmin_url}/embed.html?topic=aviation" name="Iframe_Topic_2"></iframe>
<br />
<br />

<li> Topic BAFU <br />
<iframe src="${geoadmin_url}/embed.html?topic=bafu" name="Iframe_Topic_3"></iframe>
<br />
<br />

<li> Topic BLW (color background)<br />
<iframe src="${geoadmin_url}/embed.html?topic=blw" name="Iframe_Topic_4"></iframe>
<br />
<br />

<li> Topic ECH <br />
<iframe src="${geoadmin_url}/embed.html?topic=ech" name="Iframe_Topic_5"></iframe>
<br />
<br />

<li> Topic EMAPIS <br />
<iframe src="${geoadmin_url}/embed.html?topic=emapis" name="Iframe_Topic_6"></iframe>
<br />
<br />

<li> Topic FUNKSENDER (with default layers, background with color) <br />
<iframe src="${geoadmin_url}/embed.html?topic=funksender" name="Iframe_Topic_7"></iframe>
<br />
<br />

<li> Topic GEOL (with default layers)<br />
<iframe src="${geoadmin_url}/embed.html?topic=geol" name="Iframe_Topic_8"></iframe>
<br />
<br />

<li> Topic GEWISS (with default layers)<br />
<iframe src="${geoadmin_url}/embed.html?topic=gewiss" name="Iframe_Topic_9"></iframe>
<br />
<br />

<li> Topic INSPIRE (with default layers, background with color)<br />
<iframe src="${geoadmin_url}/embed.html?topic=inspire" name="Iframe_Topic_10"></iframe>
<br />
<br />

<li> Topic IVS (with default layers, background with color)<br />
<iframe src="${geoadmin_url}/embed.html?topic=ivs" name="Iframe_Topic_11"></iframe>
<br />
<br />

<li> Topic KGS (with default layers, background with color)<br />
<iframe src="${geoadmin_url}/embed.html?topic=kgs" name="Iframe_Topic_12"></iframe>
<br />
<br />

<li> Topic LUFTBILDER (with default layers)<br />
<iframe src="${geoadmin_url}/embed.html?topic=luftbilder" name="Iframe_Topic_13"></iframe>
<br />
<br />

<li> Topic NGA<br />
<iframe src="${geoadmin_url}/embed.html?topic=nga" name="Iframe_Topic_14"></iframe>
<br />
<br />

<li> Topic SACHPLAN<br />
<iframe src="${geoadmin_url}/embed.html?topic=sachplan" name="Iframe_Topic_15"></iframe>
<br />
<br />

<li> Topic SWISSTOPO (background with color)<br />
<iframe src="${geoadmin_url}/embed.html?topic=swisstopo" name="Iframe_Topic_16"></iframe>
<br />
<br />

<li> Topic VU<br />
<iframe src="${geoadmin_url}/embed.html?topic=vu" name="Iframe_Topic_17"></iframe>
<br />
<br />

<li> Topic WILDRUHEZONEN (with default layers)<br />
<iframe src="${geoadmin_url}/embed.html?topic=wildruhezonen" name="Iframe_Topic_18"></iframe>
<br />
<br />

% endif
