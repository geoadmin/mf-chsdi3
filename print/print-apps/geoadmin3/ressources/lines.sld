<?xml version="1.0" encoding="UTF-8"?>
    <sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
      <sld:UserLayer>
            <sld:LayerFeatureConstraints>
              <sld:FeatureTypeConstraint/>
            </sld:LayerFeatureConstraints>
            <sld:UserStyle>
              <sld:Name>Trails</sld:Name>
              <sld:Title/>
              <sld:FeatureTypeStyle>
                    <sld:Rule>
                      <sld:LineSymbolizer>
                            <sld:Stroke>
                              <sld:GraphicStroke>
                                    <sld:Graphic>
                                      <sld:Mark>
                                            <sld:WellKnownName>circle</sld:WellKnownName>
                                            <sld:Fill>
                                              <sld:CssParameter name="fill">#AA0000</sld:CssParameter>
                                            </sld:Fill>
                                      </sld:Mark>
                                      <sld:Size>
                                            <ogc:Literal>6</ogc:Literal>
                                      </sld:Size>
                                    </sld:Graphic>
                              </sld:GraphicStroke>
                              <sld:CssParameter name="stroke-dasharray">6 18</sld:CssParameter>
                            </sld:Stroke>
                      </sld:LineSymbolizer>
                      <sld:LineSymbolizer>
                            <sld:Stroke>
                              <sld:CssParameter name="stroke">#AA0000</sld:CssParameter>
                              <sld:CssParameter name="stroke-dasharray">10 14</sld:CssParameter>
                              <sld:CssParameter name="stroke-dashoffset">14</sld:CssParameter>
                            </sld:Stroke>
                      </sld:LineSymbolizer>
                    </sld:Rule>
              </sld:FeatureTypeStyle>
            </sld:UserStyle>
      </sld:UserLayer>
    </sld:StyledLayerDescriptor>
