#!/bin/bash
set -eo pipefail

: "${DEPLOY_TARGET:?Variable DEPLOY_TARGET not set or empty}"
: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"

: "${DEPLOY_TARGET:?Variable DEPLOY_TARGET not set or empty}"

INSTALLDIR=$(dirname $(readlink -f "$0"))
CURRENT_DIRECTORY=${INSTALLDIR}
export INSTALLDIR 
export CURRENT_DIRECTORY


echo "INSTALLDIR=${INSTALLDIR}"

pg_isready -d stopo_prod -h ${DBHOST} -p ${DBPORT} -U ${PGUSER}

source rc_${DEPLOY_TARGET} && make production.ini development.ini

envsubst < 25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf 

envsubst < apache/application.wsgi.in > apache/application.wsgi

envsubst < apache/ports.conf.in > /etc/apache2/ports.conf

envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf


# Always put this damn shit
exec "$@"
