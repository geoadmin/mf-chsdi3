<%page args="tmsDefs"/>

% for zoom in range(17, len(tmsDefs)):
<TileMatrixSet>
<ows:Identifier>21781_${zoom}</ows:Identifier>
<ows:SupportedCRS>urn:ogc:def:crs:EPSG:21781</ows:SupportedCRS>
<!-- This tileMatrixSet in **only** for tiles generated through TileGenerator ! -->
    % for z in range(0,zoom + 1):
<TileMatrix>
<ows:Identifier>${z}</ows:Identifier>
<% scale = tmsDefs[z][3] %>
<ScaleDenominator>${scale}</ScaleDenominator>
<TopLeftCorner>420000.0 350000.0</TopLeftCorner>
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
