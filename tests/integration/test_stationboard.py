from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
import re

from pytz import timezone
from dateutil import tz
from chsdi.lib.opentransapi import opentransapi


def format_time(str_date_time, fmt="%Y-%m-%dT%H:%M:%SZ"):
    from_zone = tz.tzutc()
    to_zone = tz.gettz('Europe/Zurich')

    try:
        date_time = datetime.strptime(str_date_time, fmt)
    except ValueError:
        # sometimes the timestamp of the OJP 2.0 API's response has 7 digits for the
        # milliseconds. 6 are expected and only 6 can be handled by Python.
        # Hence we need to safely truncate everything between the last . and
        # the +01:00 part of the timestamp, e.g.:
        # 2024-11-01T15:39:45.5348804+01:00
        # Use regex to capture and truncate everything between the last '.' and
        # the first '+' to 6 digits
        truncated_date_time = re.sub(r'(\.\d{6})\d*(?=\+)', r'\1', str_date_time)
        date_time = datetime.strptime(truncated_date_time, '%Y-%m-%dT%H:%M:%S.%f%z')
    date_time_utc = date_time.replace(tzinfo=from_zone)
    date_time_zurich = date_time_utc.astimezone(to_zone)
    return date_time_zurich.strftime('%d/%m/%Y %H:%M')


class TestStationboard(TestCase):
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
        return f"""<?xml version="1.0" ?>
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

    @patch.object(opentransapi.OpenTrans, "send_post")
    def test_stationboard(self, mock_send_post):
        """Test fetching stationboard with valid data."""
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_departures = [
            {
                "id": "ch:1:sloid:30813::1",
                "label": "Zurich, Diagon Alley",
                "currentDate": now,
                "departureDate": "2024-11-19T08:52:00Z",
                "estimatedDate": "2024-11-19T08:52:00Z",
                "destinationName": "Hogwarts",
                "destinationId": "ch:1:sloid:91178::3",
            }
        ]
        mock_send_post.return_value = self.generate_mock_response(mock_departures, now).encode("utf-8")

        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        results = api.get_departures(8501120, number_results=1)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "ch:1:sloid:30813::1")
        self.assertEqual(results[0]["label"], "Zurich, Diagon Alley")
        self.assertEqual(results[0]["currentDate"], format_time(now))
        self.assertEqual(results[0]["departureDate"], format_time("2024-11-19T08:52:00Z"))
        self.assertEqual(results[0]["estimatedDate"], format_time("2024-11-19T08:52:00Z"))
        self.assertEqual(results[0]["destinationName"], "Hogwarts")
        self.assertEqual(results[0]["destinationId"], "ch:1:sloid:91178::3")

    @patch.object(opentransapi.OpenTrans, "send_post")
    def test_stationboard_missing_station(self, mock_send_post):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_send_post.return_value = self.generate_mock_response([], now).encode("utf-8")
        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures(999999)

    @patch.object(opentransapi.OpenTrans, "send_post")
    def test_stationboard_invalid_id(self, mock_send_post):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_send_post.return_value = self.generate_mock_response([], now).encode("utf-8")
        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures("invalid_id")

    @patch.object(opentransapi.OpenTrans, "send_post")
    def test_stationboard_invalid_number_results(self, mock_send_post):
        mock_send_post.side_effect = opentransapi.OpenTransException("The limit parameter must be an integer.")
        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        with self.assertRaises(opentransapi.OpenTransException):
            api.get_departures(8501120, number_results="lalala")
