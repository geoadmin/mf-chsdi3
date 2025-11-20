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
PROJECT_PATH := $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))


# default configuration
ENV_FILE ?= .env.mine
ifneq ("$(wildcard $(ENV_FILE))","")
	# Export all environment variables if the ENV_FILE exists
	include $(ENV_FILE)
	export $(shell sed 's/=.*//' $(ENV_FILE))
endif

PROCESS ?= 0

# Note the `fi`is a hack for `rm`(which didn't exist for a long time!)
# https://github.com/geoadmin/mf-chsdi3/blob/966b5471dfad9f9c77ca44a089b81419c4a6311b/chsdi/lib/helpers.py#L140-L142
AVAILABLE_LANGUAGES := de fr it fi en
LANGUAGES_PO_FILES := $(patsubst %,chsdi/locale/%/LC_MESSAGES/chsdi.po, $(AVAILABLE_LANGUAGES))
LANGUAGES_MO_FILES := $(patsubst %,chsdi/locale/%/LC_MESSAGES/chsdi.mo, $(AVAILABLE_LANGUAGES))
TRANSLATION_POT_FILE := chsdi/locale/chsdi.pot
TRANSLATION_DIRS := $(patsubst %,chsdi/locale/%, $(AVAILABLE_LANGUAGES))
TRANSLATION_FILES := $(TRANSLATION_POT_FILE) $(LANGUAGES_PO_FILES) $(LANGUAGES_MO_FILES)

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

VENV = $(shell pipenv --venv 2> /dev/null || echo "NO_VIRTUAL_ENVIRONEMENT")

# Commands
PIPENV_RUN := pipenv run
ENVSUBST := /usr/bin/envsubst

# Venv commands : these are evaluated at runtime, not at declaration
AUTOPEP8 = $(VENV)/bin/autopep8
FLAKE8 = $(VENV)/bin/flake8
MAKO = $(VENV)/bin/mako-render
NOSE = $(VENV)/bin/nose2
PIP = $(VENV)/bin/pip3 $(PIP_QUIET)
PSERVE = $(VENV)/bin/pserve
PSHELL = $(VENV)/bin/pshell
PYTHON = $(VENV)/bin/python3
PYLINT = $(VENV)/bin/pylint

PYTHON_VERSION := $(shell $$(pipenv --py 2> /dev/null) --version 2>&1 | awk '{print $$2}')

# AWS and docker variables
DOCKER_REGISTRY = 974517877189.dkr.ecr.eu-central-1.amazonaws.com
AWS_REGION_ECR := eu-central-1
AUTHOR=$(USER)

# Git metadata
GIT_HASH ?= $(shell git rev-parse HEAD)
GIT_HASH_SHORT ?= $(shell git rev-parse --short HEAD)
GIT_BRANCH ?= $(shell git symbolic-ref HEAD --short 2>/dev/null)
GIT_DIRTY ?= $(shell git status --porcelain)
GIT_TAG ?= $(shell git describe --tags --dirty || echo "no version info")
GIT_COMMIT_DATE ?= $(shell git log -1  --date=iso --pretty=format:%cd)
DOCKER_IMAGE_TAG ?= local-$(USER)-$(GIT_HASH_SHORT)
DOCKER_IMG_LOCAL_TAG_PATH = $(DOCKER_REGISTRY)/$(SERVICE_NAME):$(DOCKER_IMAGE_TAG)

# Colors
ifneq ($(shell echo ${TERM}),)
RESET := $(shell tput sgr0)
RED := $(shell tput setaf 1)
GREEN := $(shell tput setaf 2)
endif

# Date
CURRENT_DATE ?= $(shell date -u +"%Y-%m-%d %H:%M:%S %z")

