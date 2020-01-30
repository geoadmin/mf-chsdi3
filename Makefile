SHELL = /bin/bash
.DEFAULT_GOAL := help

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
CURRENT_DIRECTORY := ${PWD}
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
CURRENT_DATE ?= $(shell date -u +"%Y-%m-%d %H:%M:%S %z")
NO_TESTS ?= withtests
NODE_DIRECTORY := node_modules
APACHE_ENTRY_PATH := $(shell if [ '$(APACHE_BASE_PATH)' = 'main' ]; then echo ''; else echo /$(APACHE_BASE_PATH); fi)
DATAGEOADMINHOST ?= data.geo.admin.ch
SHORTENER_ALLOWED_DOMAINS := admin.ch, swisstopo.ch, bgdi.ch
SHORTENER_ALLOWED_HOSTS ?=
PYPI_URL ?= https://pypi.org/simple/
GITHUB_LAST_COMMIT=$(shell curl -s  https://api.github.com/repos/geoadmin/mf-chsdi3/commits | jq -r '.[0].sha')

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
LAST_PUBLIC_BUCKET_HOST  := $(call lastvalue,public-bucket-host)
LAST_SHORTENER_ALLOWED_HOSTS := $(call lastvalue,allowed-hosts)
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
PYTHON_INSTALL_VERSION ?= 3.6.4

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
SYSTEM_PYTHON_CMD ?= $(CURRENT_DIR)/local/bin/python3

.PHONY: python
python: build/python
		@echo "Python installed"

local/bin/python3.6:
		mkdir -p $(CURRENT_DIRECTORY)/local;
		curl -z $(CURRENT_DIRECTORY)/local/Python-$(PYTHON_VERSION).tar.xz \
				https://www.python.org/ftp/python/$(PYTHON_VERSION)/Python-$(PYTHON_VERSION).tar.xz \
				-o $(CURRENT_DIRECTORY)/local/Python-$(PYTHON_VERSION).tar.xz;
		cd $(CURRENT_DIRECTORY)/local && tar -xf Python-$(PYTHON_VERSION).tar.xz && Python-$(PYTHON_VERSION)/configure --prefix=$(CURRENT_DIRECTORY)/local/   --with-ensurepip=install --enable-optimizations && make altinstall

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
	@echo


.PHONY: user
user:
	source $(USER_SOURCE) && make all

# TODO removed rss
.PHONY: all
all: setup chsdi/static/css/extended.min.css templates potomo lint fixrights doc

setup: .venv node_modules .venv/hooks

templates: apache/wsgi.conf apache/application.wsgi development.ini production.ini chsdi/static/info.json
	$(call build_templates,$(DEPLOY_TARGET)) 

.PHONY: baseimage
baseimage:
	docker build -t swisstopo/mf-chsdi3:base  -f Dockerfile.base .

.PHONY: image
image:
	docker build -t swisstopo/mf-chsdi3:python3.7  -f Dockerfile  .
	
.PHONY: environ
environ:
	$(call build_templates,$(DEPLOY_TARGET)) 

define build_templates
	export $(shell cat $1.env) && source rc_$1 \                                                                                                 
	envsubst < apache/wsgi.conf.in > apache/wsgi.conf && envsubst < rancher-compose.yml.in > rancher-compose.yml && \
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
	source rc_dev && ${PYTHON_CMD} scripts/translation2po.py chsdi/locale/;
	make potomo;

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
updatedev: .venv/last-GITHUB-LAST-COMMIT
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
           .venv/last-GIT-BRANCH \
           .venv/last-DEPLOY-TARGET \
           .venv/last-BRANCH-STAGING
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

apache/application.wsgi.mako:
	@echo "${GREEN}Template file apache/application.wsgi.mako has changed${RESET}";
apache/application.wsgi: apache/application.wsgi.mako \
                         .venv/last-CURRENT-DIRECTORY \
                         .venv/last-MODWSGI-CONFIG
apache/application.wsgi.in:
	@echo "${GREEN}Template file apache/application.wsgi.in has changed${RESET}";

apache/application.wsgi: apache/application.wsgi.in\
                         .venv/last-CURRENT-DIRECTORY \
                         .venv/last-MODWSGI-CONFIG
	@echo "${GREEN}Creating apache/application.wsgi...${RESET}";
	${ENVSUBST_CMD} < $< > $@

apache/wsgi.conf.in:
	@echo "${GREEN}Template file apache/wsgi.conf.in has changed${RESET}";
apache/wsgi.conf: apache/wsgi.conf.in \
                  apache/application.wsgi \
                  .venv/last-APACHE-BASE-PATH \
                  .venv/last-APACHE-ENTRY-PATH \
                  .venv/last-ROBOTS-FILE \
                  .venv/last-BRANCH-STAGING \
                  .venv/last-GIT-BRANCH \
                  .venv/last-CURRENT-DIRECTORY \
                  .venv/last-DEPLOY-TARGET \
                  .venv/last-MODWSGI-USER \
                  .venv/last-WSGI-PROCESSES \
                  .venv/last-WSGI-THREADS \
                  .venv/last-WSGI-APP \
                  .venv/last-KML-TEMP-DIR
	@echo "${GREEN}Creating apache/wsgi.conf...${RESET}";
	${ENVSUBST_CMD} < $< > $@


app.log:
	touch $@
	chmod a+rw $@


development.ini.in: app.log
	@echo "${GREEN}Template file development.ini.in has changed${RESET}";
development.ini: development.ini.in \
	               .venv/last-VERSION \
	               .venv/last-SERVER-PORT
	@echo "${GREEN}Creating development.ini....${RESET}";
	${ENVSUBST_CMD} <  $< > $@

production.ini.in:
	@echo "${GREEN}Template file production.ini.in has changed${RESET}";
production.ini: production.ini.in \
                .venv/last-VERSION \
                .venv/last-SERVER-PORT \
                .venv/last-APACHE-BASE-PATH \
                .venv/last-APACHE-ENTRY-PATH \
                .venv/last-CURRENT-DIRECTORY \
                .venv/last-DBHOST \
                .venv/last-DBPORT \
                .venv/last-DBSTAGING \
                .venv/last-ALTI-URL \
                .venv/last-API-URL \
                .venv/last-SHOP-URL \
                .venv/last-GEODATA-STAGING \
                .venv/last-SPHINXHOST \
                .venv/last-WMSHOST \
                .venv/last-WMTS-PUBLIC-HOST \
                .venv/last-GEOADMINHOST \
                .venv/last-HOST \
                .venv/last-KML-TEMP-DIR \
                .venv/last-HTTP-PROXY \
                .venv/last-GEOADMIN-FILE-STORAGE-BUCKET \
                .venv/last-PUBLIC-BUCKET-HOST \
                .venv/last-SHORTENER-ALLOWED-HOSTS \
                .venv/last-VECTOR-BUCKET \
                .venv/last-DATAGEOADMINHOST \
                .venv/last-CMSGEOADMINHOST \
                .venv/last-LINKEDDATAHOST \
                .venv/last-OPENTRANS-API-KEY \
                .venv/last-SHORTENER-ALLOWED-DOMAINS \
                guard-OPENTRANS_API_KEY
	@echo "${GREEN}Creating production.ini...${RESET}";
	${ENVSUBST_CMD} < $< > $@

.venv/hooks: .venv/bin/git-secrets ./scripts/install-git-hooks.sh
	@echo "${GREEN}Installing git hooks${RESET}";
	./scripts/install-git-hooks.sh
	touch $@

requirements.txt:
	@echo "${GREEN}File requirements.txt has changed${RESET}";

ifeq ($(USE_PYTHON3), 1)
.venv: requirements.txt
		test -d "$(INSTALL_DIRECTORY)" || $(SYSTEM_PYTHON_CMD) -m venv $(INSTALL_DIRECTORY); \
		${PIP_CMD} install --upgrade pip==19.2.3 setuptools --index-url ${PYPI_URL} ; 
		${PIP_CMD} install --index-url ${PYPI_URL}  -e .
else
.venv: requirements.txt
	@echo "${GREEN}Setting up virtual environement...${RESET}";
	@if [ ! -d $(INSTALL_DIRECTORY) ]; \
	then \
		virtualenv -p /usr/bin/python2  $(INSTALL_DIRECTORY); \
		${PIP_CMD} install --upgrade pip==19.2.3 setuptools==44.0.0 enum34==1.1.6 --index-url ${PYPI_URL} ; \
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
.venv/last-MODWSGI-CONFIG::
	$(call cachelastvariable,$@,$(MODWSGI_CONFIG),$(LAST_MODWSGI_CONFIG),MODWSGI-CONFIG)

# development.ini.in
.venv/last-VERSION::
	$(call cachelastvariable,$@,$(VERSION),$(LAST_VERSION),version)

.venv/last-SERVER-PORT::
	$(call cachelastvariable,$@,$(SERVER_PORT),$(LAST_SERVER_PORT),server-port)

# production.ini.in
.venv/last-CURRENT-DIRECTORY::
	$(call cachelastvariable,$@,$(CURRENT_DIRECTORY),$(LAST_CURRENT_DIRECTORY),current-directory)

.venv/last-APACHE-BASE-PATH::
	$(call cachelastvariable,$@,$(APACHE_BASE_PATH),$(LAST_APACHE_BASE_PATH),apache-base-path)

.venv/last-APACHE-ENTRY-PATH::
	$(call cachelastvariable,$@,$(APACHE_ENTRY_PATH),$(LAST_APACHE_ENTRY_PATH),apache-entry-path)

.venv/last-DBHOST::
	$(call cachelastvariable,$@,$(DBHOST),$(LAST_DBHOST),dbhost)

.venv/last-DBPORT::
	$(call cachelastvariable,$@,$(DBPORT),$(LAST_DBPORT),dbport)

.venv/last-DBSTAGING::
	$(call cachelastvariable,$@,$(DBSTAGING),$(LAST_DBSTAGING),dbstaging)

.venv/last-GEODATA-STAGING::
	$(call cachelastvariable,$@,$(GEODATA_STAGING),$(LAST_GEODATA_STAGING),geodata-staging)

.venv/last-SPHINXHOST::
	$(call cachelastvariable,$@,$(SPHINXHOST),$(LAST_SPHINXHOST),sphinxhost)

.venv/last-WMSHOST::
	$(call cachelastvariable,$@,$(WMSHOST),$(LAST_WMSHOST),wmshost)

.venv/last-WMTS-PUBLIC-HOST::
	$(call cachelastvariable,$@,$(WMTS_PUBLIC_HOST),$(LAST_WMTS_PUBLIC_HOST),wmts-public-host)

.venv/last-GEOADMINHOST::
	$(call cachelastvariable,$@,$(GEOADMINHOST),$(LAST_GEOADMINHOST),geoadminhost)

.venv/last-ALTI-URL::
	$(call cachelastvariable,$@,$(ALTI_URL),$(LAST_ALTI_URL),alti-url)

.venv/last-API-URL::
	$(call cachelastvariable,$@,$(API_URL),$(LAST_API_URL),api-url)

.venv/last-SHOP-URL::
	$(call cachelastvariable,$@,$(SHOP_URL),$(LAST_SHOP_URL),shop-url)

.venv/last-HOST::
	$(call cachelastvariable,$@,$(HOST),$(LAST_HOST),host)

.venv/last-KML-TEMP-DIR::
	$(call cachelastvariable,$@,$(KML_TEMP_DIR),$(LAST_KML_TEMP_DIR),kml_temp_dir)

.venv/last-HTTP-PROXY::
	$(call cachelastvariable,$@,$(HTTP_PROXY),$(LAST_HTTP_PROXY),http-proxy)

.venv/last-GEOADMIN-FILE-STORAGE-BUCKET::
	$(call cachelastvariable,$@,$(GEOADMIN_FILE_STORAGE_BUCKET),$(LAST_GEOADMIN_FILE_STORAGE_BUCKET),geoadmin-file-storage-bucket)

.venv/last-PUBLIC-BUCKET-HOST::
	$(call cachelastvariable,$@,$(PUBLIC_BUCKET_HOST),$(LAST_PUBLIC_BUCKET_HOST),public-bucket-host)

.venv/last-SHORTENER-ALLOWED-HOSTS::
	$(call cachelastvariable,$@,$(SHORTENER_ALLOWED_HOSTS),$(LAST_SHORTENER_ALLOWED_HOSTS),shortener-allowed-hosts)

.venv/last-VECTOR-BUCKET::
	$(call cachelastvariable,$@,$(VECTOR_BUCKET),$(LAST_VECTOR_BUCKET),vector-bucket)

.venv/last-DATAGEOADMINHOST::
	$(call cachelastvariable,$@,$(DATAGEOADMINHOST),$(LAST_DATAGEOADMINHOST),datageoadminhost)

.venv/last-CMSGEOADMINHOST::
	$(call cachelastvariable,$@,$(CMSGEOADMINHOST),$(LAST_CMSGEOADMINHOST),cmsgeoadminhost)

.venv/last-LINKEDDATAHOST::
	$(call cachelastvariable,$@,$(LINKEDDATAHOST),$(LAST_LINKEDDATAHOST),linkeddatahost)

.venv/last-OPENTRANS-API-KEY::
	$(call cachelastvariable,$@,$(OPENTRANS_API_KEY),$(LAST_OPENTRANS_API_KEY),opentrans-api-key)

.venv/last-SHORTENER-ALLOWED-DOMAINS::
	$(call cachelastvariable,$@,$(SHORTENER_ALLOWED_DOMAINS),$(LAST_SHORTENER_ALLOWED_DOMAINS),shortener-allowed-domains)

# wsgi.conf.in
.venv/last-ROBOTS-FILE::
	$(call cachelastvariable,$@,$(ROBOTS_FILE),$(LAST_ROBOTS_FILE),robots-file)

.venv/last-WSGI-THREADS::
	$(call cachelastvariable,$@,$(WSGI_THREADS),$(LAST_WSGI_THREADS),wsgi-threads)

.venv/last-BRANCH-STAGING::
	$(call cachelastvariable,$@,$(BRANCH_STAGING),$(LAST_BRANCH_STAGING),branch-staging)

.venv/last-GIT-BRANCH::
	$(call cachelastvariable,$@,$(GIT_BRANCH),$(LAST_GIT_BRANCH),git-branch)

.venv/last-DEPLOY-TARGET::
	$(call cachelastvariable,$@,$(DEPLOY_TARGET),$(LAST_DEPLOY_TARGET),deploy-target)

.venv/last-MODWSGI-USER::
	$(call cachelastvariable,$@,$(MODWSGI_USER),$(LAST_MODWSGI_USER),modewsgi-user)

.venv/last-CACHE-CONTROL::
	$(call cachelastvariable,$@,$(CACHE_CONTROL),$(LAST_CACHE_CONTROL),cache-control)

.venv/last-WSGI-USER::
	$(call cachelastvariable,$@,$(WSGI_USER),$(LAST_WSGI_USER),wsgi-user)

.venv/last-WSGI-PROCESSES::
	$(call cachelastvariable,$@,$(WSGI_PROCESSES),$(LAST_WSGI_PROCESSES),wsgi-processes)

.venv/last-WSGI-THREADS::
	$(call cachelastvariable,$@,$(WSGI_THREADS),$(LAST_WSGI_THREADS),wsgi-threads)

.venv/last-WSGI-APP::
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
	rm -f docker-compose.yml
	rm -f rancher-compose.yml

.PHONY: cleanall
cleanall: clean
	rm -rf .venv
	rm -rf node_modules
	rm -rf .git/hooks/*
	rm -rf chsdi/static/css/extended.min.css
	rm -rf chsdi/locale/en/LC_MESSAGES/chsdi.mo
	rm -rf chsdi/locale/fr/LC_MESSAGES/chsdi.mo
	rm -rf chsdi/locale/de/LC_MESSAGES/chsdi.mo
	rm -rf chsdi/locale/fi/LC_MESSAGES/chsdi.mo
	rm -rf chsdi/locale/it/LC_MESSAGES/chsdi.mo
	rm -rf chsdi/static/js/jquery.min.js
	rm -rf chsdi/static/js/blueimp-gallery.min.js
	rm -rf chsdi/static/js/d3.min.js
	rm -rf chsdi/static/js/d3-tip.js

.PHONY: pythonclean
pythonclean: cleanall
	rm -rf local
