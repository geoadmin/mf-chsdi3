FROM python:3.7-buster

ENV SYSTEM_PYTHON_CMD=/usr/local/bin/python3.7
ENV PYPI_URL=https://pypi.org/simple/
ENV PROJ=chsdi
ENV VHOST=mf-${PROJ}3
ENV PROJDIR=/var/www/vhosts/${VHOST}/private/${PROJ}
ENV USER geodata
ENV GROUP geodata

# Setup default logging levels
ENV APACHE_LOG_LEVEL=info PY_ROOT_LOG_LEVEL=INFO PY_CHSDI_LOG_LEVEL=INFO PY_SQLALCHEMY_LOG_LEVEL=WARNING

# REQUIREMENTS NOTE:
#  - gettext-base is required for envsubst in docker-entrypoint.sh
#  - libgeos-dev is required by shapely python package
RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y --upgrade ca-certificates \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y  \
        libgeos-dev \
        gettext-base \
        apache2 libapache2-mod-wsgi-py3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid 2500 ${GROUP} \
    && useradd --uid 2500 --gid ${GROUP} --shell /bin/sh --create-home ${USER} \
    && mkdir -p /var/www/vhosts/${VHOST}/conf \
    && mkdir -p /var/www/vhosts/${VHOST}/private \
    && mkdir -p /var/www/vhosts/${VHOST}/cgi-bin \
    && mkdir -p /var/www/vhosts/${VHOST}/htdocs \
    && mkdir -p /var/www/vhosts/${VHOST}/logs \
    && pip3 install -q --upgrade pip==21.2.4 setuptools --index-url ${PYPI_URL}

# FIXME: use pipenv
COPY requirements-py3.txt .
RUN pip3 install -r requirements-py3.txt --index-url ${PYPI_URL}

COPY --chown=${USER}:${GROUP} 90-chsdi3.conf    /var/www/vhosts/${VHOST}/conf/
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf \
    && a2enconf fqdn \
    && a2enmod \
        auth_basic \
        authz_groupfile \
        autoindex \
        deflate \
        dir \
        env \
        expires \
        filter \
        headers \
        http2 \
        include \
        mpm_event \
        negotiation \
        rewrite \
        setenvif \
        status \
        wsgi \
        alias

COPY --chown=${USER}:${GROUP} . /var/www/vhosts/${VHOST}/private/chsdi
WORKDIR /var/www/vhosts/${VHOST}/private/chsdi

RUN pip3 install -e .

ARG GIT_HASH=unknown
ARG GIT_BRANCH=unknown
ARG GIT_DIRTY=unknown
ARG VERSION=unknown
ARG AUTHOR=unknown

LABEL git.hash=${GIT_HASH}
LABEL git.branch=${GIT_BRANCH}
LABEL git.dirty=${GIT_DIRTY}
LABEL version=${VERSION}
LABEL author=${AUTHOR}

# Substitute the version in the pylons configuration.
ENV APP_VERSION=${VERSION}
RUN sed -i 's/${APP_VERSION}/'${APP_VERSION}'/g' base.ini.in

# NOTE: Here below we cannot use environment variable with ENTRYPOINT using the `exec` form.
# The ENTRYPOINT `exec` form is required in order to use the docker-entrypoint.sh as first
# command to run before the CMD.
ENTRYPOINT ["/var/www/vhosts/mf-chsdi3/private/chsdi/docker-entrypoint.sh"]
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