# Python files (for linting)
PYTHON_FILES := $(shell find chsdi/* tests/* -path chsdi/static -prune -o -path tests/e2e -prune -o -type f -name "*.py" -print)

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
	@echo "- ci                 Create the python virtual environment with developper tools for the CI"
	@echo "                     without package updates (based on the Pipfile.lock)."
	@echo "- all                Build the application with all dependent files. Ready to serve"
	@echo
	@echo -e "\033[1mBuild TARGETS\033[0m "
	@echo "- build              Build the application files."
	@echo
	@echo -e "\033[1mFORMATING, LINTING AND TESTING TOOLS TARGETS\033[0m "
	@echo "- lint/autolint      Python code quality assurance"
	@echo "- shell              Pylons shell (for debugging)"
	@echo "- test-functional    Functional nose2 tests"
	@echo "- test-integration   Integration nose2 tests"
	@echo "- test   			Functional and integration nose2 tests"
	@echo "- unittest-ci        Same as 'test' but with specific junit output for the CI"
	@echo "- teste2e            End-to-end tests"
	@echo
	@echo -e "\033[1mLOCAL SERVER TARGETS\033[0m "
	@echo "- local-templates    Create the pylons settings file from templates and environment variables for local development."
	@echo "- serve              Run the wsgi app using the waitress debug server. Port can be set by Env variable HTTP_PORT (default: 6543)"
	@echo
	@echo -e "\033[1mDATA INTEGRATION\033[0m "
	@echo "- legends           Download from the WMS server the legend images for a given layer BODID= WMSHOST=localhost:9X78 WMSSCALELEGEND=50000"
	@echo
	@echo -e "\033[1mDocker TARGETS\033[0m "
	@echo "- dockerlogin        Login to the AWS ECR registery for pulling/pushing docker images"
	@echo "- dockerbuild        Build the project locally (with tag := $(DOCKER_IMAGE_TAG))"
	@echo "- dockerrun          Run the project within docker locally (with tag := $(DOCKER_IMAGE_TAG)) on port $(HTTP_PORT)"
	@echo "- dockerrun-shell    Open a shell locally in docker"
	@echo "- dockerpush         Build and push the project locally (with tag := $(DOCKER_IMAGE_TAG))"
	@echo "- dockerpull         Pull the docker image with tag $(DOCKER_IMAGE_TAG))"
	@echo
	@echo -e "\033[1mCLEANING TARGETS\033[0m "
	@echo "- clean              Remove generated files"
	@echo "- cleanall           Remove all the build artefacts"
	@echo
	@echo "Variables:"
	@echo "PYTHON_VERSION:      ${PYTHON_VERSION}"
	@echo "VENV:                ${VENV}"
	@echo "DBHOST:              ${DBHOST}"
	@echo "DBPORT:              ${DBPORT}"
	@echo "HTTP_PORT:           ${HTTP_PORT}"
	@echo "OPENTRANS_API_KEY:   ${OPENTRANS_API_KEY}"
	@echo "S3_TESTS:            ${S3_TESTS}"
	@echo "DOCKER_REGISTRY      ${DOCKER_REGISTRY}"
	@echo "DOCKER_IMAGE_TAG     ${DOCKER_IMAGE_TAG}"
	@echo


.PHONY: all
all: setup lint build


.PHONY: setup
setup: $(NODE_MODULES)
	@echo "${GREEN}Setup...${RESET}";
	pipenv install --dev
	# Here it is important NOT to use pipenv otherwise the editable package is added to Pipfile
	pipenv run pip install -e .
	if [ ! -e .env.mine ]; then cp .env.default .env.mine; fi


.PHONY: ci
ci: $(NODE_MODULES)
	@echo "${GREEN}CI setup...${RESET}";
	# Create virtual env with all packages for development using the Pipfile.lock
	pipenv sync --dev
	# Here it is important NOT to use pipenv otherwise the editable package is added to Pipfile
	pipenv run pip install -e .


.PHONY: build
build: guard-VENV node-module-files translate chsdi/static/css/extended.min.css set-app_version


.PHONY: set-app_version
set-app_version:
	@echo "${GREEN}Setting app version...${RESET}";
	export APP_VERSION="$(APP_VERSION)" && \
	export GIT_BRANCH="$(GIT_BRANCH)" && \
	export GIT_HASH_SHORT="$(GIT_HASH_SHORT)" && \
	export GIT_COMMIT_DATE="$(GIT_COMMIT_DATE)" && \
	export GIT_HASH="$(GIT_HASH)" && \
	export GIT_DIRTY="$(GIT_DIRTY)" && \
	export GIT_TAG="$(GIT_TAG)" && \
	export PYTHON_VERSION="$(PYTHON_VERSION)" && \
	export CURRENT_DATE="$(CURRENT_DATE)" && \
	envsubst < chsdi/static/info.json.in > chsdi/static/info.json


.PHONY: local-templates
local-templates: guard-OPENTRANS_API_KEY guard-PGUSER guard-PGPASSWORD set-app_version $(LOGS_DIR)
	@echo "${GREEN}Setting local development configuration templates...${RESET}";
	export $(shell cat $(ENV_FILE)) && \
	export CURRENT_DIRECTORY=${CURRENT_DIRECTORY} && \
	export APP_VERSION="$(APP_VERSION)" && \
	envsubst < chsdi/config/base.ini.in > base.ini && \
	envsubst < chsdi/config/dev.ini.in > development.ini && \
	envsubst < chsdi/config/prod.ini.in > production.ini && \
	cd chsdi/static && ln -sf "${ROBOTS_FILE}" robots.txt && cd -


# Generate a basically empty gettext `chsdi` domain.
# Translation are dynamic, the domain is updated at runtime directly from the BOD
.PHONY: translate
translate: guard-VENV $(TRANSLATION_FILES)


.PHONY: legends
legends: guard-VENV guard-BODID guard-WMSHOST
	@echo "${GREEN}Downloading legends...${RESET}";
	WMSPROTOCOL="https"; \
	if [[ $(WMSHOST) == *"localhost"* ]]; then \
		WMSPROTOCOL="http"; \
	fi && \
	scripts/downloadlegends.sh "$${WMSPROTOCOL}://$(WMSHOST)" $(BODID) $(WMSSCALELEGEND)


.PHONY: serve
serve: guard-VENV clean_logs local-templates build
	@echo "${GREEN}Starting gunicorn server...${RESET}";
	${PSERVE} development.ini --reload


.PHONY: shell
shell: guard-VENV clean_logs local-templates build
	${PSHELL} development.ini


.PHONY: dockerlogin
dockerlogin:
	aws --profile swisstopo-bgdi-builder ecr get-login-password --region $(AWS_REGION_ECR) | docker login --username AWS --password-stdin $(DOCKER_REGISTRY)


.PHONY: dockerbuild
dockerbuild: build
	@echo "${GREEN}Building docker image...${RESET}";
	docker build \
		--build-arg GIT_HASH="$(GIT_COMMIT_HASH)" \
		--build-arg GIT_BRANCH="$(GIT_BRANCH)" \
		--build-arg GIT_DIRTY="$(GIT_DIRTY)" \
		--build-arg GIT_TAG="$(GIT_TAG)" \
		--build-arg VERSION="$(APP_VERSION)" \
		--build-arg AUTHOR="$(AUTHOR)" -t $(DOCKER_IMG_LOCAL_TAG_PATH) -f Dockerfile .


.PHONY: dockerrun
dockerrun: guard-OPENTRANS_API_KEY guard-PGUSER guard-PGPASSWORD clean_logs ${LOGS_DIR}
	@echo "${GREEN}Starting docker container...${RESET}";
	docker run \
		-it \
		--network=host \
		--env-file=${ENV_FILE} \
		--env LOGS_DIR=/var/logs \
		--mount type=bind,source="$$(pwd)"/logs,target=/var/logs \
		--env PGUSER=${PGUSER} --env PGPASSWORD=${PGPASSWORD} \
		--env OPENTRANS_API_KEY=${OPENTRANS_API_KEY} \
		--env AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
		--env AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
		--env AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN} \
		--env AWS_SECURITY_TOKEN=${AWS_SECURITY_TOKEN} \
		--env AWS_SESSION_EXPIRATION${AWS_SESSION_EXPIRATION} \
		--env AWS_REGION=${AWS_REGION} \
		$(DOCKER_IMG_LOCAL_TAG_PATH)


.PHONY: dockerrun-shell
dockerrun-shell: guard-OPENTRANS_API_KEY guard-PGUSER guard-PGPASSWORD clean_logs ${LOGS_DIR}
	@echo "${GREEN}Starting docker shell...${RESET}";
	docker run \
		-it \
		--network=host \
		--env-file=${ENV_FILE} \
		--env LOGS_DIR=/var/logs \
		--mount type=bind,source="$$(pwd)"/logs,target=/var/logs \
		--env PGUSER=${PGUSER} --env PGPASSWORD=${PGPASSWORD} \
		--env OPENTRANS_API_KEY=${OPENTRANS_API_KEY} \
		$(DOCKER_IMG_LOCAL_TAG_PATH) /bin/sh


.PHONY: dockerpush
dockerpush:
	docker push $(DOCKER_IMG_LOCAL_TAG_PATH)


.PHONY: dockerpull
dockerpull:
	docker pull $(DOCKER_IMG_LOCAL_TAG_PATH)


.PHONY: test
test: test-integration test-functional


.PHONY: test-integration
test-integration: guard-VENV clean_logs local-templates build
	mkdir -p junit-reports/integration
	@echo "${GREEN}Unit testing (integration tests)...${RESET}";
	${PYTHON} ./scripts/pg_ready.py
	${NOSE} \
		-s tests/integration \
		-t $(PROJECT_PATH) \
		--verbose \
		-c tests/nose2.cfg \
		--junit-xml-path junit-reports/integration/nosetest.xml \
		-N ${PROCESS}


.PHONY: test-functional
test-functional: guard-VENV clean_logs local-templates build
	mkdir -p junit-reports/functional
	@echo "${GREEN}Unit testing (functional tests)...${RESET}";
	${PYTHON} ./scripts/pg_ready.py

	${NOSE} \
		-s tests/functional \
		-t $(PROJECT_PATH) \
		--verbose \
		-c tests/nose2.cfg \
		--junit-xml-path junit-reports/functional/nosetest.xml \
		-N ${PROCESS}


.PHONY: unittest-ci
unittest-ci: guard-VENV clean_logs local-templates build
	@echo "${GREEN}Unit testings for CI...${RESET}";
	mkdir -p junit-reports/integration
	mkdir -p junit-reports/functional
	${NOSE} --verbose \
		-s tests/functional \
		-t $(PROJECT_PATH) \
		-c tests/nose2.cfg \
		--junit-xml-path junit-reports/functional/nosetest.xml \
		--coverage-config .coveragerc_ci_func \
		--coverage-report xml
	${NOSE} --verbose \
		-s tests/integration \
		-t $(PROJECT_PATH) \
		-c tests/nose2.cfg \
		--junit-xml-path junit-reports/integration/nosetest.xml \
		--coverage-config .coveragerc_ci_int \
		--coverage-report xml


.PHONY: teste2e
teste2e: guard-VENV clean_logs local-templates build
	mkdir -p junit-reports/e2e
	@echo "${GREEN}Pseudo E2E tests...${RESET}";
	${NOSE} --verbose \
		-s tests/e2e \
		-t $(PROJECT_PATH) \
		-c tests/nose2.cfg \
		-N ${PROCESS} \
		--junit-xml-path junit-reports/e2e/nosetest.xml

# TODO: Replace through yapf, once the old vhost infra is replaced
.PHONY: lint
lint: guard-VENV
	@echo "${GREEN}Linting python files...${RESET}";
	${FLAKE8} --ignore=${PEP8_IGNORE} $(PYTHON_FILES)
	${PYLINT} .


# TODO: Replace through yapf, once the old vhost infra is replaced
.PHONY: autolint
autolint: guard-VENV
	@echo "${GREEN}Auto correction of python files...${RESET}";
	${AUTOPEP8} --in-place --aggressive --aggressive --verbose --ignore=${PEP8_IGNORE} $(PYTHON_FILES)


# Compiling targets

$(NODE_MODULES): package.json
	@echo "${GREEN}Installing node packages...${RESET}";
	npm install $(NPM_QUIET) --production


node-module-files: $(NODE_MODULES)
	@echo "${GREEN}Building node js static files...${RESET}";
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
TRANSLATION_POT_FILE_DEPENDENCIES := $(shell find chsdi -name "*.py")
$(TRANSLATION_POT_FILE): $(TRANSLATION_POT_FILE_DEPENDENCIES)
	@echo "${GREEN}Extracting the translation...${RESET}";
	${PYTHON} setup.py extract_messages


$(LANGUAGES_PO_FILES): $(TRANSLATION_POT_FILE)
	@echo "${GREEN}Building the translation PO $@ file...${RESET}";
	${PYTHON} setup.py init_catalog -l $(patsubst chsdi/locale/%/LC_MESSAGES/chsdi.po,%, $@)


$(LANGUAGES_MO_FILES): $(LANGUAGES_PO_FILES)
	@echo "${GREEN}Building the translation MO $@ file...${RESET}";
	${PYTHON} setup.py compile_catalog -l $(patsubst chsdi/locale/%/LC_MESSAGES/chsdi.mo,%, $@)


$(LOGS_DIR):
	mkdir -p ${LOGS_DIR}
	chmod 777 ${LOGS_DIR}


guard-%:
	@ if test "${${*}}" = ""; then \
		echo "Environment variable $* not set. Add it to your command."; \
		exit 1; \
	fi


guard-VENV:
	@ if [ ! -e $(VENV) ]; then \
		echo "Virtual environement does not exists build it first with: make setup"; \
		exit 1; \
	fi


# Clean targets

.PHONY: clean
clean:
	@echo "${GREEN}Cleaning generated files...${RESET}";
	rm -f base.ini
	rm -f production.ini
	rm -f development.ini
	rm -f 25-mf-chsdi3.conf
	rm -f apache/application.wsgi
	rm -f apache/wsgi.conf
	rm -f chsdi/static/info.json
	rm -f chsdi/static/robots.txt
	rm -rf chsdi/static/js/*
	rm -f  chsdi/static/css/blueimp-gallery.min.css
	rm -f  chsdi/static/css/extended.min.css
	rm -rf $(TRANSLATION_DIRS)
	find chsdi/static/js -type f ! -name .gitignore -exec rm -f \;
	rm -f .coverage .coverage.*
	rm -f requirements.txt
	find chsdi -name "__pycache__" -depth -exec rm -rf "{}" \;


clean_logs:
	rm -rf ${LOGS_DIR}


.PHONY: cleanall
cleanall: clean clean_logs
	@echo "${GREEN}Cleaning everything...${RESET}";
	rm -rf chsdi.egg-info/
	rm -f  package-lock.json
	rm -rf $(NODE_MODULES)
	if [ -d "$(VENV)" ]; then pipenv --rm; fi



