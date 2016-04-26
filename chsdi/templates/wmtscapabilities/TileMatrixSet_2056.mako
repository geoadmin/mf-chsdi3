<%page args="tmsDefs"/>

% for zoom in range(17, len(tmsDefs)):
<TileMatrixSet>
<ows:Identifier>2056_${zoom}</ows:Identifier>
<ows:SupportedCRS>urn:ogc:def:crs:EPSG:2056</ows:SupportedCRS>
    % for z in range(0,zoom + 1):
<TileMatrix>
<ows:Identifier>${z}</ows:Identifier>
<% scale = tmsDefs[z][3] %>
<ScaleDenominator>${scale}</ScaleDenominator>
<TopLeftCorner>2420000.0 1350000.0</TopLeftCorner>
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
