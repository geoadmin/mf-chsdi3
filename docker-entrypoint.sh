#!/bin/sh

: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"

# Default KEEPALIVE_TIMEOUT to 5 if not set
export KEEPALIVE_TIMEOUT="${KEEPALIVE_TIMEOUT:-5}"

# Get the LoadModule directive
LOAD_WSGI_MODULE_DIRECTIVE=$("${INSTALL_DIR}/.venv/bin/python" "${INSTALL_DIR}/.venv/bin/mod_wsgi-express" module-config | head -1)
export LOAD_WSGI_MODULE_DIRECTIVE

envsubst < chsdi/config/base.ini.in > base.ini
envsubst < chsdi/config/dev.ini.in > development.ini
envsubst < chsdi/config/prod.ini.in > production.ini

# Write apache configs directly to /etc/apache2 (we own these files now)
envsubst < apache/25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf
envsubst < apache/application.wsgi.in > apache/application.wsgi
envsubst < apache/ports.conf.in > /etc/apache2/ports.conf
envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf

# Set Apache to run as the current user to avoid permission issues
export APACHE_RUN_USER=$(id -un)
export APACHE_RUN_GROUP=$(id -gn)

# Execute the command provided by CMD in Dockerfile
exec "$@"
