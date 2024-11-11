# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as et
from pytz import timezone
from datetime import datetime
from dateutil import tz
import re


class OpenTrans:

    def __init__(self, open_trans_api_key, open_trans_url):
        self.open_trans_api_key = open_trans_api_key  # Get API key from config .ini
        self.url = open_trans_url  # URL of API
        self.station_id = None

    def get_departures(self, station_id, number_results=5, request_dt_time=False):
        if not request_dt_time:
            request_dt_time = datetime.now(timezone('Europe/Zurich')).strftime('%Y-%m-%dT%H:%M:%S')
        self.station_id = station_id
        api_response_xml = self.send_post(station_id, request_dt_time, number_results)  # request_dt_time in format 2017-12-11T14:26:18Z
        results = self.xml_to_array(api_response_xml)
        return results

    def _format_time(self, str_date_time, fmt="%Y-%m-%dT%H:%M:%SZ"):
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

    def _convert_estimated_date(self, el_estimated):
        # the field estimatedDate is not mandatory
        if el_estimated == None:
            return 'nodata'
        return self._format_time(el_estimated.text)

    def _check_element(self, el_name, el):
        if el == None:
            raise OpenTransException("An xml node %s of the OpenTransportData API response is missing." % el_name)
        return el.text

    def xml_to_array(self, xml_data):
        # Define namespaces for OJP and SIRI
        ns = {
            'ojp': 'http://www.vdv.de/ojp',
            'siri': 'http://www.siri.org.uk/siri'
        }
        root = et.fromstring(xml_data.decode('utf-8'))
        el_stop_points = root.findall('.//ojp:StopEventResult/ojp:StopEvent', ns)

        if not el_stop_points:
            raise OpenTransNoStationException("No data available for the station %s." % str(self.station_id))

        results = []

        for el in el_stop_points:
            el_id = self._check_element('StopPointRef', el.find('.//siri:StopPointRef', ns))
            el_service_name = self._check_element('PublishedServiceName', el.find('.//ojp:Service/ojp:PublishedServiceName/ojp:Text', ns))
            el_current_date = self._check_element('ResponseTimestamp', root.find('.//siri:ResponseTimestamp', ns))
            el_departure_date = self._check_element('TimetabledTime', el.find('.//ojp:ServiceDeparture/ojp:TimetabledTime', ns))
            el_destination_name = self._check_element('DestinationText', el.find('.//ojp:DestinationText/ojp:Text', ns))
            el_destination_id = self._check_element('DestinationStopPointRef', el.find('.//ojp:DestinationStopPointRef', ns))

            # Append the data to results
            results.append({
                'id': el_id,
                'label': el_service_name,
                'currentDate': self._format_time(el_current_date, fmt="%Y-%m-%dT%H:%M:%S.%f%z"),
                'departureDate': self._format_time(el_departure_date),
                'estimatedDate': self._convert_estimated_date(el.find('.//ojp:ServiceDeparture/ojp:EstimatedTime', ns)),
                'destinationName': el_destination_name,
                'destinationId': el_destination_id
            })

        return results

    def create_ojp_payload(self, station_id, request_dt_time, number_results=5):
        payload = f"""<?xml version="1.0" encoding="UTF-8"?>
        <OJP xmlns='http://www.vdv.de/ojp' xmlns:siri='http://www.siri.org.uk/siri' version='2.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://www.vdv.de/ojp ../../../../OJP4/OJP.xsd'>
            <OJPRequest>
                <siri:ServiceRequest>
                    <siri:RequestTimestamp>{request_dt_time}</siri:RequestTimestamp>
                    <siri:RequestorRef>swisstopo_Abfahrtsmonitor</siri:RequestorRef>
                    <OJPStopEventRequest>
                        <siri:RequestTimestamp>{request_dt_time}</siri:RequestTimestamp>
                        <siri:MessageIdentifier>SER</siri:MessageIdentifier>
                        <Location>
                            <PlaceRef>
                                <siri:StopPointRef>{station_id}</siri:StopPointRef>
                            </PlaceRef>
                                <DepArrTime>{request_dt_time}</DepArrTime>
                        </Location>
                        <Params>
                            <NumberOfResults>{number_results}</NumberOfResults>
                            <StopEventType>departure</StopEventType>
                            <IncludePreviousCalls>false</IncludePreviousCalls>
                            <IncludeOnwardCalls>true</IncludeOnwardCalls>
                            <IncludeRealtimeData>true</IncludeRealtimeData>
                        </Params>
                    </OJPStopEventRequest>
                </siri:ServiceRequest>
            </OJPRequest>
        </OJP>
    """
        # strip any non needed whitespaces from the payload in order to keep the data traffic to
        # the minimum necessary
        return re.sub(r">\s+<", "><", payload.strip())

    def send_post(self, station_id, request_dt_time, number_results=5):
        headers = {
            'authorization': self.open_trans_api_key,
            'content-type': 'application/xml; charset=utf-8',
            'accept-charset': 'utf-8'
        }
        xml_data = self.create_ojp_payload(str(station_id), str(request_dt_time), str(number_results))
        resp = requests.post(url=self.url, data=xml_data, headers=headers, timeout=5)

        if (resp.status_code == 429):
            raise OpenTransRateLimitException("The rate limit of OpenTransportdata has exceeded")

        if (resp.status_code != requests.codes.ok):
            resp.raise_for_status()

        resp.encoding = 'utf-8'  # TODO better encoding solution
        return resp.text.encode('utf-8')


class OpenTransException(Exception):
    pass


class OpenTransRateLimitException(Exception):
    pass


class OpenTransNoStationException(Exception):
    pass
