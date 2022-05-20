#!/bin/bash
set -eo pipefail

: "${DEPLOY_TARGET:?Variable DEPLOY_TARGET not set or empty}"
: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"
: "${RC_FILE_TO_USE:?Variable RC_FILE_TO_USE not set or empty}"


INSTALLDIR=$(dirname $(readlink -f "$0"))
export INSTALLDIR


echo "INSTALLDIR=${INSTALLDIR}"

pg_isready -d stopo_prod -h ${DBHOST} -p ${DBPORT} -U ${PGUSER}

cut -c8- ${RC_FILE_TO_USE} > ${RC_FILE_TO_USE}_no_export
source ${RC_FILE_TO_USE}_no_export && make production.ini development.ini

envsubst < 25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf

envsubst < apache/application.wsgi.in > apache/application.wsgi

envsubst < apache/ports.conf.in > /etc/apache2/ports.conf

envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf



# Always put this damn shit
exec "$@"
