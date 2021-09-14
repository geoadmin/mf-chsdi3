FROM python:3.7-buster

ENV USE_PYTHON3=1
ENV SYSTEM_PYTHON_CMD=/usr/local/bin/python3.7
ENV OPENTRANS_API_KEY=dummy-key

ENV PROJ=chsdi
ENV VHOST=mf-${PROJ}3
ENV PROJDIR=/var/www/vhosts/${VHOST}/private/${PROJ}

RUN apt-get update && apt-get install apt-utils \
      ; DEBIAN_FRONTEND=noninteractive apt-get install -y --upgrade ca-certificates \
      ; DEBIAN_FRONTEND=noninteractive apt-get install -y -o Dpkg::Options::="--force-confold" \
      nodejs npm  build-essential git  gettext-base libpq-dev libgeos-dev \
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
COPY 25-mf-chsdi3.conf /etc/apache2/sites-available/000-default.conf
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf && a2enconf fqdn

RUN /usr/sbin/a2enmod auth_basic authz_groupfile autoindex dir env expires filter headers http2 include mpm_event negotiation proxy proxy_http proxy_http2 rewrite setenvif ssl status wsgi alias

COPY . /var/www/vhosts/${VHOST}/private/chsdi
WORKDIR /var/www/vhosts/${VHOST}/private/chsdi
# TODO: potomo & translate
RUN . ./rc_dev && make cleanall build/python setup chsdi/static/css/extended.min.css development.ini production.ini fixrights

ENTRYPOINT ["/var/www/vhosts/mf-chsdi3/private/chsdi/docker-entrypoint.sh"]
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
