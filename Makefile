SHELL = /bin/bash
# Variables
APACHE_BASE_PATH ?=
LAST_APACHE_BASE_PATH := $(shell if [ -f .venv/last-apache-base-path ]; then cat .venv/last-apache-base-path 2> /dev/null; else echo '-none-'; fi)
APACHE_ENTRY_PATH := $(shell if [ '$(APACHE_BASE_PATH)' = 'main' ]; then echo ''; else echo /$(APACHE_BASE_PATH); fi)
LAST_APACHE_ENTRY_PATH := $(shell if [ -f .venv/last-apache-entry-path ]; then cat .venv/last-apache-entry-path 2> /dev/null; else echo '-none-'; fi)
DBHOST ?=
LAST_DBHOST := $(shell if [ -f .venv/last-dbhost ]; then cat .venv/last-dbhost 2> /dev/null; else echo '-none-'; fi)
DBPORT ?=
LAST_DBPORT := $(shell if [ -f .venv/last-dbport ]; then cat .venv/last-dbport 2> /dev/null; else echo '-none-'; fi)
DBSTAGING ?=
LAST_DBSTAGING := $(shell if [ -f .venv/last-dbstaging ]; then cat .venv/last-dbstaging 2> /dev/null; else echo '-none-'; fi)
GEODATA_STAGING ?=
LAST_GEODATA_STAGING := $(shell if [ -f .venv/last-geodata-staging ]; then cat .venv/last-geodata-staging 2> /dev/null; else echo '-none-'; fi)
SPHINXHOST ?=
LAST_SPHINXHOST := $(shell if [ -f .venv/last-sphinxhost ]; then cat .venv/last-sphinxhost 2> /dev/null; else echo '-none-'; fi)
WMSHOST ?=
LAST_WMSHOST := $(shell if [ -f .venv/last-wmshost ]; then cat .venv/last-wmshost 2> /dev/null; else echo '-none-'; fi)
MAPPROXYHOST ?=
LAST_MAPPROXYHOST := $(shell if [ -f .venv/last-mapproxyhost ]; then cat .venv/last-mapproxyhost 2> /dev/null; else echo '-none-'; fi)
GEOADMINHOST ?=
LAST_GEOADMINHOST := $(shell if [ -f .venv/last-geoadminhost ]; then cat .venv/last-geoadminhost 2> /dev/null; else echo '-none-'; fi)
CMSGEOADMINHOST ?=
LAST_CMSGEOADMINHOST := $(shell if [ -f .venv/last-cmsgeoadminhost ]; then cat .venv/last-cmsgeoadminhost 2> /dev/null; else echo '-none-'; fi)
ALTI_URL ?=
LAST_ALTI_URL := $(shell if [ -f .venv/last-alti-url ]; then cat .venv/last-alti-url 2> /dev/null; else echo '-none-'; fi)
API_URL ?=
LAST_API_URL := $(shell if [ -f .venv/last-api-url ]; then cat .venv/last-api-url 2> /dev/null; else echo '-none-'; fi)
SHOP_URL ?=
LAST_SHOP_URL := $(shell if [ -f .venv/last-shop-url ]; then cat .venv/last-shop-url 2> /dev/null; else echo '-none-'; fi)
CURRENT_DIRECTORY ?=
LAST_CURRENT_DIRECTORY := $(shell if [ -f .venv/last-current-directory ]; then cat .venv/last-current-directory 2> /dev/null; else echo '-none-'; fi)
HOST ?=
LAST_HOST := $(shell if [ -f .venv/last-host ]; then cat .venv/last-host 2> /dev/null; else echo '-none-'; fi)
GEOADMIN_FILE_STORAGE_BUCKET ?=
LAST_GEOADMIN_FILE_STORAGE_BUCKET := $(shell if [ -f .venv/last-geoadmin-file-storage-bucket ]; then cat .venv/last-geoadmin-file-storage-bucket 2> /dev/null; else echo '-none-'; fi)
VECTOR_BUCKET ?=
LAST_VECTOR_BUCKET := $(shell if [ -f .venv/last-vector-bucket ]; then cat .venv/last-vector-bucket 2> /dev/null; else echo '-none-'; fi)
VECTOR_PROFILNAME ?=
LAST_VECTOR_PROFILNAME := $(shell if [ -f .venv/last-vector-profilname ]; then cat .venv/last-vector-profilname 2> /dev/null; else echo '-none-'; fi)
ROBOTS_FILE ?=
LAST_ROBOTS_FILE := $(shell if [ -f .venv/last-robots-file ]; then cat .venv/last-robots-file 2> /dev/null; else echo '-none-'; fi)
WSGI_THREADS ?=
LAST_WSGI_THREADS := $(shell if [ -f .venv/last-wsgi-threads ]; then cat .venv/last-wsgi-threads 2> /dev/null; else echo '-none-'; fi)
KEEP_VERSION ?= 'false'
LAST_VERSION := $(shell if [ -f '.venv/last-version' ]; then cat .venv/last-version 2> /dev/null; else echo '-none-'; fi)
VERSION := $(shell if [ '$(KEEP_VERSION)' = 'true' ] && [ '$(LAST_VERSION)' != '-none-' ]; then echo $(LAST_VERSION); else python -c "print __import__('time').strftime('%s')"; fi)
BRANCH_STAGING := $(shell if [ '$(DEPLOY_TARGET)' = 'dev' ]; then echo 'test'; else echo 'integration'; fi)
BRANCH_TO_DELETE :=
CURRENT_DIRECTORY := $(shell pwd)
DEPLOY_TARGET ?=
BODID ?=
WMSSCALELEGEND ?=
GIT_BRANCH := $(shell if [ -f '.venv/deployed-git-branch' ]; then cat .venv/deployed-git-branch 2> /dev/null; else git rev-parse --symbolic-full-name --abbrev-ref HEAD; fi)
HTTP_PROXY := http://ec2-52-28-118-239.eu-central-1.compute.amazonaws.com:80
LAST_HTTP_PPROXY := $(shell if [ -f .venv/last-kml-http-proxy ]; then cat .venv/last-http-proxy 2> /dev/null; else echo '-none-'; fi)
INSTALL_DIRECTORY := .venv
KML_TEMP_DIR := /var/local/print/kml
LAST_KML_TEMP_DIR := $(shell if [ -f .venv/last-kml-temp-dir ]; then cat .venv/last-kml-temp-dir 2> /dev/null; else echo '-none-'; fi)
MODWSGI_USER := www-data
LAST_MODWSGI_USER := $(shell if [ -f .venv/last-modwsgi-user ]; then cat .venv/last-modwsgi-user 2> /dev/null; else echo '-none-'; fi)
NO_TESTS ?= withtests
NODE_DIRECTORY := node_modules
PYTHON_FILES := $(shell find chsdi/* -path chsdi/static -prune -o -type f -name "*.py" -print)
SHORTENER_ALLOWED_DOMAINS := admin.ch, swisstopo.ch, bgdi.ch
LAST__SHORTENER_ALLOWED_DOMAINS := $(shell if [ -f .venv/last-shortener-allowed-domains ]; then cat .venv/last-shortener-allowed-domains 2> /dev/null; else echo '-none-'; fi)
SHORTENER_ALLOWED_HOSTS :=
LAST_SHORTENER_ALLOWED_HOSTS := $(shell if [ -f .venv/last-shortener-allowed-hosts ]; then cat .venv/last-shortener-allowed-hosts 2> /dev/null; else echo '-none-'; fi)
TEMPLATE_FILES := $(shell find -type f -name "*.in" -print)
USER_SOURCE ?= rc_user
WSGI_APP := $(CURRENT_DIRECTORY)/apache/application.wsgi
LAST_WSGI_APP := $(shell if [ -f .venv/last-wsgi-app ]; then cat .venv/last-wsgi-app 2> /dev/null; else echo '-none-'; fi)
DATAGEOADMINHOST ?= data.geo.admin.ch
LAST_DATAGEOADMINHOST := $(shell if [ -f .venv/last-datageoadminhost ]; then cat .venv/last-datageoadminhost 2> /dev/null; else echo '-none-'; fi)

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

# Linting rules
PEP8_IGNORE := "E128,E221,E241,E251,E272,E305,E501,E711,E731"

# E128: continuation line under-indented for visual indent
# E221: multiple spaces before operator
# E241: multiple spaces after ':'
# E251: multiple spaces around keyword/parameter equals
# E272: multiple spaces before keyword
# E501: line length 79 per default
# E711: comparison to None should be 'if cond is None:' (SQLAlchemy's filter syntax requires this ignore!)
# E731: do not assign a lambda expression, use a def

# Colors
RESET := $(shell tput sgr0)
RED := $(shell tput setaf 1)
GREEN := $(shell tput setaf 2)

# Versions
# We need GDAL which is hard to install in a venv, modify PYTHONPATH to use the
# system wide version.
GDAL_VERSION ?= 1.10.0
PYTHON_VERSION := $(shell python --version 2>&1 | cut -d ' ' -f 2 | cut -d '.' -f 1,2)
PYTHONPATH ?= .venv/lib/python${PYTHON_VERSION}/site-packages:/usr/lib64/python${PYTHON_VERSION}/site-packages

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
	@echo "- deletebranch       List deployed branches or delete a deployed branch (BRANCH_TO_DELETE=...)"
	@echo "- updateapi          Updates geoadmin api source code (ol3 fork)"
	@echo "- deploydev          Deploys master to dev (SNAPSHOT=true to also create a snapshot)"
	@echo "- deployint          Deploys a snapshot to integration (SNAPSHOT=201512021146)"
	@echo "- deployprod         Deploys a snapshot to production (SNAPSHOT=201512021146)"
	@echo "- clean              Remove generated files"
	@echo "- cleanall           Remove all the build artefacts"
	@echo
	@echo "Variables:"
	@echo "APACHE_ENTRY_PATH:   ${APACHE_ENTRY_PATH}"
	@echo "API_URL:             ${API_URL}"
	@echo "WMSHOST:             ${WMSHOST}"
	@echo "BRANCH_STAGING:      ${BRANCH_STAGING}"
	@echo "DBHOST:              ${DBHOST}"
	@echo "DBSTAGING:           ${DBSTAGING}"
	@echo "GEOADMINHOST:        ${GEOADMINHOST}"
	@echo "GIT_BRANCH:          ${GIT_BRANCH}"
	@echo "SERVER_PORT:         ${SERVER_PORT}"
	@echo


.PHONY: user
user:
	source $(USER_SOURCE) && make all

.PHONY: all
all: setup chsdi/static/css/extended.min.css templates potomo rss lint fixrights

setup: .venv node_modules .venv/hooks

templates: .venv/last-version apache/wsgi.conf development.ini production.ini

.PHONY: dev
dev:
	source rc_dev && make all

.PHONY: int
int:
	source rc_int && make all

.PHONY: prod
prod:
	source rc_prod && make all

.PHONY: serve
serve:
	PYTHONPATH=${PYTHONPATH} ${PSERVE_CMD} development.ini --reload

.PHONY: shell
shell:
	PYTHONPATH=${PYTHONPATH} ${PSHELL_CMD} development.ini

.PHONY: test
test:
	PYTHONPATH=${PYTHONPATH} ${NOSE_CMD} chsdi/tests/ -e .*e2e.*

.PHONY: teste2e
teste2e:
	PYTHONPATH=${PYTHONPATH} ${NOSE_CMD} chsdi/tests/e2e/

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

.PHONY: updateapi
updateapi:
	@echo "${GREEN}Updating geoadmin API...${RESET}";
	rm -rf chsdi/static/js/ol3 && \
	cd chsdi/static/js/ && \
	git clone https://github.com/geoadmin/ol3.git && \
	cd ol3 && \
	git remote add upstream https://github.com/openlayers/ol3 && \
	git fetch upstream && \
	npm install && \
	API_URL=$(API_URL) make -f Makefile-ga build-ga && \
	cp build/ga.css ../../css/ && \
	cp build/ga*.js ../../js/ && \
	cp resources/EPSG* ../../js/;

.PHONY: deploybranch
deploybranch:
	@echo "${GREEN}Deploying branch $(GIT_BRANCH) to dev...${RESET}";
	./scripts/deploybranch.sh

.PHONY: deletebranch
deletebranch:
	./scripts/delete_branch.sh $(BRANCH_TO_DELETE)

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

.PHONY: deployint
deployint: guard-SNAPSHOT
	scripts/deploysnapshot.sh $(SNAPSHOT) int $(NO_TESTS)

.PHONY: deployprod
deployprod: guard-SNAPSHOT
	scripts/deploysnapshot.sh $(SNAPSHOT) prod $(NO_TESTS)

.PHONY: legends
legends: guard-BODID guard-WMSHOST
	source rc_user && scripts/downloadlegends.sh $(WMSHOST) $(BODID) $(WMSSCALELEGEND)

rc_branch.mako:
	@echo "${GREEN}Branch has changed${RESET}";
rc_branch: rc_branch.mako
	@echo "${GREEN}Creating branch template...${RESET}"
	${MAKO_CMD} \
		--var "git_branch=$(GIT_BRANCH)" \
		--var "deploy_target=$(DEPLOY_TARGET)" \
		--var "branch_staging=$(BRANCH_STAGING)" $< > $@

deploy/deploy-branch.cfg.in:
	@echo "${GREEN]}Template file deploy/deploy-branch.cfg.in has changed${RESET}";
deploy/deploy-branch.cfg: deploy/deploy-branch.cfg.in
	@echo "${GREEN}Creating deploy/deploy-branch.cfg...${RESET}";
	${MAKO_CMD} --var "git_branch=$(GIT_BRANCH)" $< > $@

deploy/conf/00-branch.conf.in:
	@echo "${GREEN}Templat file deploy/conf/00-branch.conf.in has changed${RESET}";
deploy/conf/00-branch.conf: deploy/conf/00-branch.conf.in
	@echo "${GREEN}Creating deploy/conf/00-branch.conf...${RESET}"
	${MAKO_CMD} --var "git_branch=$(GIT_BRANCH)" $< > $@

apache/application.wsgi.mako:
	@echo "${GREEN}Template file apache/application.wsgi.mako has changed${RESET}";
apache/application.wsgi: apache/application.wsgi.mako
	@echo "${GREEN}Creating apache/application.wsgi...${RESET}";
	${MAKO_CMD} \
		--var "current_directory=$(CURRENT_DIRECTORY)" \
		--var "modwsgi_config=$(MODWSGI_CONFIG)" $< > $@

apache/wsgi.conf.in:
	@echo "${GREEN}Template file apache/wsgi.conf.in has changed${RESET}";
apache/wsgi.conf: apache/wsgi.conf.in \
                  apache/application.wsgi \
                  .venv/last-apache-base-path \
                  .venv/last-apache-entry-path \
                  .venv/last-robots-file \
                  .venv/last-current-directory \
                  .venv/last-modwsgi-user \
                  .venv/last-wsgi-threads \
                  .venv/last-wsgi-app \
                  .venv/last-kml_temp_dir
	@echo "${GREEN}Creating apache/wsgi.conf...${RESET}";
	${MAKO_CMD} \
		--var "apache_base_path=$(APACHE_BASE_PATH)" \
		--var "apache_entry_path=$(APACHE_ENTRY_PATH)" \
		--var "robots_file=$(ROBOTS_FILE)" \
		--var "branch_staging=$(BRANCH_STAGING)" \
		--var "git_branch=$(GIT_BRANCH)" \
		--var "current_directory=$(CURRENT_DIRECTORY)" \
		--var "modwsgi_user=$(MODWSGI_USER)" \
		--var "wsgi_threads=$(WSGI_THREADS)" \
		--var "wsgi_app=$(WSGI_APP)" \
		--var "kml_temp_dir=$(KML_TEMP_DIR)" $< > $@

development.ini.in:
	@echo "${GREEN}Template file development.ini.in has changed${RESET}";
development.ini: development.ini.in
	@echo "${GREEN}Creating development.ini....${RESET}";
	${MAKO_CMD} \
		--var "app_version=$(VERSION)" \
		--var "server_port=$(SERVER_PORT)" $< > $@

production.ini.in:
	@echo "${GREEN}Template file production.ini.in has changed${RESET}";
production.ini: production.ini.in \
                .venv/last-apache-base-path \
                .venv/last-apache-entry-path \
                .venv/last-dbhost \
                .venv/last-dbport \
                .venv/last-dbstaging \
                .venv/last-geodata-staging \
                .venv/last-sphinxhost \
                .venv/last-wmshost \
                .venv/last-mapproxyhost \
                .venv/last-geoadminhost \
                .venv/last-cmsgeoadminhost \
                .venv/last-alti-url \
                .venv/last-api-url \
                .venv/last-shop-url \
                .venv/last-current-directory \
                .venv/last-host \
                .venv/last-kml-temp-dir \
                .venv/last-http-proxy \
                .venv/last-geoadmin-file-storage-bucket \
                .venv/last-vector-bucket \
                .venv/last-vector-profilname \
                .venv/last-datageoadminhost \
                .venv/last-shortener-allowed-hosts \
                .venv/last-shortener-allowed-domains
	@echo "${GREEN}Creating production.ini...${RESET}";
	${MAKO_CMD} \
		--var "app_version=$(VERSION)" \
		--var "server_port=$(SERVER_PORT)" \
		--var "apache_base_path=$(APACHE_BASE_PATH)" \
		--var "apache_entry_path=$(APACHE_ENTRY_PATH)" \
		--var "current_directory=$(CURRENT_DIRECTORY)" \
		--var "dbhost=$(DBHOST)" \
		--var "dbport=$(DBPORT)" \
		--var "dbstaging=$(DBSTAGING)" \
		--var "alti_url=$(ALTI_URL)" \
		--var "api_url=$(API_URL)" \
		--var "shop_url=$(SHOP_URL)" \
		--var "geodata_staging=$(GEODATA_STAGING)" \
		--var "sphinxhost=$(SPHINXHOST)" \
		--var "wmshost=$(WMSHOST)" \
		--var "mapproxyhost=$(MAPPROXYHOST)" \
		--var "geoadminhost=$(GEOADMINHOST)" \
		--var "host=$(HOST)" \
		--var "kml_temp_dir=$(KML_TEMP_DIR)" \
		--var "http_proxy=$(HTTP_PROXY)" \
		--var "geoadmin_file_storage_bucket=$(GEOADMIN_FILE_STORAGE_BUCKET)" \
		--var "shortener_allowed_hosts=$(SHORTENER_ALLOWED_HOSTS)" \
		--var "vector_bucket=$(VECTOR_BUCKET)" \
		--var "vector_profilename=$(VECTOR_PROFILENAME)" \
		--var "datageoadminhost=$(DATAGEOADMINHOST)" \
		--var "cmsgeoadminhost=$(CMSGEOADMINHOST)" \
		--var "shortener_allowed_domains=$(SHORTENER_ALLOWED_DOMAINS)" $< > $@

.venv/hooks: .venv/bin/git-secrets ./scripts/install-git-hooks.sh
	@echo "${GREEN}Installing git hooks${RESET}";
	./scripts/install-git-hooks.sh
	touch $@

requirements.txt:
	@echo "${GREEN}File requirements.txt has changed${RESET}";
.venv: requirements.txt
	@echo "${GREEN}Setting up virtual environement...${RESET}";
	@if [ ! -d $(INSTALL_DIRECTORY) ]; \
	then \
		virtualenv $(INSTALL_DIRECTORY); \
		${PIP_CMD} install -U pip setuptools; \
	fi
	${PIP_CMD} install --find-links local_eggs/ -e .

.venv/bin/git-secrets: .venv
	@echo "${GREEN}Installing git secrets${RESET}";
	if [ ! -d ".git" ]; then git init; fi
	rm -rf .venv/git-secrets
	git clone https://github.com/awslabs/git-secrets .venv/git-secrets
	cd .venv/git-secrets && make install PREFIX=..
	(git config --local --get-regexp secret && git config --remove-section secrets) || cd
	.venv/bin/git-secrets --register-aws

.venv/last-version::
	mkdir -p $(dir $@)
	test $(VERSION) != $(LAST_VERSION) && echo $(VERSION) > .venv/last-version || :

package.json:
	@echo "${GREEN}File package.json has changed${RESET}";
node_modules: package.json
	@echo "${GREEN}Installing node packages...${RESET}";
	npm install
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

.venv/last-apache-base-path::
	mkdir -p $(dir $@)
	test "$(APACHE_BASE_PATH)" != "$(LAST_APACHE_BASE_PATH)" && \
	    echo $(APACHE_BASE_PATH) > .venv/last-apache-base-path || :

.venv/last-apache-entry-path::
	mkdir -p $(dir $@)
	test "$(APACHE_ENTRY_PATH)" != "$(LAST_APACHE_ENTRY_PATH)" && \
	    echo $(APACHE_ENTRY_PATH) > .venv/last-apache-entry-path || :

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
	rm -rf rc_branch
	rm -rf apache/application.wsgi
	rm -rf deploy/deploy-branch.cfg
	rm -rf deploy/conf/00-branch.conf

.PHONY: cleanall
cleanall: clean
	rm -rf .venv
	rm -rf node_modules
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
