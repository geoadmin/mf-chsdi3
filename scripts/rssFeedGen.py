from bs4 import BeautifulSoup
from datetime import datetime
import time
import PyRSS2Gen
import re
import sys
import pytz
from lxml import etree
from lxml.etree import Element, SubElement, QName, tostring


class NoOutput:

    def __init__(self):
        pass

    def publish(self, handler):
        pass

class XMLNamespaces:
    atom = "http://www.w3.org/2005/Atom"


class MyRSS2(PyRSS2Gen.RSSItem):

    def __init__(self, **kwargs):
        PyRSS2Gen.RSSItem.__init__(self, **kwargs)

    def publish(self, handler):
        self.do_not_autooutput_description = self.description
        self.description = NoOutput()
        PyRSS2Gen.RSSItem.publish(self, handler)

    def publish_extensions(self, handler):
        handler._write('<%s><![CDATA[%s]]></%s>' % ('description', self.do_not_autooutput_description, 'description'))


def extract_releases(html):
    with open(html, 'r') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        divRelease = soup.find('div', {'id': 'release-notes'})
        releases = divRelease.findAll('div', {'id': re.compile('release-')})
    return releases


def id_to_rss_date(r):
    id_str = r.findNext('span').get('id')
    date_str = id_str.split('-')[1]
    date_str = date_str + ' 00:00:00'
    date_obj = datetime.strptime(date_str, '%Y%m%d %H:%M:%S')
    localtz = pytz.timezone('Europe/Zurich')
    date_rss = datetime.strftime(localtz.localize(date_obj), '%a, %d %b %Y %H:%M:%S %z')
    return date_rss


def extract_data(r):
    data = r
    for elem in data('h2'):
        elem.extract()
    return data


def data_to_description(data):
    data = data.decode('utf-8', 'ignore')
    description = data.encode('ascii', 'ignore')
    return description

if __name__ == '__main__':
    if len(sys.argv) <2:
        print("Error. You must set API_URL")
        sys.exit(2)

    api_url = sys.argv[1] + '/'
    print("RSS feed url: {}".format(api_url))
    
    items = []
    pathToReleaseNotes = 'chsdi/static/doc/build/releasenotes/index.html'
    try:
        releases = extract_releases(pathToReleaseNotes)
    except IOError as e:
        print('%s does nor exist' % pathToReleaseNotes)
        raise IOError(e)

    i = 0
    for r in releases:
        # parse information from html
        title = r.findNext('h2').text[:-1]
        date_rss = id_to_rss_date(r)
        data = str(extract_data(r))
        description = data_to_description(data)
        # create feeds
        items.append(MyRSS2(
            title=title,
            link= api_url + r.findNext('a').get('href'),
            description=description,
            guid=api_url + r.findNext('a').get('href'),
            pubDate=date_rss))
        i += 1
        if i == 10:
            break

    # create rss
    rss = PyRSS2Gen.RSS2(
        title='GeoAdmin - RSS Feed',
        link=api_url + 'releasenotes/',
        description="The latest news about GeoAdmin application's changes, new and updated data available on map.geo.admin.ch",
        lastBuildDate=time.strftime('%a, %d %b %Y %H:%M:%S %z'),
        items=items
    )

    # Make the feed validate (https://validator.w3.org/feed/check.cgi?)
    rss = rss.to_xml('utf-8')
    root = etree.fromstring(rss)
    new_root = Element('rss', nsmap={'atom':XMLNamespaces.atom})
    new_root.attrib['version'] = '2.0'
    channel = root[0]
    atom_link  = Element(QName(XMLNamespaces.atom, 'link'))
    # Ugly hack to force closing open/close tag style
    atom_link.text=''
    atom_link.attrib['type'] = "application/rss+xml"
    atom_link.attrib['rel'] = "self"
    atom_link.attrib['href'] = api_url + 'releasenotes/rss2.xml'
    link = channel.find("link")
    link.addnext(atom_link)
    new_root.append(channel)

    with open('chsdi/static/doc/build/releasenotes/rss2.xml', 'w') as xml:
        xml.write(etree.tostring(new_root, pretty_print=True))
