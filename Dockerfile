FROM python:3.7-slim-buster AS builder

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y  \
        gcc \
        libgeos-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --user pipenv

ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile.lock Pipfile /usr/src/
WORKDIR /usr/src

# Create virtualenv with all dependencies
RUN /root/.local/bin/pipenv sync

FROM python:3.7-slim-buster AS runtime

ENV VHOST_DIR=/var/www/vhosts/mf-chsdi3
ENV INSTALL_DIR=/var/www/vhosts/mf-chsdi3/private/chsdi
ENV APACHE_ENTRY_PATH=
ENV APACHE_BASE_PATH=main
ENV MODWSGI_USER=www-data

ENV USER geodata
ENV GROUP geodata

# Setup default logging levels
ENV APACHE_LOG_LEVEL=info PY_ROOT_LOG_LEVEL=INFO PY_CHSDI_LOG_LEVEL=INFO PY_SQLALCHEMY_LOG_LEVEL=WARNING

# REQUIREMENTS NOTE:
#  - gettext-base is required for envsubst in docker-entrypoint.sh
RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y --upgrade ca-certificates \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y  \
        gettext-base \
        apache2 \
        libapache2-mod-wsgi-py3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid 2500 ${GROUP} \
    && useradd --uid 2500 --gid ${GROUP} --shell /bin/sh --create-home ${USER} \
    && mkdir -p ${VHOST_DIR}/conf \
    && mkdir -p ${VHOST_DIR}/private \
    && mkdir -p ${VHOST_DIR}/cgi-bin \
    && mkdir -p ${VHOST_DIR}/htdocs \
    && mkdir -p ${VHOST_DIR}/logs \
    &&  echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf \
    && a2enconf fqdn \
    && a2enmod \
        auth_basic \
        authz_groupfile \
        autoindex \
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

# Copy the virtual environment from the builder stage
COPY --from=builder --chown=${USER}:${GROUP} /usr/src/.venv/ ${INSTALL_DIR}/.venv/

# Copy the python chsdi package setup files for package installation down below
COPY --chown=${USER}:${GROUP} \
    setup.cfg \
    setup.py \
    MANIFEST.in \
    README.md \
    LICENSE.md \
    CHANGES.txt \
    docker-entrypoint.sh   ${INSTALL_DIR}/

# Add apache configurations and templates
COPY --chown=${USER}:${GROUP} 90-chsdi3.conf    ${VHOST_DIR}/conf/
COPY --chown=${USER}:${GROUP} apache            ${INSTALL_DIR}/apache/

# Add the application
COPY --chown=${USER}:${GROUP} chsdi             ${INSTALL_DIR}/chsdi/

WORKDIR ${INSTALL_DIR}

ARG GIT_HASH=unknown
ARG GIT_BRANCH=unknown
ARG GIT_DIRTY=unknown
ARG GIT_TAG=unknown
ARG VERSION=unknown
ARG AUTHOR=unknown

LABEL git.hash=${GIT_HASH}
LABEL git.branch=${GIT_BRANCH}
LABEL git.dirty=${GIT_DIRTY}
LABEL git.tag=${GIT_TAG}
LABEL version=${VERSION}
LABEL author=${AUTHOR}

# Substitute the version in the pylons configuration
# and install the chsdi package as editable needed by pyramid
ENV APP_VERSION=${VERSION}
RUN sed -i 's/${APP_VERSION}/'${APP_VERSION}'/g' chsdi/config/base.ini.in \
    && .venv/bin/python -m pip install -e .

# NOTE: Here below we cannot use environment variable with ENTRYPOINT using the `exec` form.
# The ENTRYPOINT `exec` form is required in order to use the docker-entrypoint.sh as first
# command to run before the CMD.
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
