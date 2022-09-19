FROM python:3.7-slim-buster

ENV USER geodata
ENV GROUP geodata


# REQUIREMENTS NOTE:
#  - gettext-base is required for envsubst in docker-entrypoint.sh
#  - libgeos-dev is required by shapely python package
#  - gcc is required by pyproj
RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y --upgrade ca-certificates \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y  \
        gcc \
        libgeos-dev \
        gettext-base \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install pipenv \
    && groupadd --gid 2500 ${GROUP} \
    && useradd --uid 2500 --gid ${GROUP} --shell /bin/sh --create-home ${USER}

COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY --chown=${USER}:${GROUP} . /mf-chsdi3/
WORKDIR /mf-chsdi3


RUN pip3 install -e .

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

# Substitute the version in the pylons configuration.
ENV APP_VERSION=${VERSION}
RUN sed -i 's/${APP_VERSION}/'${APP_VERSION}'/g' pyramid-config/base.ini.in

# NOTE: Here below we cannot use environment variable with ENTRYPOINT using the `exec` form.
# The ENTRYPOINT `exec` form is required in order to use the docker-entrypoint.sh as first
# command to run before the CMD.
ENTRYPOINT ["/mf-chsdi3/docker-entrypoint.sh"]
CMD ["python", "gunicorn_wsgi.py", "--paste", "production.ini"]
