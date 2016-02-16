from bs4 import BeautifulSoup
from datetime import datetime
import time
import PyRSS2Gen
import re


class NoOutput:

    def __init__(self):
        pass

    def publish(self, handler):
        pass


class MyRSS2(PyRSS2Gen.RSSItem):

    def __init__(self, **kwargs):
        PyRSS2Gen.RSSItem.__init__(self, **kwargs)

    def publish(self, handler):
        self.do_not_autooutput_description = self.description
        self.description = NoOutput()
        PyRSS2Gen.RSSItem.publish(self, handler)

    def publish_extensions(self, handler):
        handler._out.write('<%s><![CDATA[%s]]></%s>' % ('description', self.do_not_autooutput_description, 'description'))


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
    date_rss = datetime.strftime(date_obj, '%a, %d %b %Y %H:%M:%S %z')
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
    items = []
    pathToReleaseNotes = 'chsdi/static/doc/build/releasenotes/index.html'
    try:
        releases = extract_releases(pathToReleaseNotes)
    except IOError as e:
        print '%s does nor exist' % pathToReleaseNotes

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
            link='//api3.geo.admin.ch/releasenotes/' + r.findNext('a').get('href'),
            description=description,
            guid='//api3.geo.admin.ch/releasenotes/' + r.findNext('a').get('href'),
            pubDate=date_rss))
        i += 1
        if i == 10:
            break

    # create rss
    rss = PyRSS2Gen.RSS2(
        title='GeoAdmin - RSS Feed',
        link='//api3.geo.admin.ch/releasenotes/',
        description="The latest news about GeoAdmin application's changes, new and updated data available on map.geo.admin.ch",
        lastBuildDate=time.strftime('%a, %d %b %Y %H:%M:%S %z'),
        items=items
    )

    # write into xml file
    rss = rss.to_xml('utf-8')
    with open('chsdi/static/doc/build/releasenotes/rss2.xml', 'w') as xml:
        xml.write(rss)
