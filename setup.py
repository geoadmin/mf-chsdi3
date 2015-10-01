import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'zc.buildout',
    'webtest',
    'pyramid_mako',
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'psycopg2',
    'SQLAlchemy',
    'geoalchemy2',
    'transaction',
    'pyramid_tm',
    'papyrus',
    'geojson',
    'shapely',
    'Babel',
    'httplib2',
    'nose',
    'coverage',
    'PyYAML',
    'papyrus_ogcproxy>0.1',
    'pep8',
    'autopep8',
    'regex',
    'pystache',
    'lxml',
    'OWSLib',
    'MapProxy==1.8.1a0-20150925',
    'qrcode',
    'sphinx_rtd_theme==0.1.6-ga3',
    'boto',
    'PyPDF2',
    'requests',
    'pyflakes',
    ]

setup(name='chsdi',
      version='0.0.1',
      description='chsdi',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      dependency_links= ['https://github.com/procrastinatio/mapproxy/archive/1.8.1a0-20150925.tar.gz#egg=MapProxy-1.8.1a0-20150925'],
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      package_data = {'chsdi': ['locale/*/LC_MESSAGES/*.mo']},
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="chsdi",
      entry_points="""\
      [paste.app_factory]
      main = chsdi:main
      """,
      )
