# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as et
from pytz import timezone
from datetime import datetime
from dateutil import tz


class OpenTrans:

    def __init__(self, open_trans_api_key):
        self.open_trans_api_key = open_trans_api_key  # Get API key from config .ini
        self.url = 'https://api.opentransportdata.swiss/trias2020'  # URL of API

    def get_departures(self, station_id, number_results=5, request_dt_time=False):
        if not request_dt_time:
            request_dt_time = datetime.now(timezone('Europe/Zurich')).strftime('%Y-%m-%dT%H:%M:%S')
        self.station_id = station_id
        api_response_xml = self.send_post(station_id, request_dt_time, number_results)  # request_dt_time in format 2017-12-11T14:26:18Z
        results = self.xml_to_array(api_response_xml)
        return results

    def _format_time(self, str_date_time):
        from_zone = tz.tzutc()
        to_zone = tz.gettz('Europe/Zurich')
        date_time = datetime.strptime(str_date_time, '%Y-%m-%dT%H:%M:%SZ')
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
        ns = {'trias': 'http://www.vdv.de/trias'}
        root = et.fromstring(xml_data)
        el_stop_events = root.findall('.//trias:StopEvent', ns)
        if not el_stop_events:
            raise OpenTransNoStationException("No data available for the station %s." % str(self.station_id))

        results = []
        for el in el_stop_events:
            el_id = self._check_element('StopPointRef', el.find('./trias:ThisCall/trias:CallAtStop/trias:StopPointRef', ns))
            el_label = self._check_element('PublichedLineName', el.find('./trias:Service/trias:PublishedLineName/trias:Text', ns))
            el_current_date = self._check_element('ResponseTimestamp', root.find('.//{http://www.siri.org.uk/siri}ResponseTimestamp'))
            el_departure_date = self._check_element('TimetabledTime', el.find('./trias:ThisCall/trias:CallAtStop/trias:ServiceDeparture/trias:TimetabledTime', ns))
            el_destination_name = self._check_element('DestinationText', el.find('./trias:Service/trias:DestinationText/trias:Text', ns))
            el_destination_id = self._check_element('DestinationStopPointRef', el.find('./trias:Service/trias:DestinationStopPointRef', ns))

            results.append({
                'id': el_id,
                'label': el_label,
                'currentDate': self._format_time(el_current_date),
                'departureDate': self._format_time(el_departure_date),
                'estimatedDate': self._convert_estimated_date(el.find('./trias:ThisCall/trias:CallAtStop/trias:ServiceDeparture/trias:EstimatedTime', ns)),
                'destinationName': el_destination_name,
                'destinationId': el_destination_id})

        return results

    def send_post(self, station_id, request_dt_time, number_results=5):
        self.headers = {
            'authorization': self.open_trans_api_key,
            'content-type': 'application/xml; charset=utf-8',
            'accept-charset': 'utf-8'
        }
        self.xml_data = u"""
                    <?xml version="1.0" encoding="UTF-8"?>
                    <Trias version="1.1" xmlns="http://www.vdv.de/trias" xmlns:siri="http://www.siri.org.uk/siri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                        <ServiceRequest>
                            <siri:RequestTimestamp>%s</siri:RequestTimestamp>
                            <siri:RequestorRef>EPSa</siri:RequestorRef>
                            <RequestPayload>
                                <StopEventRequest>
                                    <Location>
                                        <LocationRef>
                                            <StopPointRef>%s</StopPointRef>
                                        </LocationRef>
                                        <DepArrTime>%s</DepArrTime>
                                    </Location>
                                    <Params>
                                        <NumberOfResults>%s</NumberOfResults>
                                        <StopEventType>departure</StopEventType>
                                        <IncludePreviousCalls>false</IncludePreviousCalls>
                                        <IncludeOnwardCalls>true</IncludeOnwardCalls>
                                        <IncludeRealtimeData>true</IncludeRealtimeData>
                                    </Params>
                                </StopEventRequest>
                            </RequestPayload>
                        </ServiceRequest>
                    </Trias>
                    """ % (str(request_dt_time), str(station_id), str(request_dt_time), str(number_results))

        self.r = requests.post(self.url, self.xml_data, headers=self.headers, timeout=5)

        if (self.r.status_code == 429):
            raise OpenTransRateLimitException("The rate limit of OpenTransportdata has exceeded")

        if (self.r.status_code != requests.codes.ok):
            self.r.raise_for_status()

        self.r.encoding = 'utf-8'  # TODO better encoding solution
        return self.r.text.encode('utf-8')


class OpenTransException(Exception):
    pass


class OpenTransRateLimitException(Exception):
    pass


class OpenTransNoStationException(Exception):
    pass
