# -*- coding: utf-8 -*-

import re
from urlparse import urlparse
import requests
from requests.exceptions import Timeout, ConnectionError

from pyramid.view import view_config

from pyramid.httpexceptions import HTTPBadRequest, HTTPBadGateway, HTTPNotAcceptable, HTTPRequestTimeout
from pyramid.response import Response

from StringIO import StringIO
from urllib import urlopen
from zipfile import ZipFile


allowed_hosts = (
    # list allowed hosts here (no port limiting)
)

DEFAULT_ENCODING = 'utf-8'
DEFAULT_REQUEST_TIMEOUT = 30


class OgcProxy:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='ogcproxy', request_method=['GET', 'POST'])
    def ogcproxy(self):

        url = self.request.params.get("url")
        if url is None:
            return HTTPBadRequest()

        # check for full url
        parsed_url = urlparse(url)
        if not parsed_url.netloc or parsed_url.scheme not in ("http", "https"):
            raise HTTPBadRequest()

        # forward request to target (without Host Header)
        h = dict(self.request.headers)
        h.pop("Host", h)
        try:
            if self.request.method.upper() == 'GET':
                resp = requests.get(url,
                             stream=False,
                             timeout=DEFAULT_REQUEST_TIMEOUT,
                             params=self.request.params,
                             headers=h,
                             verify=False)
            else:
                resp = requests.post(url,
                             stream=False,
                             timeout=DEFAULT_REQUEST_TIMEOUT,
                             params=self.request.params,
                             headers=h,
                             verify=False)
        except Timeout:
            raise HTTPRequestTimeout('Proxied request %s timed out after %s seconds.' % (url, DEFAULT_REQUEST_TIMEOUT))
        except ConnectionError:
            HTTPBadGateway('Bad Gateway for url %s' % url)
        except:  # pragma: no cover
            raise HTTPBadGateway()

        #  All content types are allowed
        headers = dict(resp.headers)
        ct = headers.get('content-type')
        if ct is not None:
            content = resp.content if hasattr(resp, 'content') else None
            if ct == "application/vnd.google-earth.kmz" or \
                    (ct == "application/octet-stream" and headers.get("Content-Location").endswith(".kmz")):
                zipfile = None
                try:
                    zipurl = urlopen(url)
                    zipfile = ZipFile(StringIO(zipurl.read()))
                    content = ''
                    for line in zipfile.open(zipfile.namelist()[0]).readlines():
                        content = content + line
                    ct = 'application/vnd.google-earth.kml+xml'
                except:  # pragma: no cover
                    raise HTTPBadGateway()
                finally:
                    if zipfile:
                        zipurl.close()
        else:  # pragma: no cover
            raise HTTPNotAcceptable()

        if content.find('encoding=') > 0:
            m = re.search("encoding=[\\\"|\"|\'](.*?)[\\\"|\"|\']", content)
            doc_encoding = m.group(1)
            if doc_encoding.lower() != DEFAULT_ENCODING:
                try:
                    data = content.decode(doc_encoding, "replace")
                except Exception:
                    raise HTTPNotAcceptable("Cannot decode requested content from advertized encoding: %s into unicode." % doc_encoding)
                content = data.encode(DEFAULT_ENCODING)
                content = content.replace(doc_encoding, DEFAULT_ENCODING)

        response = Response(content, status=str(resp.status_code),
                            headers={"Content-Type": ct})

        return response
