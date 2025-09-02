import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name='chsdi',
      version='3.2.0',
      description='Macro-services for the Swiss Federal Geoportal https://map.geo.admin.ch',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='https://github.com/geoadmin/mf-chsdi3',
      keywords='web pyramid pylons',
      packages=find_packages(),
      package_data = {'chsdi': ['locale/*/LC_MESSAGES/*.mo']},
      include_package_data=True,
      zip_safe=False,
      python_requires='>2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
      entry_points="""\
      [paste.app_factory]
      main = chsdi:main
      """,
      )
