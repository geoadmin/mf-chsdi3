#
# This Makefile is to be used only in new environement (docker, python3 and
# AWS Region Frankfurt (eu-central-1)
# Please, keep it lean, compact and understandable
#
# Currently, the .venv is used inside the docker image, to run
# the application and locally, for development, linting, generating
# files from template, building doc, etc. Python 3.7 is used.

SHELL = /bin/bash
.DEFAULT_GOAL := help

SERVICE_NAME := mf-chsdi3

CURRENT_DIRECTORY := $(shell pwd)
VENV := .venv

# default configuration
ENV_FILE ?= .env.default
include $(ENV_FILE)
S3_TESTS ?= 1

# Note the `fi`is a hack for `rm`(which didn't exist for a long time!)
# https://github.com/geoadmin/mf-chsdi3/blob/966b5471dfad9f9c77ca44a089b81419c4a6311b/chsdi/lib/helpers.py#L140-L142
AVAILABLE_LANGUAGES := de fr it fi en
LANGUAGES_PO_FILES := $(patsubst %,chsdi/locale/%/LC_MESSAGES/chsdi.po, $(AVAILABLE_LANGUAGES))
LANGUAGES_MO_FILES := $(patsubst %,chsdi/locale/%/LC_MESSAGES/chsdi.mo, $(AVAILABLE_LANGUAGES))
TRANSLATION_POT_FILE := chsdi/locale/chsdi.pot
TRANSLATION_DIRS := $(patsubst %,chsdi/locale/%, $(AVAILABLE_LANGUAGES))
TRANSLATION_FILES := $(TRANSLATION_POT_FILE) $(LANGUAGES_PO_FILES) $(LANGUAGES_MO_FILES)
DOC_BUILD := chsdi/static/doc/build

# Create legends
WMSSCALELEGEND ?=
NODE_MODULES := node_modules

ifeq ($(CI_QUIET), 1)
PIP_QUIET := -q
NPM_QUIET := --silent
else
PIP_QUIET :=
NPM_QUIET :=
endif


# Commands
AUTOPEP8 := $(VENV)/bin/autopep8
FLAKE8 := $(VENV)/bin/flake8
MAKO := $(VENV)/bin/mako-render
NOSE := $(VENV)/bin/nosetests
PIP := $(VENV)/bin/pip3 $(PIP_QUIET)
PSERVE := $(VENV)/bin/pserve
PSHELL := $(VENV)/bin/pshell
PYTHON := $(VENV)/bin/python3
SPHINX := $(VENV)/bin/sphinx-build
ENVSUBST := /usr/bin/envsubst

PYTHON_VERSION := 3.7
SYSTEM_PYTHON_CMD ?= python${PYTHON_VERSION}
PYTHONPATH ?= $(VENV)/lib/python${PYTHON_VERSION}/site-packages:/usr/lib64/python${PYTHON_VERSION}/site-packages


PYPI_URL ?= https://pypi.org/simple/


# AWS and docker variables
DOCKER_REGISTRY = 974517877189.dkr.ecr.eu-central-1.amazonaws.com
AWS_REGION_ECR := eu-central-1
AUTHOR=$(USER)

# data.geo.admin.ch hosts
DATAGEOADMINHOST ?= data.geo.admin.ch

# Git metadata
GIT_HASH ?= $(shell git rev-parse HEAD)
GIT_HASH_SHORT ?= $(shell git rev-parse --short HEAD)
GIT_BRANCH ?= $(shell git symbolic-ref HEAD --short 2>/dev/null)
GIT_DIRTY ?= $(shell git status --porcelain)
GIT_TAG ?= $(shell git describe --tags --dirty || echo "no version info")
GIT_COMMIT_DATE ?= $(shell git log -1  --date=iso --pretty=format:%cd)
DOCKER_IMAGE_TAG ?= local-$(USER)-$(GIT_HASH_SHORT)
DOCKER_IMG_LOCAL_TAG_PATH = $(DOCKER_REGISTRY)/$(SERVICE_NAME):$(DOCKER_IMAGE_TAG)
APP_VERSION=$(GIT_TAG)

