SHELL = /bin/bash
.DEFAULT_GOAL := help

SERVICE_NAME := mf-chsdi3

# Macro functions
lastvalue = $(shell if [ -f .venv/last-$1 ]; then cat .venv/last-$1 2> /dev/null; else echo '-none-'; fi;)

define cachelastvariable
	mkdir -p $(dir $1)
	test "$2" != "$3" && \
	    echo "$2" > .venv/last-$4 || :
endef

# Script variables
BODID ?=
DEPLOY_TARGET ?=
BRANCH_TO_DELETE ?=
WMSSCALELEGEND ?=

# Variables
USER_SOURCE ?= rc_user
CURRENT_DIRECTORY := $(shell pwd)
WSGI_APP := $(CURRENT_DIRECTORY)/apache/application.wsgi
INSTALL_DIRECTORY := .venv
KML_TEMP_DIR := /var/local/print/kml
MODWSGI_USER := www-data
HTTP_PROXY := http://ec2-52-28-118-239.eu-central-1.compute.amazonaws.com:80
BRANCH_STAGING := $(shell if [ '$(DEPLOY_TARGET)' = 'dev' ]; then echo 'test'; else echo 'integration'; fi)
GIT_BRANCH := $(shell if [ -f '.venv/deployed-git-branch' ]; \
							  then cat .venv/deployed-git-branch 2> /dev/null; else git rev-parse --symbolic-full-name --abbrev-ref HEAD; fi)
