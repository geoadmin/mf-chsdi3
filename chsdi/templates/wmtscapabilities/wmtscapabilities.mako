<?xml version="1.0" encoding="UTF-8"?>
<%
  from chsdi.lib.helpers import to_utf8
  layers = pageargs['layers']
  metadata = pageargs['metadata']
  themes = pageargs['themes']
  scheme = pageargs['scheme']
  onlineressource = pageargs['onlineressource']
  tilematrixset = pageargs['tilematrixset']
  tmsDefs = pageargs['tilematrixsetDefs']
  zoomLevels = pageargs['zoomlevels']
  epsg = tilematrixset
  TileMatrixSet_epsg = "TileMatrixSet_%s.mako" % epsg
  def pad(num):
      return str(num).zfill(2)
%>
<Capabilities xmlns="http://www.opengis.net/wmts/1.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gml="http://www.opengis.net/gml" xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetCapabilities_response.xsd" version="1.0.0">
<%include file="standardHeader.mako" args="epsg=epsg"/>
   <ows:OperationsMetadata>
        <ows:Operation name="GetCapabilities">
            <ows:DCP>
                <ows:HTTP>
                    <ows:Get xlink:href="${onlineressource}1.0.0/WMTSCapabilities.xml">
                        <ows:Constraint name="GetEncoding">
                            <ows:AllowedValues>
                                <ows:Value>REST</ows:Value>
                            </ows:AllowedValues>
                        </ows:Constraint>
                    </ows:Get>
                </ows:HTTP>
            </ows:DCP>
        </ows:Operation>
        <ows:Operation name="GetTile">
            <ows:DCP>
                <ows:HTTP>
                    <ows:Get xlink:href="${onlineressource}">
                        <ows:Constraint name="GetEncoding">
                            <ows:AllowedValues>
                                <ows:Value>REST</ows:Value>
                            </ows:AllowedValues>
                        </ows:Constraint>
                    </ows:Get>
                </ows:HTTP>
            </ows:DCP>
        </ows:Operation>
    </ows:OperationsMetadata>
    <Contents>
  ## Main loop
   % for layer in layers:
        <Layer>
            <ows:Title>${layer.kurzbezeichnung or '-'|n,x,trim}</ows:Title>
            <ows:Abstract>${layer.abstract or '-'|n,x,trim}</ows:Abstract>
            <ows:WGS84BoundingBox>
                <ows:LowerCorner>5.140242 45.398181</ows:LowerCorner>
                <ows:UpperCorner>11.47757 48.230651</ows:UpperCorner>
            </ows:WGS84BoundingBox>
            <ows:Identifier>${layer.id|n,x,trim}</ows:Identifier>
            <ows:Metadata xlink:href="https://www.geocat.ch/geonetwork/srv/ger/md.viewer#/full_view/${layer.idGeoCat}"/>
            <Style>
                <ows:Title>${layer.kurzbezeichnung or '-'|n,x,trim}</ows:Title>
                <ows:Identifier>${layer.id or '-'|n,x,trim}</ows:Identifier>
                ## TODO relative path
                <% legendName = "/var/www/vhosts/mf-chsdi3/private/chsdi/chsdi/static/images/legends/" + to_utf8(layer.id) + "_" + to_utf8(request.lang) + ".png" %>
                <%! import os.path %>
                <% hasLegend = os.path.isfile(legendName) %>
                % if hasLegend:
                <LegendURL format="image/png" xlink:href="${scheme}://api3.geo.admin.ch/static/images/legends/${layer.id|n,x,trim}_${request.lang|n,x,trim}.png" />
                % endif
            </Style>
            % if layer.id == 'ch.swisstopo.zeitreihen' and epsg == '21781':
            <Format>image/png</Format>
            % endif
            <Format>image/${str(layer.arr_all_formats).split(',')[0]}</Format>
            ## All dimensions
            <Dimension>
                <ows:Identifier>Time</ows:Identifier>
                <Default>${str(layer.timestamp).split(',')[0]}</Default>
                % if layer.id == 'ch.kantone.cadastralwebmap-farbe':
                <Current>true</Current>
                % endif
                % for timestamp in layer.timestamp.split(','):
                <Value>${timestamp}</Value>
                % endfor
            </Dimension>
            <TileMatrixSetLink>
                <TileMatrixSet>${epsg}_${str(layer.getClosestZoom(epsg, layer.resolution_max))}</TileMatrixSet>
            </TileMatrixSetLink>
            ## Zeitreihen has two formats available 'png' (desktop GIS) and (pngjpeg) web gis
            % if layer.id == 'ch.swisstopo.zeitreihen' and epsg == '21781':
                <ResourceURL format="image/png" resourceType="tile" template="${onlineressource}1.0.0/${layer.id|n,x,trim}/default/{Time}/${epsg}/{TileMatrix}/{TileRow}/{TileCol}.png"/>
            % endif
            ## ACHTUNG: s3 tiles have a row/col order, mapproxy ones the standard col/row
            % if epsg in ['21781']:
                <ResourceURL format="image/${str(layer.arr_all_formats).split(',')[0]}" resourceType="tile" template="${onlineressource}1.0.0/${layer.id|n,x,trim}/default/{Time}/${epsg}/{TileMatrix}/{TileRow}/{TileCol}.${str(layer.arr_all_formats).split(',')[0]}"/>
            % else:
            ## Maproxy order
                <ResourceURL format="image/${str(layer.arr_all_formats).split(',')[0]}" resourceType="tile" template="${onlineressource}1.0.0/${layer.id|n,x,trim}/default/{Time}/${epsg}/{TileMatrix}/{TileCol}/{TileRow}.${str(layer.arr_all_formats).split(',')[0]}"/>
            % endif
        </Layer>
  % endfor
  ## End main loop
        <%include file="TileMatrixSet.mako" args="tmsDefs=tmsDefs, zoomLevels=zoomLevels, epsg=epsg"/>
    </Contents>
    <Themes>
    ## Main loop for the themes
    ## The DB-list is ordered by oberthema_id
   <% pre_oberthema= 'not_yet' %>
   <% counter_i = 0 %>
   % for theme in themes:
   ## Oberthema
       % if not(pre_oberthema== theme.oberthema_id):
           <Theme>
               <ows:Title>${theme.inspire_oberthema_name or '-'|n,x,trim}</ows:Title>
               <ows:Abstract>${theme.inspire_oberthema_abstract or '-'|n,x,trim}</ows:Abstract>
               <ows:Identifier>${theme.oberthema_id or '-'|n,x,trim}</ows:Identifier>
       % endif
       ## Second level Thema
               <Theme>
                   <ows:Title>${theme.inspire_name or '-'|n,x,trim}</ows:Title>
                   <ows:Abstract>${theme.inspire_abstract or '-'|n,x,trim}</ows:Abstract>
                   <ows:Identifier>${theme.id or '-'|n,x,trim}</ows:Identifier>
                   ## Refs
                   <% layers = theme.fk_dataset_id.split(',')  %>
                   % for i in range(len(layers)):
                       <LayerRef>${layers[i]}</LayerRef>
                   % endfor
               </Theme>
       ## No overflow
       % if counter_i < (len(themes) - 1):
           <% counter_i = counter_i + 1 %>
       % endif
       ## End Oberthema if next oberthema is not the same as the current one
       % if not(theme.oberthema_id == themes[counter_i].oberthema_id):
           </Theme>
       % endif
       ## remember the precedent Oberthema
       <% pre_oberthema= theme.oberthema_id %>
    % endfor
    ## End main loop
    ## could be that the db ist empty
    % if len(themes) > 0:
    </Theme>
    % endif
  </Themes>
    <ServiceMetadataURL xlink:href="${onlineressource}1.0.0/WMTSCapabilities.xml"/>
</Capabilities>