# Colors
ifneq ($(shell echo ${TERM}),)
RESET := $(shell tput sgr0)
RED := $(shell tput setaf 1)
GREEN := $(shell tput setaf 2)
endif

# Date
CURRENT_DATE ?= $(shell date -u +"%Y-%m-%d %H:%M:%S %z")

# Python files (for linting)
PYTHON_FILES := $(shell find chsdi/* tests/* -path chsdi/static -prune -o -path chsdi/lib/sphinxapi -prune -o -path tests/e2e -prune -o -type f -name "*.py" -print)

# Linting rules
PEP8_IGNORE := "E128,E221,E241,E251,E272,E305,E501,E711,E731,W503,W504,W605"

# E128: continuation line under-indented for visual indent
# E221: multiple spaces before operator
# E241: multiple spaces after ':'
# E251: multiple spaces around keyword/parameter equals
# E272: multiple spaces before keyword
# E501: line length 79 per default
# E711: comparison to None should be 'if cond is None:' (SQLAlchemy's filter syntax requires this ignore!)
# E731: do not assign a lambda expression, use a def
# TODO: break before or after, but decide
# W503: line break before binary operator
# W504: line break afterbinary operator
# W605 invalid escape sequence

.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Possible targets:"
	@echo
	@echo -e "\033[1mSetup TARGETS\033[0m "
	@echo "- setup              Create the python virtual environment with developper tools"
	@echo "- all                Build the application with all dependent files. Ready to serve"
	@echo
	@echo -e "\033[1mBuild TARGETS\033[0m "
	@echo "- build              Build the application files."
	@echo
	@echo -e "\033[1mFORMATING, LINTING AND TESTING TOOLS TARGETS\033[0m "
	@echo "- lint/autolint      Python code quality assurance"
	@echo "- shell              Pylons shell (for debugging)"
	@echo "- test               Functional and integration nose tests"
	@echo "- unittest-ci        Same as 'test' but with specific junit output for the CI"
	@echo "- teste2e            End-to-end tests"
	@echo
	@echo -e "\033[1mLOCAL SERVER TARGETS\033[0m "
	@echo "- config-templates   Create the pylons settings file from templates and environment variables."
	@echo "- serve              Run the wsgi app using the waitress debug server. Port can be set by Env variable SERVER_PORT (default: 6543)"
	@echo
	@echo -e "\033[1mWEBSITE AND DOCUMENTATION\033[0m "
	@echo "- doc                Create the website and static files"
	@echo "- rss                Create RSS feed from the releasenotes html file"
	@echo
	@echo -e "\033[1mDATA INTEGRATION\033[0m "
	@echo "- legends           Download from the WMS server the legend images for a given layer"
	@echo
	@echo -e "\033[1mDocker TARGETS\033[0m "
	@echo "- dockerlogin        Login to the AWS ECR registery for pulling/pushing docker images"
	@echo "- dockerbuild        Build the project localy (with tag := $(DOCKER_IMAGE_TAG))"
	@echo "- dockerrun          Run the project within docker localy (with tag := $(DOCKER_IMAGE_TAG)) on port $(APACHE_PORT)"
	@echo "- dockerrun-shell    Run the project within docker localy (with tag := $(DOCKER_IMAGE_TAG)) on port $(APACHE_PORT)"
	@echo "- dockerpush         Build and push the project localy (with tag := $(DOCKER_IMAGE_TAG))"
	@echo "- dockerpull         Pull the docker image with tag $(DOCKER_IMAGE_TAG))"
	@echo
	@echo -e "\033[1mCLEANING TARGETS\033[0m "
	@echo "- clean              Remove generated files"
	@echo "- cleanall           Remove all the build artefacts and venv"
	@echo
	@echo "Variables:"
	@echo "PYTHON_VERSION:      ${PYTHON_VERSION}"
	@echo "SYSTEM_PYTHON_CMD:   ${SYSTEM_PYTHON_CMD}"
	@echo "DBHOST:              ${DBHOST}"
	@echo "DBPORT:              ${DBPORT}"
	@echo "SERVER_PORT:         ${SERVER_PORT}"
	@echo "APACHE_PORT:         ${APACHE_PORT}"
	@echo "OPENTRANS_API_KEY:   ${OPENTRANS_API_KEY}"
	@echo "S3_TESTS:            ${S3_TESTS}"
	@echo "DOCKER_REGISTRY      ${DOCKER_REGISTRY}"
	@echo "DOCKER_IMAGE_TAG     ${DOCKER_IMAGE_TAG}"
	@echo


# TODO: add targets `translate` when merged
.PHONY: all
all: setup config-templates lint build


.PHONY: setup
setup: $(VENV) $(NODE_MODULES)


requirements-py3.txt:
	@echo "${GREEN}requirements-py3.txt has changed...${RESET}";


# TODO: replace through pipenv as in the other projects.
$(VENV): requirements-py3.txt
		test -d "$(VENV)" ||  ( $(SYSTEM_PYTHON_CMD) -m venv $(VENV) && \
		${PIP} install $(PIP_QUIET) --upgrade pip==21.2.4 setuptools --index-url ${PYPI_URL}  && \
		${PIP} install $(PIP_QUIET) -r requirements-py3.txt --index-url ${PYPI_URL}  -e . )


.PHONY: build
build: doc translate chsdi/static/css/extended.min.css rss set-app_version

.PHONY: set-app_version
set-app_version:
	export APP_VERSION="$(APP_VERSION)" && \
	export GIT_BRANCH="$(GIT_BRANCH)" && \
	export GIT_HASH_SHORT="$(GIT_HASH_SHORT)" && \
	export GIT_COMMIT_DATE="$(GIT_COMMIT_DATE)" && \
	export GIT_HASH="$(GIT_HASH)" && \
	export GIT_DIRTY="$(GIT_DIRTY)" && \
	export PYTHON_VERSION="$(PYTHON_VERSION)" && \
	export CURRENT_DATE="$(CURRENT_DATE)" && \
	envsubst < chsdi/static/info.json.in > chsdi/static/info.json


.PHONY: config-templates
config-templates: guard-OPENTRANS_API_KEY guard-PGUSER guard-PGPASSWORD set-app_version
# FIXME: nosetests is still using development.ini
	export $(shell cat $(ENV_FILE)) && \
	export CURRENT_DIRECTORY=${CURRENT_DIRECTORY} && \
	export APP_VERSION="$(APP_VERSION)" && \
	export DATAGEOADMINHOST="$(DATAGEOADMINHOST)" && \
	envsubst < base.ini.in > base.ini && \
	envsubst < dev.ini.in > development.ini && \
	envsubst < prod.ini.in > production.ini && \
	envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf && \
	envsubst < apache/application.wsgi.in > apache/application.wsgi && \
	envsubst < 25-mf-chsdi3.conf.in > 25-mf-chsdi3.conf


# Generate a basically empty gettext `chsdi` domain.
# Translation are dynamic, the domain is updated at runtime directly from the BOD
.PHONY: translate
translate: $(VENV) $(TRANSLATION_FILES)


# FIXME add the rss and css compilation
.PHONY: doc
doc: $(VENV) $(DOC_BUILD)


.PHONY:
rss: $(VENV) doc chsdi/static/doc/build/releasenotes/index.html
	@echo "${GREEN}Creating the rss feed from releasenotes${RESET}";
	${PYTHON} scripts/rssFeedGen.py "https://api3.geo.admin.ch"


.PHONY: legends
legends: $(VENV) guard-BODID guard-WMSHOST
	scripts/downloadlegends.sh $(WMSHOST) $(BODID) $(WMSSCALELEGEND)


.PHONY: serve
serve: $(VENV) config-templates set-app_version
	PYTHONPATH=${PYTHONPATH} ${PSERVE} development.ini --reload


.PHONY: shell
shell: $(VENV) config-templates set-app_version
	PYTHONPATH=${PYTHONPATH} ${PSHELL} development.ini


.PHONY: dockerlogin
dockerlogin:
	aws --profile swisstopo-bgdi-builder ecr get-login-password --region $(AWS_REGION_ECR) | docker login --username AWS --password-stdin $(DOCKER_REGISTRY)


.PHONY: dockerbuild
dockerbuild: build
	docker build \
		--build-arg GIT_HASH="$(GIT_COMMIT_HASH)" \
		--build-arg GIT_BRANCH="$(GIT_BRANCH)" \
		--build-arg GIT_DIRTY="$(GIT_DIRTY)" \
		--build-arg VERSION="$(GIT_TAG)" \
		--build-arg AUTHOR="$(AUTHOR)" -t $(DOCKER_IMG_LOCAL_TAG_PATH) -f Dockerfile .


.PHONY: dockerrun
dockerrun: guard-OPENTRANS_API_KEY guard-PGUSER guard-PGPASSWORD
	docker run \
	    -it \
	    --network=host \
	    --env-file=${ENV_FILE} \
	    --env PGUSER=${PGUSER} --env PGPASSWORD=${PGPASSWORD} \
		--env OPENTRANS_API_KEY=${OPENTRANS_API_KEY} \
		$(DOCKER_IMG_LOCAL_TAG_PATH)


.PHONY: dockerrun-shell
dockerrun-shell: guard-OPENTRANS_API_KEY guard-PGUSER guard-PGPASSWORD
	docker run \
	    -it \
	    --network=host \
	    --env-file=${ENV_FILE} \
	    --env PGUSER=${PGUSER} --env PGPASSWORD=${PGPASSWORD} \
		--env OPENTRANS_API_KEY=${OPENTRANS_API_KEY} \
		--entrypoint /bin/sh \
		$(DOCKER_IMG_LOCAL_TAG_PATH)


.PHONY: dockerpush
dockerpush:
	docker push $(DOCKER_IMG_LOCAL_TAG_PATH)


.PHONY: dockerpull
dockerpull:
	docker pull $(DOCKER_IMG_LOCAL_TAG_PATH)


.PHONY: test
test: $(VENV) config-templates $(TRANSLATION_FILES) $(DOC_BUILD)
	export $(shell cat $(ENV_FILE)) && ${PYTHON} ./scripts/pg_ready.py
	PYTHONPATH=${PYTHONPATH} S3_TESTS=$(S3_TESTS) ${NOSE} --verbosity=2 --cover-erase  tests/ -e .*e2e.*


.PHONY: unittest-ci
unittest-ci: $(VENV) config-templates $(TRANSLATION_FILES) $(DOC_BUILD)
	mkdir -p junit-reports/{integration,functional}
	PYTHONPATH=${PYTHONPATH} ${NOSE} --verbosity=2 \
		--with-xunit --xunit-file=junit-reports/functional/nosetest.xml \
		tests/functional
	PYTHONPATH=${PYTHONPATH} S3_TESTS=$(S3_TESTS) ${NOSE} --verbosity=2 \
		--with-xunit --xunit-file=junit-reports/integration/nosetest.xml \
		tests/integration


.PHONY: teste2e
teste2e: $(VENV)
	PYTHONPATH=${PYTHONPATH} ${NOSE} tests/e2e/

# TODO: Replace through yapf, once the old vhost infra is replaced
.PHONY: lint
lint: $(VENV)
	@echo "${GREEN}Linting python files...${RESET}";
	${FLAKE8} --ignore=${PEP8_IGNORE} $(PYTHON_FILES) && echo ${RED}


# TODO: Replace through yapf, once the old vhost infra is replaced
.PHONY: autolint
autolint: $(VENV)
	@echo "${GREEN}Auto correction of python files...${RESET}";
	${AUTOPEP8} --in-place --aggressive --aggressive --verbose --ignore=${PEP8_IGNORE} $(PYTHON_FILES)


# Compiling targets

$(NODE_MODULES): package.json
	@echo "${GREEN}Installing node packages...${RESET}";
	npm install $(NPM_QUIET) --production
	mkdir -p chsdi/static/js/
	cp -f $(NODE_MODULES)/jquery/dist/jquery.min.js chsdi/static/js/jquery.min.js
	cp -f $(NODE_MODULES)/blueimp-gallery/js/blueimp-gallery.min.js chsdi/static/js/blueimp-gallery.min.js
	cp -f $(NODE_MODULES)/d3/d3.min.js chsdi/static/js/d3.min.js
	cp -f $(NODE_MODULES)/d3-tip/index.js chsdi/static/js/d3-tip.js
	cp -f $(NODE_MODULES)/blueimp-gallery/css/blueimp-gallery.min.css chsdi/static/css/blueimp-gallery.min.css

chsdi/static/css/extended.min.css: chsdi/static/less/extended.less
	@echo "${GREEN}Generating new css file...${RESET}";
	$(NODE_MODULES)/.bin/lessc -ru --clean-css $< $@

# Translation POT file depends on all files from chsdi sources except the translation files generated
# and the python compiled and cache files
TRANSLATION_POT_FILE_DEPENDENCIES := $(shell find chsdi -name *.py)
$(TRANSLATION_POT_FILE): $(TRANSLATION_POT_FILE_DEPENDENCIES)
	@echo "${GREEN}Extracting the translation...${RESET}";
	${PYTHON} setup.py extract_messages


$(LANGUAGES_PO_FILES): $(TRANSLATION_POT_FILE)
	@echo "${GREEN}Building the translation PO $@ file...${RESET}";
	${PYTHON} setup.py init_catalog -l $(patsubst chsdi/locale/%/LC_MESSAGES/chsdi.po,%, $@)


$(LANGUAGES_MO_FILES): $(LANGUAGES_PO_FILES)
	@echo "${GREEN}Building the translation MO $@ file...${RESET}";
	${PYTHON} setup.py compile_catalog -l $(patsubst chsdi/locale/%/LC_MESSAGES/chsdi.mo,%, $@)


DOC_FILES_DEPENDENCIES := $(shell find chsdi/static/doc/source ! -name *.pyc ! -name __pycache__)
$(DOC_BUILD): $(DOC_FILES_DEPENDENCIES)
	@echo "${GREEN}Building the documentation...${RESET}";
	cd chsdi/static/doc && ../../../${SPHINX} -W -b html source build || exit 1 ;


guard-%:
	@ if test "${${*}}" = ""; then \
	  echo "Environment variable $* not set. Add it to your command."; \
	  exit 1; \
	fi

# Clean targets

.PHONY: clean
clean:
	rm -f base.ini
	rm -f production.ini
	rm -f development.ini
	rm -f 25-mf-chsdi3.conf
	rm -f apache/application.wsgi
	rm -f apache/wsgi.conf
	rm -f chsdi/static/info.json
	rm -rf $(DOC_BUILD)
	rm -f  chsdi/static/css/blueimp-gallery.min.css
	rm -f  chsdi/static/css/extended.min.css
	rm -rf $(TRANSLATION_DIRS)
	find chsdi/static/js -type f ! -name .gitignore -exec rm -f \;
	rm -f .coverage .coverage.*
	find chsdi -name "__pycache__" -exec rm -rf "{}" \;


PHONY: cleanall
cleanall: clean
	rm -rf chsdi.egg-info/
	rm -rf $(VENV)
	rm -rf node_modules
	rm -f  package-lock.json

