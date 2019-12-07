#FROM python:3.8-buster
FROM swisstopo/mf-chsdi3:base



ENV USE_PYTHON3=1
ENV SYSTEM_PYTHON_CMD=/usr/local/bin/python3.7
ENV OPENTRANS_API_KEY=dummy-key

ENV PROJ=chsdi
ENV VHOST=mf-${PROJ}3
ENV PROJDIR=/var/www/vhosts/${VHOST}/private/${PROJ}


RUN groupadd --gid 2500 geodata \
    && useradd --uid 2500 --gid geodata --shell /bin/bash --create-home geodata

RUN mkdir -p /var/www/vhosts/${VHOST}/conf && \
    mkdir -p /var/www/vhosts/${VHOST}/private && \
    mkdir -p /var/www/vhosts/${VHOST}/cgi-bin && \
    mkdir -p /var/www/vhosts/${VHOST}/htdocs && \
    mkdir -p /var/www/vhosts/${VHOST}/logs


RUN envsusbt < 25-mf-chsdi3.conf.in > /etc/apache2/sites-available/000-default.conf
COPY 90-chsdi3.conf    /var/www/vhosts/mf-chsdi3/conf/
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf && a2enconf fqdn 

#RUN /usr/sbin/a2ensite 25-${VHOST}
RUN /usr/sbin/a2enmod auth_basic authz_groupfile autoindex dir env expires filter headers http2 include mpm_event negotiation proxy proxy_http proxy_http2 rewrite setenvif ssl status wsgi alias



COPY . /var/www/vhosts/${VHOST}/private/chsdi
# COPY _pgpass /var/www/.pgpass
# RUN chown www-data /var/www/.pgpass && chmod 600  /var/www/.pgpass
# RUN rm -rf /var/www/vhosts/${VHOST}/private/chsdi/.git
WORKDIR /var/www/vhosts/${VHOST}/private/chsdi
RUN rm _pgpass
RUN . ./rc_dev && make cleanall build/python setup chsdi/static/css/extended.min.css production.ini development.ini  potomo lint fixrights doc

#ENTRYPOINT ["/usr/sbin/apache2"]
#CMD ["-D", "FOREGROUND"]
#ENTRYPOINT ["make", "serve"]
ENTRYPOINT ["/var/www/vhosts/mf-chsdi3/private/chsdi/docker-entrypoint.sh"]
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
