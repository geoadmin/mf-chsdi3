<%page args="tmsDefs, zoomLevels, epsg"/>

% for zoom in zoomLevels:
<TileMatrixSet>
  <ows:Identifier>${epsg}_${zoom}</ows:Identifier>
  <ows:SupportedCRS>urn:ogc:def:crs:EPSG:${epsg}</ows:SupportedCRS>
    % for z in range(0,zoom + 1):
    <TileMatrix>
      <ows:Identifier>${z}</ows:Identifier>
      <% scale = tmsDefs[z][3] %>
      <ScaleDenominator>${scale}</ScaleDenominator>
      <TopLeftCorner>${tmsDefs['MAXY']} ${tmsDefs['MINX']}</TopLeftCorner>
      <TileWidth>256</TileWidth>
      <TileHeight>256</TileHeight>
      <% matrix_width = tmsDefs[z][1] %>
      <MatrixWidth>${matrix_width}</MatrixWidth>
      <% matrix_height = tmsDefs[z][2] %>
      <MatrixHeight>${matrix_height}</MatrixHeight>
      </TileMatrix>
    % endfor
  </TileMatrixSet>
% endfor
