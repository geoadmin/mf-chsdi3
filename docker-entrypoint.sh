#!/bin/bash
set -eo pipefail

# mandatory environment variables
: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"
: "${OPENTRANS_API_KEY:?Variable OPENTRANS_API_KEY not set or empty}"


INSTALLDIR=$(dirname $(readlink -f "$0"))
export INSTALLDIR


echo "INSTALLDIR=${INSTALLDIR}"

pg_isready -d stopo_prod -h ${DBHOST} -p ${DBPORT} -U ${PGUSER}

envsubst < base.ini.in > base.ini
# FIXME: name should be local.ini
envsubst < dev.ini.in > development.ini

envsubst < apache/application.wsgi.in > apache/application.wsgi

envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf



# Always put this damn shit
exec "$@"
