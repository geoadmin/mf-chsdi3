from datetime import datetime
import re
from unittest.mock import Mock
from unittest.mock import patch

from pytz import timezone
from dateutil import tz
from pyramid.httpexceptions import HTTPBadRequest
import requests_mock

from chsdi.lib.opentransapi import opentransapi
from chsdi.views.stationboard import TransportView
from tests.integration import TestsBase


def format_time(str_date_time, fmt="%Y-%m-%dT%H:%M:%SZ"):
    from_zone = tz.tzutc()
    to_zone = tz.gettz('Europe/Zurich')

    try:
        date_time = datetime.strptime(str_date_time, fmt)
    except ValueError:
        truncated_date_time = re.sub(r'(\.\d{6})\d*(?=\+)', r'\1', str_date_time)
        date_time = datetime.strptime(truncated_date_time, '%Y-%m-%dT%H:%M:%S.%f%z')
    date_time_utc = date_time.replace(tzinfo=from_zone)
    date_time_zurich = date_time_utc.astimezone(to_zone)
    return date_time_zurich.strftime('%d/%m/%Y %H:%M')


class TestStationboard(TestsBase):
    def setUp(self):
        self.mock_api_key = "dummy_api_key"
        self.mock_url = "https://dummy-url.com"

    def generate_mock_response(self, departures, now):
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

    @requests_mock.Mocker()
    def test_stationboard(self, mock_requests):
        # Generate mock response
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_departures = [
            {
                "id": "ch:1:sloid:30813::1",
                "label": "Hogwarts Express",
                "currentDate": now,
                "departureDate": "2024-11-19T08:52:00Z",
                "estimatedDate": "2024-11-19T08:52:00Z",
                "destinationName": "Hogwarts",
                "destinationId": "ch:1:sloid:91178::3",
            }
        ]
        mock_response = self.generate_mock_response(mock_departures, now)

        mock_requests.post(
            self.mock_url,
            text=mock_response,
            status_code=200
        )

        # Initialize API and make the call
        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        results = api.get_departures(8501120, number_results=1)

        # Assertions
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "ch:1:sloid:30813::1")
        self.assertEqual(results[0]["label"], "Hogwarts Express")
        self.assertEqual(results[0]["currentDate"], format_time(now))
        self.assertEqual(results[0]["departureDate"], format_time("2024-11-19T08:52:00Z"))
        self.assertEqual(results[0]["estimatedDate"], format_time("2024-11-19T08:52:00Z"))
        self.assertEqual(results[0]["destinationName"], "Hogwarts")
        self.assertEqual(results[0]["destinationId"], "ch:1:sloid:91178::3")

    @requests_mock.Mocker()
    def test_stationboard_missing_station(self, mock_requests):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_response = self.generate_mock_response([], now)
        mock_requests.post(self.mock_url, text=mock_response, status_code=200)

        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures(999999)

    @requests_mock.Mocker()
    def test_stationboard_invalid_id(self, mock_requests):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_response = self.generate_mock_response([], now)
        mock_requests.post(self.mock_url, text=mock_response, status_code=200)

        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures("invalid_id")

    @patch('chsdi.views.stationboard.get_current_registry')
    def test_invalid_limit_param(self, mock_get_current_registry):

        mock_request = Mock()
        mock_request.matched_route.name = 'stationboard'
        mock_request.params = {}
        mock_request.matchdict = {'id': '8501120'}

        mock_registry = Mock()
        mock_registry.settings = {
            'opentrans_api_key': 'dummy_api_key',
            'opentrans_url': 'https://dummy-url.com',
        }
        mock_get_current_registry.return_value = mock_registry

        mock_request.params['limit'] = 'lalala'

        # Expect an HTTPBadRequest exception
        with self.assertRaises(HTTPBadRequest):
            TransportView(mock_request)