GIT_COMMIT_HASH ?= $(shell git rev-parse --verify HEAD)
GIT_COMMIT_SHORT ?= $(shell git rev-parse --short $(GIT_COMMIT_HASH))
GIT_COMMIT_DATE ?= $(shell git log -1  --date=iso --pretty=format:%cd)
DOCKER_IMG_TAG_LATEST ?= $(DOCKER_REGISTRY)/${SERVICE_NAME}:${GIT_BRANCH}.latest
CURRENT_DATE ?= $(shell date -u +"%Y-%m-%d %H:%M:%S %z")
NO_TESTS ?= withtests
NODE_DIRECTORY := node_modules
APACHE_ENTRY_PATH := $(shell if [ '$(APACHE_BASE_PATH)' = 'main' ]; then echo ''; else echo /$(APACHE_BASE_PATH); fi)
DATAGEOADMINHOST ?= data.geo.admin.ch
AWS_DEFAULT_REGION ?= eu-west-1
SHORTENER_ALLOWED_DOMAINS := admin.ch, swisstopo.ch, bgdi.ch
SHORTENER_ALLOWED_HOSTS ?=
# A single table for dev, int and prod. Different name for each build test
GEOADMIN_FILE_STORAGE_TABLE_NAME ?= geoadmin-file-storage
GEOADMIN_FILE_STORAGE_TABLE_REGION ?= $(AWS_DEFAULT_REGION)
GEOADMIN_FILE_STORAGE_BUCKET ?= public-dev-bgdi-ch
GLSTYLES_STORAGE_TABLE_NAME ?= vectortiles-styles-storage
GLSTYLES_STORAGE_TABLE_REGION ?= $(AWS_DEFAULT_REGION)
GLSTYLES_STORAGE_BUCKET ?= $(GEOADMIN_FILE_STORAGE_BUCKET)
SHORTENER_TABLE_NAME ?= shorturl
SHORTENER_TABLE_REGION ?= $(AWS_DEFAULT_REGION)
PYPI_URL ?= https://pypi.org/simple/
GITHUB_LAST_COMMIT=$(shell curl -s  https://api.github.com/repos/geoadmin/mf-chsdi3/commits | jq -r '.[0].sha')
DYNAMIC_TRANSLATION ?= 1

# Docker metadata
GIT_HASH = $(shell git rev-parse HEAD)
GIT_HASH_SHORT = $(shell git rev-parse --short HEAD)
GIT_BRANCH = $(shell git symbolic-ref HEAD --short 2>/dev/null)
GIT_DIRTY = $(shell git status --porcelain)
GIT_TAG = $(shell git describe --tags || echo "no version info")
AUTHOR = $(USER)

# Docker variables
DOCKER_REGISTRY = 974517877189.dkr.ecr.eu-central-1.amazonaws.com
DOCKER_IMG_LOCAL_TAG := $(DOCKER_REGISTRY)/$(SERVICE_NAME):local-$(USER)-$(GIT_HASH_SHORT)
DOCKER_IMAGE_LOCAL_TAG_BASEIMAGE = $(DOCKER_REGISTRY)/mf-chsdi3:base

# AWS variables
 AWS_DEFAULT_REGION ?= eu-central-1


# Last values
KEEP_VERSION ?= 'false'
LAST_VERSION := $(call lastvalue,version)
VERSION := $(shell if [ '$(KEEP_VERSION)' = 'true' ] && [ '$(LAST_VERSION)' != '-none-' ]; \
						 then echo $(LAST_VERSION); else date +'%s'; fi)
LAST_MODWSGI_CONFIG := $(call lastvalue,modwsgi-config)
LAST_SERVER_PORT := $(call lastvalue,server-port)
LAST_CURRENT_DIRECTORY := $(call lastvalue,current-directory)
LAST_APACHE_BASE_PATH := $(call lastvalue,apache-base-path)
LAST_APACHE_ENTRY_PATH := $(call lastvalue,apache-entry-path)
LAST_DBHOST := $(call lastvalue,dbhost)
LAST_DBPORT := $(call lastvalue,dbport)
LAST_DBSTAGING := $(call lastvalue,dbstaging)
LAST_GEODATA_STAGING := $(call lastvalue,geodata-staging)
LAST_SPHINXHOST := $(call lastvalue,sphinxhost)
LAST_WMSHOST := $(call lastvalue,wmshost)
LAST_WMTS_PUBLIC_HOST := $(call lastvalue,wmts-public-host)
LAST_GEOADMINHOST := $(call lastvalue,geoadminhost)
LAST_ALTI_URL := $(call lastvalue,alti-url)
LAST_API_URL := $(call lastvalue,api-url)
LAST_SHOP_URL := $(call lastvalue,shop-url)
LAST_HOST := $(call lastvalue,host)
LAST_GEOADMIN_FILE_STORAGE_BUCKET := $(call lastvalue,geoadmin-file-storage-bucket)
LAST_GEOADMIN_FILE_STORAGE_TABLE_NAME := $(call lastvalue,geoadmin-file-storage-table-name)
LAST_GEOADMIN_FILE_STORAGE_TABLE_REGION := $(call lastvalue,geoadmin-file-storage-table-region)
LAST_GLSTYLES_STORAGE_TABLE_NAME := $(call lastvalue,glstyles-storage-table-name)
LAST_GLSTYLES_STORAGE_TABLE_REGION := $(call lastvalue,glstyles-storage-table-region)
LAST_PUBLIC_BUCKET_HOST  := $(call lastvalue,public-bucket-host)
LAST_SHORTENER_ALLOWED_HOSTS := $(call lastvalue,shortener-allowed-hosts)
LAST_SHORTENER_TABLE_NAME := $(call lastvalue,shortener-table-name)
LAST_SHORTENER_TABLE_REGION := $(call lastvalue,shortener-table-region)
LAST_VECTOR_BUCKET := $(call lastvalue,vector-bucket)
LAST_DATAGEOADMINHOST := $(call lastvalue,datageoadminhost)
LAST_CMSGEOADMINHOST := $(call lastvalue,cmsgeoadminhost)
LAST_LINKEDDATAHOST := $(call lastvalue,linkeddatahost)
LAST_OPENTRANS_API_KEY := $(call lastvalue,opentrans-api-key)
LAST_SHORTENER_ALLOWED_DOMAINS := $(call lastvalue,shortener-allowed-domains)
LAST_ROBOTS_FILE := $(call lastvalue,robots-file)
LAST_WSGI_THREADS := $(call lastvalue,wsgi-threads)
LAST_BRANCH_STAGING := $(call lastvalue,branch-staging)
LAST_GIT_BRANCH := $(call lastvalue,git-branch)
LAST_DEPLOY_TARGET := $(call lastvalue,deploy_target)
LAST_CACHE_CONTROL := $(call lastvalue,cache-control)
LAST_WSGI_USER := $(call lastvalue,wsgi-user)
LAST_WSGI_PROCESSES := $(call lastvalue,wsgi-processes)
LAST_WSGI_THREADS := $(call lastvalue,wsgi-threads)
LAST_WSGI_APP := $(call lastvalue,wsgi-app)
LAST_KML_TEMP_DIR := $(call lastvalue,kml-temp-dir)
LAST_GIT_COMMIT_HASH ?= $(call lastvalue,git-commit-hash)
LAST_GIT_COMMIT_SHORT ?= $(call lastvalue,git-commit-short)
LAST_GITHUB_LAST_COMMIT := $(call lastvalue,github-last-commit)
LAST_DYNAMIC_TRANSLATION := $(call lastvalue,dynamic-translation)

PYTHON_FILES := $(shell find chsdi/* tests/* -path chsdi/static -prune -o -path chsdi/lib/sphinxapi -prune -o -path tests/e2e -prune -o -type f -name "*.py" -print)
TEMPLATE_FILES := $(shell find -type f -name "*.in" -print)

# Commands
AUTOPEP8_CMD := $(INSTALL_DIRECTORY)/bin/autopep8
FLAKE8_CMD := $(INSTALL_DIRECTORY)/bin/flake8
MAKO_CMD := $(INSTALL_DIRECTORY)/bin/mako-render
NOSE_CMD := $(INSTALL_DIRECTORY)/bin/nosetests
PIP_CMD := $(INSTALL_DIRECTORY)/bin/pip
PSERVE_CMD := $(INSTALL_DIRECTORY)/bin/pserve
PSHELL_CMD := $(INSTALL_DIRECTORY)/bin/pshell
PYTHON_CMD := $(INSTALL_DIRECTORY)/bin/python
SPHINX_CMD := $(INSTALL_DIRECTORY)/bin/sphinx-build
ENVSUBST_CMD := /usr/bin/envsubst

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

# Colors
RESET := $(shell tput sgr0)
RED := $(shell tput setaf 1)
GREEN := $(shell tput setaf 2)

# Versions
# We need GDAL which is hard to install in a venv, modify PYTHONPATH to use the
# system wide version.
GDAL_VERSION ?= 1.10.0
PYTHON_INSTALL_VERSION ?= 3.7.10

ifndef USE_PYTHON3
		override USE_PYTHON3 = 0
endif

ifeq ($(USE_PYTHON3), 1)
ifeq (, $(shell which $(SYSTEM_PYTHON_CMD)))
		PYTHON_VERSION := $(shell $(PYTHON_INSTALL_VERSION)  --version 2>&1 | cut -d ' ' -f 2 | cut -d '.' -f 1,2)
else
    PYTHON_VERSION := $(shell $(SYSTEM_PYTHON_CMD)  --version 2>&1 | cut -d ' ' -f 2 | cut -d '.' -f 1,2)
endif
PIP_CMD := $(INSTALL_DIRECTORY)/bin/pip${PYTHON_VERSION}
build/python:
		mkdir -p build && touch build/python;
else
		PYTHON_VERSION := $(shell python2 --version 2>&1 | cut -d ' ' -f 2 | cut -d '.' -f 1,2)
build/python:
		mkdir -p build && touch build/python;
endif
PYTHONPATH ?= .venv/lib/python${PYTHON_VERSION}/site-packages:/usr/lib64/python${PYTHON_VERSION}/site-packages

PYTHON_BINDIR := $(shell dirname $(PYTHON_CMD))
PYTHONHOME :=$(shell eval "cd $(PYTHON_BINDIR); pwd; cd > /dev/null")
SYSTEM_PYTHON_CMD ?= $(CURRENT_DIRECTORY)/local/bin/python$(PYTHON_VERSION)

.PHONY: python
python: build/python
		@echo "Python installed"

local/bin/python3.7:
		mkdir -p $(CURRENT_DIRECTORY)/local;
		curl https://www.python.org/ftp/python/$(PYTHON_INSTALL_VERSION)/Python-$(PYTHON_INSTALL_VERSION).tar.xz \
				-o $(CURRENT_DIRECTORY)/local/Python-$(PYTHON_INSTALL_VERSION).tar.xz;
		cd $(CURRENT_DIRECTORY)/local && tar -xf Python-$(PYTHON_INSTALL_VERSION).tar.xz && Python-$(PYTHON_INSTALL_VERSION)/configure --prefix=$(CURRENT_DIRECTORY)/local/   --with-ensurepip=install --enable-optimizations && make altinstall;

.PHONY: print_vars 
print_vars:
	    $(foreach v, $(.VARIABLES), $(if $(filter file,$(origin $(v))), $(info $(v)=$($(v)))))

.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Possible targets:"
	@echo "- user               Build the user specific version of the app"
	@echo "- all                Build the app"
	@echo "- serve              Serve the application with pserve"
	@echo "- shell              Enter interactive shell with app loaded in the background"
	@echo "- test               Launch the tests (no e2e tests)"
	@echo "- testci             Lauch tests with reports (for CI)"
	@echo "- teste2e            Launch end-to-end tests"
	@echo "- lint               Run the linter"
	@echo "- autolint           Run the autolinter"
	@echo "- translate          Generate the translation files"
	@echo "- legends            Downloads and optimizes all WMS legend images (make legends BODID=ch.foo WMSSCALELEGEND=)"
	@echo "- doc                Generate the doc for api3.geo.admin.ch"
	@echo "- deploybranch       Deploy current branch to dev (must be pushed before hand)"
	@echo "- deploybranchint    Deploy current branch to dev and int (must be pushed before hand)"
	@echo "- deletebranch       List deployed branches or delete a deployed branch on dev and int (BRANCH_TO_DELETE=...)"
	@echo "- deletebranchdev    List deployed branches or delete a deployed branch on dev (BRANCH_TO_DELETE=...)"
	@echo "- deletebranchint    List deployed branches or delete a deployed branch on int (BRANCH_TO_DELETE=...)"
	@echo "- updateapi          Updates geoadmin api source code (ol3 fork)"
	@echo "- deploydev          Deploys master to dev (SNAPSHOT=true to also create a snapshot)"
	@echo "- updatedev          Updates master to dev, if version has changed (with snapshot)"
	@echo "- deployint          Deploys a snapshot to integration (SNAPSHOT=201512021146)"
	@echo "- deployprod         Deploys a snapshot to production (SNAPSHOT=201512021146)"
	@echo "- clean              Remove generated files"
	@echo "- cleanall           Remove all the build artefacts"
	@echo "- pythonclean        Remove all the build artefacts and the downloaded python version"
	@echo
	@echo "Variables:"
	@echo "USE_PYTHON3          ${USE_PYTHON3}"
	@echo "PYTHON_VERSION:      ${PYTHON_VERSION}"
	@echo "PYTHON_CMD:          ${PYTHON_CMD}"
	@echo "SYSTEM_PYTHON_CMD:   ${SYSTEM_PYTHON_CMD}"
	@echo "PIP_CMD:             ${PIP_CMD}"
	@echo "PYTHONPATH:          ${PYTHONPATH}"
	@echo "APACHE_ENTRY_PATH:   ${APACHE_ENTRY_PATH}"
	@echo "API_URL:             ${API_URL}"
	@echo "WMSHOST:             ${WMSHOST}"
	@echo "BRANCH_STAGING:      ${BRANCH_STAGING}"
	@echo "DBHOST:              ${DBHOST}"
	@echo "DBSTAGING:           ${DBSTAGING}"
	@echo "GEOADMINHOST:        ${GEOADMINHOST}"
	@echo "GIT_BRANCH:          ${GIT_BRANCH}"
	@echo "SERVER_PORT:         ${SERVER_PORT}"
	@echo "OPENTRANS_API_KEY:   ${OPENTRANS_API_KEY}"
	@echo "DOCKER_IMG_LOCAL_TAG   ${DOCKER_IMG_LOCAL_TAG}"
	@echo "DOCKER_IMG_TAG_LATEST  ${DOCKER_IMG_TAG_LATEST}"
	@echo


.PHONY: user
user:
	source $(USER_SOURCE) && make all

# TODO removed rss
.PHONY: all
all: setup chsdi/static/css/extended.min.css templates translate lint fixrights doc rss

setup: .venv node_modules .venv/hooks

ifeq ($(USE_PYTHON3), 1)
templates: apache/wsgi.conf apache/application.wsgi development.ini production.ini chsdi/static/info.json
	$(call build_templates,$(DEPLOY_TARGET))
else
templates: apache/wsgi.conf development.ini production.ini chsdi/static/info.json
endif

.PHONY: image
image:
	docker build \
		--build-arg GIT_HASH="$(GIT_HASH)" \
		--build-arg GIT_BRANCH="$(GIT_BRANCH)" \
		--build-arg GIT_DIRTY="$(GIT_DIRTY)" \
		--build-arg VERSION="$(GIT_TAG)" \
		--build-arg AUTHOR="$(AUTHOR)" -t $(DOCKER_IMG_LOCAL_TAG) -t ${DOCKER_IMG_TAG_LATEST} -f Dockerfile .


.PHONY: dockerlogin
dockerlogin:
	aws --profile swisstopo-bgdi-builder ecr get-login-password --region $(AWS_DEFAULT_REGION) | docker login --username AWS --password-stdin $(DOCKER_REGISTRY)


.PHONY: dockerpush
dockerpush: image
	docker push $(DOCKER_IMG_TAG_LATEST)
	docker push $(DOCKER_IMG_LOCAL_TAG)


.PHONY: environ
environ:
	$(call build_templates,$(DEPLOY_TARGET))

define build_templates
	export $(shell cat $1.env) && source rc_$1 && export DOCKER_IMG_LOCAL_TAG=${DOCKER_IMG_LOCAL_TAG} && export DOCKER_IMG_TAG_LATEST=${DOCKER_IMG_TAG_LATEST} && \
		envsubst < apache/wsgi-py3.conf.in > apache/wsgi.conf && \
		envsubst <  apache/application.wsgi.in > apache/application.wsgi && \
		envsubst < docker-compose.yml.in > docker-compose.yml && \
		envsubst < 25-mf-chsdi3.conf.in > 25-mf-chsdi3.conf
endef

.PHONY: serve
serve:
	PYTHONPATH=${PYTHONPATH} ${PSERVE_CMD} development.ini --reload

.PHONY: shell
shell:
	PYTHONPATH=${PYTHONPATH} ${PSHELL_CMD} development.ini

.PHONY: test
test:
	PYTHONPATH=${PYTHONPATH} ${NOSE_CMD}  tests/ -e .*e2e.*

.PHONY: testci
testci:
	mkdir -p junit-reports/{integration,functional}
	PYTHONPATH=${PYTHONPATH} ${NOSE_CMD} --with-xunit --xunit-file=junit-reports/functional/nosetest.xml   tests/functional -e .*e2e.*
	PYTHONPATH=${PYTHONPATH} ${NOSE_CMD} --with-xunit --xunit-file=junit-reports/integration/nosetest.xml  tests/integration -e .*e2e.*

.PHONY: teste2e
teste2e:
	PYTHONPATH=${PYTHONPATH} ${NOSE_CMD} tests/e2e/

.PHONY: lint
lint:
	@echo "${GREEN}Linting python files...${RESET}";
	${FLAKE8_CMD} --ignore=${PEP8_IGNORE} $(PYTHON_FILES) && echo ${RED}

.PHONY: autolint
autolint:
	@echo "${GREEN}Auto correction of python files...${RESET}";
	${AUTOPEP8_CMD} --in-place --aggressive --aggressive --verbose --ignore=${PEP8_IGNORE} $(PYTHON_FILES)

.PHONY: doc
doc: chsdi/static/css/extended.min.css
	@echo "${GREEN}Building the documentation...${RESET}";
	cd chsdi/static/doc && ../../../${SPHINX_CMD} -W -b html source build || exit 1 ;

.PHONY:
rss: doc chsdi/static/doc/build/releasenotes/index.html
	@echo "${GREEN}Creating the rss feed from releasenotes${RESET}";
	${PYTHON_CMD} scripts/rssFeedGen.py "https://api3.geo.admin.ch"

.PHONY: translate
translate:
	@echo "${GREEN}Updating translations...${RESET}";
	make pofiles potomo
	
.PHONY: pofiles
pofiles:
		@echo "${GREEN}Generating pofiles...${RESET}";
		mkdir -p chsdi/locale/{de,fr,it,fi,en}/LC_MESSAGES;
		source rc_prod && ${PYTHON_CMD} scripts/translation2po.py chsdi/locale/

chsdi/locale/en/LC_MESSAGES/chsdi.po:
chsdi/locale/en/LC_MESSAGES/chsdi.mo: chsdi/locale/en/LC_MESSAGES/chsdi.po
	msgfmt -o $@ $<
chsdi/locale/fr/LC_MESSAGES/chsdi.po:
chsdi/locale/fr/LC_MESSAGES/chsdi.mo: chsdi/locale/fr/LC_MESSAGES/chsdi.po
	msgfmt -o $@ $<
chsdi/locale/de/LC_MESSAGES/chsdi.po:
chsdi/locale/de/LC_MESSAGES/chsdi.mo: chsdi/locale/de/LC_MESSAGES/chsdi.po
	msgfmt -o $@ $<
chsdi/locale/fi/LC_MESSAGES/chsdi.po:
chsdi/locale/fi/LC_MESSAGES/chsdi.mo: chsdi/locale/fi/LC_MESSAGES/chsdi.po
	msgfmt -o $@ $<
chsdi/locale/it/LC_MESSAGES/chsdi.po:
chsdi/locale/it/LC_MESSAGES/chsdi.mo: chsdi/locale/it/LC_MESSAGES/chsdi.po
	msgfmt -o $@ $<

potomo: chsdi/locale/en/LC_MESSAGES/chsdi.mo chsdi/locale/fr/LC_MESSAGES/chsdi.mo \
        chsdi/locale/de/LC_MESSAGES/chsdi.mo chsdi/locale/fi/LC_MESSAGES/chsdi.mo \
        chsdi/locale/it/LC_MESSAGES/chsdi.mo

### vhosts specific targets ###
.PHONY: deploybranch
deploybranch:
	@echo "${GREEN}Deploying branch $(GIT_BRANCH) to dev...${RESET}";
	./scripts/deploybranch.sh

.PHONY: deletebranch
deletebranch:
	make deletebranchdev BRANCH_TO_DELETE=$(BRANCH_TO_DELETE)
	make deletebranchint BRANCH_TO_DELETE=$(BRANCH_TO_DELETE)

.PHONY: deletebranchdev
deletebranchdev:
	./scripts/delete_branch.sh dev $(BRANCH_TO_DELETE)

.PHONY: deletebranchint
deletebranchint:
	./scripts/delete_branch.sh int $(BRANCH_TO_DELETE)

.PHONY: deploybranchint
deploybranchint:
	@echo "${GREEN}Deploying branch $(GIT_BRANCH) to dev and int...${RESET}";
	./scripts/deploybranch.sh int

# Remove when ready to be merged
.PHONY: deploydev
deploydev:
	@if test "$(SNAPSHOT)" = "true"; \
	then \
		scripts/deploydev.sh -s; \
	else \
		scripts/deploydev.sh; \
	fi

.PHONY: updatedev
updatedev: .venv/last-github-last-commit
		@if [ "${GITHUB_LAST_COMMIT}" == "${LAST_GITHUB_LAST_COMMIT}"   ]; then \
				echo "No updating dev"; \
		else \
		    scripts/deploydev.sh -s; \
		fi


.PHONY: deployint
deployint: guard-SNAPSHOT
	scripts/deploysnapshot.sh $(SNAPSHOT) int $(NO_TESTS)

.PHONY: deployprod
deployprod: guard-SNAPSHOT
	scripts/deploysnapshot.sh $(SNAPSHOT) prod $(NO_TESTS)

.PHONY: legends
legends: guard-BODID guard-WMSHOST
	source rc_user && scripts/downloadlegends.sh $(WMSHOST) $(BODID) $(WMSSCALELEGEND)

chsdi/templates/info.json.mako:
	@echo "${GREEN}info.json has changed${RESET}";
chsdi/static/info.json:  chsdi/templates/info.json.mako
		${PYTHON_CMD} ${MAKO_CMD} \
		--var "version=$(VERSION)" \
		--var "git_branch=$(GIT_BRANCH)" \
		--var "git_commit_short=$(GIT_COMMIT_SHORT)" \
		--var "git_commit_date=$(GIT_COMMIT_DATE)" \
		--var "git_commit_hash=$(GIT_COMMIT_HASH)" \
		--var "python_version=$(PYTHON_VERSION)" \
		--var "build_date=$(CURRENT_DATE)"  $< > $@

rc_branch.mako:
	@echo "${GREEN}Branch has changed${RESET}";
rc_branch: rc_branch.mako \
           .venv/last-git-branch \
           .venv/last-deploy-target \
           .venv/last-branch-staging
	@echo "${GREEN}Creating branch template...${RESET}"
	${MAKO_CMD} \
		--var "git_branch=$(GIT_BRANCH)" \
		--var "deploy_target=$(DEPLOY_TARGET)" \
		--var "branch_staging=$(BRANCH_STAGING)" $< > $@

deploy/deploy-branch.cfg.in:
	@echo "${GREEN]}Template file deploy/deploy-branch.cfg.in has changed${RESET}";
deploy/deploy-branch.cfg: deploy/deploy-branch.cfg.in \
                          .venv/last-git-branch
	@echo "${GREEN}Creating deploy/deploy-branch.cfg...${RESET}";
	${MAKO_CMD} --var "git_branch=$(GIT_BRANCH)" $< > $@

deploy/conf/00-branch.conf.in:
	@echo "${GREEN}Templat file deploy/conf/00-branch.conf.in has changed${RESET}";
deploy/conf/00-branch.conf: deploy/conf/00-branch.conf.in \
                            .venv/last-git-branch
	@echo "${GREEN}Creating deploy/conf/00-branch.conf...${RESET}"
	${MAKO_CMD} --var "git_branch=$(GIT_BRANCH)" $< > $@


### Starting script is different again in python2 and python3
apache/application.wsgi.mako:
		@echo "${GREEN}Template file apache/application.wsgi.mako has changed${RESET}";

apache/application.wsgi.in:
	@echo "${GREEN}Template file apache/application.wsgi.in has changed${RESET}";

ifeq ($(USE_PYTHON3), 0)
apache/application.wsgi: apache/application.wsgi.mako \
                         .venv/last-current-directory \
                         .venv/last-modwsgi-config
		@echo "${GREEN}Creating apache/application.wsgi...${RESET}";
		${MAKO_CMD} \
				--var "current_directory=$(CURRENT_DIRECTORY)" \
				--var "modwsgi_config=$(MODWSGI_CONFIG)" $< > $@
else

apache/application.wsgi: apache/application.wsgi.in\
                         .venv/last-current-directory \
                         .venv/last-modwsgi-config
	@echo "${GREEN}Creating apache/application.wsgi...${RESET}";
	${ENVSUBST_CMD} < $< > $@

endif

apache/wsgi.conf.in:
	@echo "${GREEN}Template file apache/wsgi.conf.in has changed${RESET}";

apache/wsgi-py3.conf.in:
	@echo "${GREEN}Template file apache/wsgi-py3.conf.in has changed${RESET}";

ifeq ($(USE_PYTHON3), 1)

apache/wsgi.conf: apache/wsgi-py3.conf.in \
                  apache/application.wsgi \
                  .venv/last-apache-base-path \
                  .venv/last-apache-entry-path \
                  .venv/last-robots-file \
                  .venv/last-branch-staging \
                  .venv/last-git-branch \
                  .venv/last-current-directory \
                  .venv/last-deploy-target \
                  .venv/last-modwsgi-user \
                  .venv/last-wsgi-processes \
                  .venv/last-wsgi-threads \
                  .venv/last-wsgi-app \
                  .venv/last-kml-temp-dir
	@echo "${GREEN}Creating apache/wsgi.conf...${RESET}";
	${ENVSUBST_CMD} < $< > $@

else
apache/wsgi.conf: apache/wsgi.conf.in \
                  apache/application.wsgi \
                  .venv/last-apache-base-path \
                  .venv/last-apache-entry-path \
                  .venv/last-robots-file \
                  .venv/last-branch-staging \
                  .venv/last-git-branch \
                  .venv/last-current-directory \
                  .venv/last-deploy-target \
                  .venv/last-modwsgi-user \
                  .venv/last-wsgi-processes \
                  .venv/last-wsgi-threads \
                  .venv/last-wsgi-app \
                  .venv/last-kml-temp-dir
		@echo "${GREEN}Creating apache/wsgi.conf...${RESET}";
		${MAKO_CMD} \
				--var "apache_base_path=$(APACHE_BASE_PATH)" \
				--var "apache_entry_path=$(APACHE_ENTRY_PATH)" \
				--var "robots_file=$(ROBOTS_FILE)" \
				--var "branch_staging=$(BRANCH_STAGING)" \
				--var "git_branch=$(GIT_BRANCH)" \
				--var "current_directory=$(CURRENT_DIRECTORY)" \
				--var "deploy_target=$(DEPLOY_TARGET)" \
				--var "cache_control=$(CACHE_CONTROL)" \
				--var "modwsgi_user=$(MODWSGI_USER)" \
				--var "wsgi_processes=$(WSGI_PROCESSES)" \
				--var "wsgi_threads=$(WSGI_THREADS)" \
				--var "wsgi_app=$(WSGI_APP)" \
				--var "kml_temp_dir=$(KML_TEMP_DIR)" $< > $@
endif

app.log:
	touch $@
	chmod a+rw $@


development.ini.in: app.log
	@echo "${GREEN}Template file development.ini.in has changed${RESET}";
development.ini: development.ini.in \
	               .venv/last-version \
	               .venv/last-server-port
	@echo "${GREEN}Creating development.ini....${RESET}";
	${ENVSUBST_CMD} <  $< > $@

production.ini.in:
	@echo "${GREEN}Template file production.ini.in has changed${RESET}";
production.ini: production.ini.in \
                .venv/last-version \
                .venv/last-server-port \
                .venv/last-apache-base-path \
                .venv/last-apache-entry-path \
                .venv/last-current-directory \
                .venv/last-dbhost \
                .venv/last-dbport \
                .venv/last-dbstaging \
                .venv/last-alti-url \
                .venv/last-api-url \
                .venv/last-shop-url \
                .venv/last-geodata-staging \
                .venv/last-sphinxhost \
                .venv/last-wmshost \
                .venv/last-wmts-public-host \
                .venv/last-geoadminhost \
                .venv/last-host \
                .venv/last-kml-temp-dir \
                .venv/last-http-proxy \
                .venv/last-geoadmin-file-storage-bucket \
                .venv/last-geoadmin-file-storage-table-name \
                .venv/last-geoadmin-file-storage-table-region \
								.venv/last-glstyles-storage-table-name \
								.venv/last-glstyles-storage-table-region \
                .venv/last-public-bucket-host \
                .venv/last-shortener-allowed-hosts \
                .venv/last-vector-bucket \
                .venv/last-datageoadminhost \
                .venv/last-cmsgeoadminhost \
                .venv/last-linkeddatahost \
                .venv/last-opentrans-api-key \
                .venv/last-shortener-allowed-domains \
                .venv/last-shortener-table-name \
                .venv/last-shortener-table-region \
								.venv/last-dynamic-translation \
                guard-OPENTRANS_API_KEY
	@echo "${GREEN}Creating production.ini...${RESET}";
	${MAKO_CMD} \
		--var "APP_VERSION=$(VERSION)" \
		--var "SERVER_PORT=$(SERVER_PORT)" \
		--var "APACHE_BASE_PATH=$(APACHE_BASE_PATH)" \
		--var "APACHE_ENTRY_PATH=$(APACHE_ENTRY_PATH)" \
		--var "CURRENT_DIRECTORY=$(CURRENT_DIRECTORY)" \
		--var "DBHOST=$(DBHOST)" \
		--var "DBPORT=$(DBPORT)" \
		--var "DBSTAGING=$(DBSTAGING)" \
		--var "ALTI_URL=$(ALTI_URL)" \
		--var "API_URL=$(API_URL)" \
		--var "SHOP_URL=$(SHOP_URL)" \
		--var "GEODATA_STAGING=$(GEODATA_STAGING)" \
		--var "SPHINXHOST=$(SPHINXHOST)" \
		--var "WMSHOST=$(WMSHOST)" \
		--var "WMTS_PUBLIC_HOST=$(WMTS_PUBLIC_HOST)" \
		--var "GEOADMINHOST=$(GEOADMINHOST)" \
		--var "HOST=$(HOST)" \
		--var "KML_TEMP_DIR=$(KML_TEMP_DIR)" \
		--var "HTTP_PROXY=$(HTTP_PROXY)" \
		--var "GEOADMIN_FILE_STORAGE_BUCKET=$(GEOADMIN_FILE_STORAGE_BUCKET)" \
		--var "GEOADMIN_FILE_STORAGE_TABLE_REGION=$(GEOADMIN_FILE_STORAGE_TABLE_REGION)" \
		--var "GEOADMIN_FILE_STORAGE_TABLE_NAME=$(GEOADMIN_FILE_STORAGE_TABLE_NAME)" \
		--var "GLSTYLES_STORAGE_TABLE_NAME=$(GLSTYLES_STORAGE_TABLE_NAME)" \
		--var "GLSTYLES_STORAGE_TABLE_REGION=$(GLSTYLES_STORAGE_TABLE_REGION)" \
		--var "PUBLIC_BUCKET_HOST=$(PUBLIC_BUCKET_HOST)" \
		--var "SHORTENER_ALLOWED_HOSTS=$(SHORTENER_ALLOWED_HOSTS)" \
		--var "SHORTENER_TABLE_NAME=$(SHORTENER_TABLE_NAME)" \
		--var "SHORTENER_TABLE_REGION=$(SHORTENER_TABLE_REGION)" \
		--var "VECTOR_BUCKET=$(VECTOR_BUCKET)" \
		--var "DATAGEOADMINHOST=$(DATAGEOADMINHOST)" \
		--var "CMSGEOADMINHOST=$(CMSGEOADMINHOST)" \
		--var "LINKEDDATAHOST=$(LINKEDDATAHOST)" \
		--var "OPENTRANS_API_KEY=$(OPENTRANS_API_KEY)" \
		--var "DYNAMIC_TRANSLATION=$(DYNAMIC_TRANSLATION)" \
		--var "SHORTENER_ALLOWED_DOMAINS=$(SHORTENER_ALLOWED_DOMAINS)" $< > $@

.venv/hooks: .venv/bin/git-secrets ./scripts/install-git-hooks.sh
	@echo "${GREEN}Installing git hooks${RESET}";
	./scripts/install-git-hooks.sh
	touch $@

ifeq ($(USE_PYTHON3), 1)
requirements-py3.txt:
	@echo "${GREEN}File requirements-py3.txt has changed${RESET}";

.venv: requirements-py3.txt
		test -d "$(INSTALL_DIRECTORY)" || $(SYSTEM_PYTHON_CMD) -m venv $(INSTALL_DIRECTORY); \
		${PIP_CMD} install --upgrade pip==21.2.4 setuptools --index-url ${PYPI_URL} ;
		${PIP_CMD} install -r requirements-py3.txt --index-url ${PYPI_URL}  -e .
else
requirements.txt:
	@echo "${GREEN}File requirements.txt has changed${RESET}";
.venv: requirements.txt
	@echo "${GREEN}Setting up virtual environement...${RESET}";
	@if [ ! -d $(INSTALL_DIRECTORY) ]; \
	then \
		virtualenv -p /usr/bin/python2  $(INSTALL_DIRECTORY); \
		${PIP_CMD} install pip==19.2.3 setuptools==44.1.1 enum34==1.1.6 --index-url ${PYPI_URL} ; \
		${PIP_CMD} install --requirement requirements.txt  --index-url ${PYPI_URL} ; \
	fi
	${PIP_CMD} install --index-url ${PYPI_URL} -e .
endif

.venv/bin/git-secrets: .venv
	@echo "${GREEN}Installing git secrets${RESET}";
	if [ ! -d ".git" ]; then git init; fi
	rm -rf .venv/git-secrets
	git clone https://github.com/awslabs/git-secrets .venv/git-secrets
	cd .venv/git-secrets  && git reset --hard 635895a8d1b7c976ac9794cef420f8dc111a24d4 && make install PREFIX=..
	(git config --local --get-regexp secret && git config --remove-section secrets) || cd
	.venv/bin/git-secrets --register-aws

package.json:
	@echo "${GREEN}File package.json has changed${RESET}";
node_modules: package.json
	@echo "${GREEN}Installing node packages...${RESET}";
	npm install --production
	cp -f node_modules/jquery/dist/jquery.min.js chsdi/static/js/jquery.min.js
	cp -f node_modules/blueimp-gallery/js/blueimp-gallery.min.js chsdi/static/js/blueimp-gallery.min.js
	cp -f node_modules/d3/d3.min.js chsdi/static/js/d3.min.js
	cp -f node_modules/d3-tip/index.js chsdi/static/js/d3-tip.js
	cp -f node_modules/blueimp-gallery/css/blueimp-gallery.min.css chsdi/static/css/blueimp-gallery.min.css

chsdi/static/less/extended.less:
	@echo "${GREEN}File chsdi/static/less/extended.less has changed${RESET}";
chsdi/static/css/extended.min.css: chsdi/static/less/extended.less
	@echo "${GREEN}Generating new css file...${RESET}";
	node_modules/.bin/lessc -ru --clean-css $< $@

.venv/last-github-last-commit::
	$(call cachelastvariable,$@,$(GITHUB_LAST_COMMIT),$(LAST_GITHUB_LAST_COMMIT),github-last-commit)

# application.wsg
.venv/last-modwsgi-config::
	$(call cachelastvariable,$@,$(MODWSGI_CONFIG),$(LAST_MODWSGI_CONFIG),MODWSGI-CONFIG)

# development.ini.in
.venv/last-version::
	$(call cachelastvariable,$@,$(VERSION),$(LAST_VERSION),version)

.venv/last-server-port::
	$(call cachelastvariable,$@,$(SERVER_PORT),$(LAST_SERVER_PORT),server-port)

# production.ini.in
.venv/last-current-directory::
	$(call cachelastvariable,$@,$(CURRENT_DIRECTORY),$(LAST_CURRENT_DIRECTORY),current-directory)

.venv/last-apache-base-path::
	$(call cachelastvariable,$@,$(APACHE_BASE_PATH),$(LAST_APACHE_BASE_PATH),apache-base-path)

.venv/last-apache-entry-path::
	$(call cachelastvariable,$@,$(APACHE_ENTRY_PATH),$(LAST_APACHE_ENTRY_PATH),apache-entry-path)

.venv/last-dbhost::
	$(call cachelastvariable,$@,$(DBHOST),$(LAST_DBHOST),dbhost)

.venv/last-dbport::
	$(call cachelastvariable,$@,$(DBPORT),$(LAST_DBPORT),dbport)

.venv/last-dbstaging::
	$(call cachelastvariable,$@,$(DBSTAGING),$(LAST_DBSTAGING),dbstaging)

.venv/last-geodata-staging::
	$(call cachelastvariable,$@,$(GEODATA_STAGING),$(LAST_GEODATA_STAGING),geodata-staging)

.venv/last-sphinxhost::
	$(call cachelastvariable,$@,$(SPHINXHOST),$(LAST_SPHINXHOST),sphinxhost)

.venv/last-wmshost::
	$(call cachelastvariable,$@,$(WMSHOST),$(LAST_WMSHOST),wmshost)

.venv/last-wmts-public-host::
	$(call cachelastvariable,$@,$(WMTS_PUBLIC_HOST),$(LAST_WMTS_PUBLIC_HOST),wmts-public-host)

.venv/last-geoadminhost::
	$(call cachelastvariable,$@,$(GEOADMINHOST),$(LAST_GEOADMINHOST),geoadminhost)

.venv/last-alti-url::
	$(call cachelastvariable,$@,$(ALTI_URL),$(LAST_ALTI_URL),alti-url)

.venv/last-api-url::
	$(call cachelastvariable,$@,$(API_URL),$(LAST_API_URL),api-url)

.venv/last-shop-url::
	$(call cachelastvariable,$@,$(SHOP_URL),$(LAST_SHOP_URL),shop-url)

.venv/last-host::
	$(call cachelastvariable,$@,$(HOST),$(LAST_HOST),host)

.venv/last-kml-temp-dir::
	$(call cachelastvariable,$@,$(KML_TEMP_DIR),$(LAST_KML_TEMP_DIR),kml_temp_dir)

.venv/last-http-proxy::
	$(call cachelastvariable,$@,$(HTTP_PROXY),$(LAST_HTTP_PROXY),http-proxy)

.venv/last-geoadmin-file-storage-bucket::
	$(call cachelastvariable,$@,$(GEOADMIN_FILE_STORAGE_BUCKET),$(LAST_GEOADMIN_FILE_STORAGE_BUCKET),geoadmin-file-storage-bucket)

.venv/last-geoadmin-file-storage-table-name::
	$(call cachelastvariable,$@,$(GEOADMIN_FILE_STORAGE_TABLE_NAME),$(LAST_GEOADMIN_FILE_STORAGE_TABLE_NAME),geoadmin-file-storage-table-name)

.venv/last-geoadmin-file-storage-table-region::
	$(call cachelastvariable,$@,$(GEOADMIN_FILE_STORAGE_TABLE_REGION),$(LAST_GEOADMIN_FILE_STORAGE_TABLE_REGION),geoadmin-file-storage-table-region)

.venv/last-glstyles-storage-table-name::
	$(call cachelastvariable,$@,$(GLSTYLES_STORAGE_TABLE_NAME),$(LAST_GLSTYLES_STORAGE_TABLE_NAME),glstyles-storage-table-name)

.venv/last-glstyles-storage-table-region::
	$(call cachelastvariable,$@,$(GLSTYLES_STORAGE_TABLE_REGION),$(LAST_GLSTYLES_STORAGE_TABLE_REGION),glstyles-storage-table-region)

.venv/last-public-bucket-host::
	$(call cachelastvariable,$@,$(PUBLIC_BUCKET_HOST),$(LAST_PUBLIC_BUCKET_HOST),public-bucket-host)

.venv/last-shortener-table-name::
	$(call cachelastvariable,$@,$(SHORTENER_TABLE_NAME),$(LAST_SHORTENER_TABLE_NAME),shortener-table-name)

.venv/last-shortener-table-region::
	$(call cachelastvariable,$@,$(SHORTENER_TABLE_REGION),$(LAST_SHORTENER_TABLE_REGION),shortener-table-region)

.venv/last-vector-bucket::
	$(call cachelastvariable,$@,$(VECTOR_BUCKET),$(LAST_VECTOR_BUCKET),vector-bucket)

.venv/last-datageoadminhost::
	$(call cachelastvariable,$@,$(DATAGEOADMINHOST),$(LAST_DATAGEOADMINHOST),datageoadminhost)

.venv/last-cmsgeoadminhost::
	$(call cachelastvariable,$@,$(CMSGEOADMINHOST),$(LAST_CMSGEOADMINHOST),cmsgeoadminhost)

.venv/last-linkeddatahost::
	$(call cachelastvariable,$@,$(LINKEDDATAHOST),$(LAST_LINKEDDATAHOST),linkeddatahost)

.venv/last-opentrans-api-key::
	$(call cachelastvariable,$@,$(OPENTRANS_API_KEY),$(LAST_OPENTRANS_API_KEY),opentrans-api-key)

.venv/last-shortener-allowed-domains::
	$(call cachelastvariable,$@,$(SHORTENER_ALLOWED_DOMAINS),$(LAST_SHORTENER_ALLOWED_DOMAINS),shortener-allowed-domains)

.venv/last-shortener-allowed-hosts::
	$(call cachelastvariable,$@,$(SHORTENER_ALLOWED_HOSTS),$(LAST_SHORTENER_ALLOWED_HOSTS),shortener-allowed-hosts)

.venv/last-dynamic-translation::
	$(call cachelastvariable,$@,$(DYNAMIC_TRANSLATION),$(LAST_DYNAMIC_TRANSLATION),dynamic-translation)

# wsgi.conf.in
.venv/last-robots-file::
	$(call cachelastvariable,$@,$(ROBOTS_FILE),$(LAST_ROBOTS_FILE),robots-file)

.venv/last-wsgi-threads::
	$(call cachelastvariable,$@,$(WSGI_THREADS),$(LAST_WSGI_THREADS),wsgi-threads)

.venv/last-branch-staging::
	$(call cachelastvariable,$@,$(BRANCH_STAGING),$(LAST_BRANCH_STAGING),branch-staging)

.venv/last-git-branch::
	$(call cachelastvariable,$@,$(GIT_BRANCH),$(LAST_GIT_BRANCH),git-branch)

.venv/last-deploy-target::
	$(call cachelastvariable,$@,$(DEPLOY_TARGET),$(LAST_DEPLOY_TARGET),deploy-target)

.venv/last-modwsgi-user::
	$(call cachelastvariable,$@,$(MODWSGI_USER),$(LAST_MODWSGI_USER),modewsgi-user)

.venv/last-cache-control::
	$(call cachelastvariable,$@,$(CACHE_CONTROL),$(LAST_CACHE_CONTROL),cache-control)

.venv/last-wsgi-user::
	$(call cachelastvariable,$@,$(WSGI_USER),$(LAST_WSGI_USER),wsgi-user)

.venv/last-wsgi-processes::
	$(call cachelastvariable,$@,$(WSGI_PROCESSES),$(LAST_WSGI_PROCESSES),wsgi-processes)

.venv/last-wsgi-threads::
	$(call cachelastvariable,$@,$(WSGI_THREADS),$(LAST_WSGI_THREADS),wsgi-threads)

.venv/last-wsgi-app::
	$(call cachelastvariable,$@,$(WSGI_APP),$(LAST_WSGI_APP),wsgi-app)

fixrights:
	@echo "${GREEN}Fixing rights...${RESET}";
	chgrp -f -R geodata . || :
	chmod -f -R g+srwX . || :

guard-%:
	@ if test "${${*}}" = ""; then \
	  echo "Environment variable $* not set. Add it to your command."; \
	  exit 1; \
	fi

.PHONY: clean
clean:
	rm -rf production.ini
	rm -rf development.ini
	rm -rf apache/wsgi.conf
	rm -rf app.log
	rm -rf apache/application.wsgi
	rm -rf deploy/deploy-branch.cfg
	rm -rf deploy/conf/00-branch.conf
	rm -f  chsdi/static/info.json
	rm -rf junit_report
	rm -f docker-compose.yml
	rm -f rancher-compose.yml
	rm -rf 25-mf-chsdi3.conf

.PHONY: cleanall
cleanall: clean
	rm -rf .venv
	rm -rf node_modules
	rm -rf .git/hooks/*
	rm -rf chsdi/static/css/extended.min.css
	rm -rf chsdi/locale/en/LC_MESSAGES/chsdi.*
	rm -rf chsdi/locale/fr/LC_MESSAGES/chsdi.*
	rm -rf chsdi/locale/de/LC_MESSAGES/chsdi.*
	rm -rf chsdi/locale/fi/LC_MESSAGES/chsdi.*
	rm -rf chsdi/locale/it/LC_MESSAGES/chsdi.*
	rm -rf chsdi/static/js/jquery.min.js
	rm -rf chsdi/static/js/blueimp-gallery.min.js
	rm -rf chsdi/static/js/d3.min.js
	rm -rf chsdi/static/js/d3-tip.js

.PHONY: pythonclean
pythonclean: cleanall
	rm -rf local
