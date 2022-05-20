FROM python:3.7-buster

ENV USE_PYTHON3=1
ENV SYSTEM_PYTHON_CMD=/usr/local/bin/python3.7
ENV OPENTRANS_API_KEY=dummy-key

ENV PROJ=chsdi
ENV VHOST=mf-${PROJ}3
ENV PROJDIR=/var/www/vhosts/${VHOST}/private/${PROJ}

RUN apt-get update -qq && apt-get install -qq -y apt-utils \
    ; DEBIAN_FRONTEND=noninteractive apt-get install -qq -y --upgrade ca-certificates \
    ; DEBIAN_FRONTEND=noninteractive apt-get install -qq -y -o Dpkg::Options::="--force-confold" \
    nodejs npm  build-essential git  gettext-base libpq-dev libgeos-dev \
    postgresql-client-common postgresql-client-11 \
    apache2 libapache2-mod-wsgi-py3 \
    gettext gettext-base  \
    curl \
    bash \
    vim \
    lynx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 2500 geodata \
    && useradd --uid 2500 --gid geodata --shell /bin/bash --create-home geodata

RUN mkdir -p /var/www/vhosts/${VHOST}/conf && \
    mkdir -p /var/www/vhosts/${VHOST}/private && \
    mkdir -p /var/www/vhosts/${VHOST}/cgi-bin && \
    mkdir -p /var/www/vhosts/${VHOST}/htdocs && \
    mkdir -p /var/www/vhosts/${VHOST}/logs


COPY 90-chsdi3.conf    /var/www/vhosts/mf-chsdi3/conf/
# Template 25-mf-chsdi3.conf will be replaced at run time into /etc/apache2/sites-available/000-default.conf
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf && a2enconf fqdn

RUN /usr/sbin/a2enmod auth_basic authz_groupfile autoindex dir env expires filter headers http2 include mpm_event negotiation proxy proxy_http proxy_http2 rewrite setenvif status wsgi alias

COPY . /var/www/vhosts/${VHOST}/private/chsdi
WORKDIR /var/www/vhosts/${VHOST}/private/chsdi

ARG GIT_HASH=unknown
ARG GIT_BRANCH=unknown
ARG GIT_DIRTY=unknown
ARG VERSION=unknown
ARG AUTHOR=unknown

LABEL git.hash=$GIT_HASH
LABEL git.branch=$GIT_BRANCH
LABEL git.dirty=$GIT_DIRTY
LABEL version=$VERSION
LABEL author=$AUTHOR

# TODO: potomo & translate
RUN . ./rc_dev && make cleanall setup chsdi/static/css/extended.min.css development.ini production.ini fixrights

ENTRYPOINT ["/var/www/vhosts/mf-chsdi3/private/chsdi/docker-entrypoint.sh"]
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
