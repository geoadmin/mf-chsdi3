<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor
    xmlns="http://www.opengis.net/sld"
    xmlns:sld="http://www.opengis.net/sld"
    xmlns:ogc="http://www.opengis.net/ogc"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:gml="http://www.opengis.net/gml" version="1.1.0">
    <sld:UserLayer>
        <sld:UserStyle>
            <sld:FeatureTypeStyle>
                <sld:Rule>
                             <sld:LineSymbolizer>
                            <sld:Stroke>
                              <sld:CssParameter name="stroke">#AA0000</sld:CssParameter>
                            </sld:Stroke>
                      </sld:LineSymbolizer>
                    <sld:PolygonSymbolizer>
                            <sld:Fill>
                              <sld:GraphicFill>
                                    <sld:Graphic>
                                     <sld:Mark>
                                        <!-- as defined in the mapfile symbole list -->
                                        <sld:WellKnownName>shape://vertline</sld:WellKnownName>
                                    </sld:Mark>
                                    </sld:Graphic>
                              </sld:GraphicFill>
                            </sld:Fill>
                    </sld:PolygonSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>
