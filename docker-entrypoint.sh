#!/bin/sh

: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"

echo "INSTALLDIR=${INSTALLDIR}"

envsubst < base.ini.in > base.ini
envsubst < dev.ini.in > development.ini
envsubst < prod.ini.in > production.ini

envsubst < 25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf

envsubst < apache/application.wsgi.in > apache/application.wsgi

envsubst < apache/ports.conf.in > /etc/apache2/ports.conf

envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf

# Execute the command provided by CMD in Dockerfile
exec "$@"
