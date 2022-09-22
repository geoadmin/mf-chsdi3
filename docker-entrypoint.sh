#!/bin/sh

: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"


envsubst < chsdi/config/base.ini.in > base.ini
envsubst < chsdi/config/dev.ini.in > development.ini
envsubst < chsdi/config/prod.ini.in > production.ini

envsubst < apache/25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf

envsubst < apache/application.wsgi.in > apache/application.wsgi

envsubst < apache/ports.conf.in > /etc/apache2/ports.conf

envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf

cd chsdi/static/ && ln -sf "${ROBOTS_FILE}" robots.txt && cd - || echo "FAILED TO CREATE ROBOTS LINK"

# Execute the command provided by CMD in Dockerfile
exec "$@"
