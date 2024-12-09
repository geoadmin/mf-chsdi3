def generate_mock_response(departures, now):
    """Generate a dynamic mock OJP response with correct structure."""
    departure_events = "".join(
        f"""
        <StopEventResult>
            <StopEvent>
                <ThisCall>
                    <CallAtStop>
                        <siri:StopPointRef>{dep['id']}</siri:StopPointRef>
                        <StopPointName>
                            <Text>{dep['label']}</Text>
                        </StopPointName>
                        <ServiceDeparture>
                            <TimetabledTime>{dep['departureDate']}</TimetabledTime>
                            <EstimatedTime>{dep.get('estimatedDate', dep['departureDate'])}</EstimatedTime>
                        </ServiceDeparture>
                    </CallAtStop>
                </ThisCall>
                <Service>
                    <PublishedServiceName>
                        <Text>{dep['label']}</Text>
                    </PublishedServiceName>
                    <DestinationText>
                        <Text>{dep['destinationName']}</Text>
                    </DestinationText>
                    <DestinationStopPointRef>{dep['destinationId']}</DestinationStopPointRef>
                </Service>
            </StopEvent>
        </StopEventResult>
        """
        for dep in departures
    )

    mock_response = f"""<?xml version="1.0" ?>
    <OJP xmlns:siri="http://www.siri.org.uk/siri" xmlns="http://www.vdv.de/ojp" version="2.0">
        <OJPResponse>
            <siri:ServiceDelivery>
                <siri:ResponseTimestamp>{now}</siri:ResponseTimestamp>
                <OJPStopEventDelivery>
                    <siri:ResponseTimestamp>{now}</siri:ResponseTimestamp>
                    {departure_events}
                </OJPStopEventDelivery>
            </siri:ServiceDelivery>
        </OJPResponse>
    </OJP>"""

    return mock_response


def generate_mock_empty_response(now):
    # This mocked response will contain just enough for parsing, but will
    # lead to no detected station, i.e.: station not existing case
    mock_response = f"""<?xml version="1.0" ?>
    <OJP xmlns:siri="http://www.siri.org.uk/siri" xmlns="http://www.vdv.de/ojp" version="2.0">
        <OJPResponse>
            <siri:ServiceDelivery>
                <siri:ResponseTimestamp>{now}</siri:ResponseTimestamp>
                <OJPStopEventDelivery>
                    <siri:ResponseTimestamp>{now}</siri:ResponseTimestamp>
                    <!-- No StopEventResult entries -->
                </OJPStopEventDelivery>
            </siri:ServiceDelivery>
        </OJPResponse>
    </OJP>"""

    return mock_response
