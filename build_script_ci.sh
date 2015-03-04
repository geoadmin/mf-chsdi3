#!/bin/bash
set +x
source /var/lib/jenkins/.pgpassword
set -x
python bootstrap.py --version 1.5.2 --distribute --download-base http://pypi.camptocamp.net/distribute-0.6.22_fix-issue-227/ --setup-source http://pypi.camptocamp.net/distribute-0.6.22_fix-issue-227/distribute_setup.py
# buildout/bin/buildout -c buildout_cleaner.cfg
buildout/bin/buildout -c buildout_ci.cfg
buildout/bin/nosetests -e test_external_links
