#!/bin/sh

: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"
: "${GUNICORN_TMPFS_DIR:?Variable GUNICORN_TMPFS_DIR not set or empty}"
: "${ROBOTS_FILE:?Variable ROBOTS_FILE not set or empty}"


envsubst < pyramid-config/base.ini.in > base.ini
envsubst < pyramid-config/dev.ini.in > development.ini
envsubst < pyramid-config/prod.ini.in > production.ini

cd chsdi/static/ && ln -sf "${ROBOTS_FILE}" robots.txt && cd - || echo "FAILED TO CREATE ROBOTS LINK"

# Execute the command provided by CMD in Dockerfile
exec "$@"
