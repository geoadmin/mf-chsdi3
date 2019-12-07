#!/bin/bash
set -e

: "${DEPLOY_TARGET:?Variable DEPLOY_TARGET not set or empty}"

INSTALLDIR=$(dirname $(readlink -f "$0"))
export INSTALLDIR


echo "INSTALLDIR=${INSTALLDIR}"

source rc_${DEPLOY_TARGET} && make production.ini development.ini

envsubst < 25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf 

envsubst < apache/application.wsgi.in > apache/application.wsgi

envsubst < apache/ports.conf.in > /etc/apache2/ports.conf

envsubst < apache/wsgi.conf.in > apache/wsgi.conf



# Always put this damn shit
exec "$@"
