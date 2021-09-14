#!/bin/bash
set -e

: "${DEPLOY_TARGET:?Variable DEPLOY_TARGET not set or empty}"

: "${AWS_DEFAULT_REGION?Variable AWS_DEFAULT_REGION not set or empty}"
: "${GEOADMIN_FILE_STORAGE_BUCKET:?Variable GEOADMIN_FILE_STORAGE_BUCKET not set or empty}"
: "${GEOADMIN_FILE_STORAGE_TABLE_NAME:?Variable GEOADMIN_FILE_STORAGE_TABLE_NAME not set or empty}"
: "${GEOADMIN_FILE_STORAGE_TABLE_REGION:?Variable GEOADMIN_FILE_STORAGE_TABLE_REGION not set or empty}"
: "${GEOADMIN_FILE_STORAGE_BUCKET:?Variable GEOADMIN_FILE_STORAGE_BUCKET not set or empty}"
: "${GLSTYLES_STORAGE_TABLE_NAME:?Variable GLSTYLES_STORAGE_TABLE_NAME not set or empty}"
: "${GLSTYLES_STORAGE_TABLE_REGION:?Variable GLSTYLES_STORAGE_TABLE_REGION not set or empty}"
: "${GEOADMIN_FILE_STORAGE_BUCKET:?Variable GEOADMIN_FILE_STORAGE_BUCKET not set or empty}"
: "${SHORTENER_TABLE_NAME:?Variable SHORTENER_TABLE_NAME not set or empty}"
: "${SHORTENER_TABLE_REGION:?Variable SHORTENER_TABLE_REGION not set or empty}"

: "${APACHE_LOG_LEVEL:?Variable APACHE_LOG_LEVEL not set or empty}"
: "${APACHE_PORT:?Variable APACHE_PORT not set or empty}"
: "${APACHE_BASE_PATH:?Variable APACHE_BASE_PATH not set or empty}"
# Root of apache,
#: "${APACHE_ENTRY_PATH:?Variable APACHE_ENTRY_PATH not set or empty}"
: "${CACHE_CONTROL:?Variable CACHE_CONTROL not set or empty}"
: "${PGPASSWORD:?Variable PGPASSWORD not set or empty}"
: "${PGUSER:?Variable PGUSER not set or empty}"
: "${DBSTAGING:?Variable DBSTAGING not set or empty}"
: "${DBPORT:?Variable DBPORT not set or empty}"
: "${ALTI_URL:?Variable ALTI_URL not set or empty}"
: "${API_URL:?Variable API_URL not set or empty}"
: "${CMSGEOADMINHOST:?Variable CMSGEOADMINHOST not set or empty}"
: "${DATAGEOADMINHOST:?Variable DATAGEOADMINHOST not set or empty}"
: "${DBHOST:?Variable DBHOST not set or empty}"
: "${DYNAMIC_TRANSLATION:?Variable DYNAMIC_TRANSLATION not set or empty}"
: "${GEOADMIN_FILE_STORAGE_BUCKET:?Variable GEOADMIN_FILE_STORAGE_BUCKET not set or empty}"
: "${GEOADMIN_FILE_STORAGE_TABLE_NAME:?Variable GEOADMIN_FILE_STORAGE_TABLE_NAME not set or empty}"
: "${GEOADMIN_FILE_STORAGE_TABLE_REGION:?Variable GEOADMIN_FILE_STORAGE_TABLE_REGION not set or empty}"
: "${GEOADMINHOST:?Variable GEOADMINHOST not set or empty}"
: "${GEODATA_STAGING:?Variable GEODATA_STAGING not set or empty}"
: "${GLSTYLES_STORAGE_TABLE_NAME:?Variable GLSTYLES_STORAGE_TABLE_NAME not set or empty}"
: "${GLSTYLES_STORAGE_TABLE_REGION:?Variable GLSTYLES_STORAGE_TABLE_REGION not set or empty}"
: "${HOST:?Variable HOST not set or empty}"
: "${HTTP_PROXY:?Variable HTTP_PROXY not set or empty}"
: "${KML_TEMP_DIR:?Variable KML_TEMP_DIR not set or empty}"
: "${LINKEDDATAHOST:?Variable LINKEDDATAHOST not set or empty}"
: "${OPENTRANS_API_KEY:?Variable OPENTRANS_API_KEY not set or empty}"
: "${PUBLIC_BUCKET_HOST:?Variable PUBLIC_BUCKET_HOST not set or empty}"
: "${SHOP_URL:?Variable SHOP_URL not set or empty}"
: "${SHORTENER_ALLOWED_DOMAINS:?Variable SHORTENER_ALLOWED_DOMAINS not set or empty}"
: "${SHORTENER_ALLOWED_HOSTS:?Variable SHORTENER_ALLOWED_HOSTS not set or empty}"
: "${SHORTENER_TABLE_NAME:?Variable SHORTENER_TABLE_NAME not set or empty}"
: "${SHORTENER_TABLE_REGION:?Variable SHORTENER_TABLE_REGION not set or empty}"
: "${SPHINXHOST:?Variable SPHINXHOST not set or empty}"
: "${VECTOR_BUCKET:?Variable VECTOR_BUCKET not set or empty}"
: "${WMSHOST:?Variable WMSHOST not set or empty}"
: "${WMTS_PUBLIC_HOST:?Variable WMTS_PUBLIC_HOST not set or empty}"

: "${MODWSGI_USER:?Variable MODWSGI_USER not set or empty}"

: "${WSGI_APP:?Variable WSGI_APP not set or empty}"

INSTALLDIR=$(dirname $(readlink -f "$0"))
export INSTALLDIR


echo "INSTALLDIR=${INSTALLDIR}"
# Variables are listed in prod.env file

make production.ini development.ini

envsubst < 25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf 

envsubst < apache/application.wsgi.in > apache/application.wsgi

envsubst < apache/ports.conf.in > /etc/apache2/ports.conf

envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf



# Always put this damn shit
exec "$@"
