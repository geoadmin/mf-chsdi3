# Variables
APACHE_ENTRY_PATH := $(shell if [ '$(APACHE_BASE_PATH)' = 'main' ]; then echo ''; else echo /$(APACHE_BASE_PATH); fi)
APP_VERSION := $(shell python -c "print __import__('time').strftime('%s')")
BASEWAR := print-servlet-3.3-SNAPSHOT.war
BRANCH_STAGING := $(shell if [ '$(DEPLOY_TARGET)' = 'dev' ]; then echo 'test'; else echo 'integration'; fi)
BRANCH_TO_DELETE :=
CURRENT_DIRECTORY := $(shell pwd)
DEPLOYCONFIG ?=
DEPLOY_TARGET ?=
GIT_BRANCH := $(shell if [ -f '.venv/deployed-git-branch' ]; then cat .venv/deployed-git-branch 2> /dev/null; else git rev-parse --symbolic-full-name --abbrev-ref HEAD; fi)
HTTP_PROXY := http://ec2-52-28-118-239.eu-central-1.compute.amazonaws.com:80
INSTALL_DIRECTORY := .venv
MODWSGI_USER := www-data
NO_TESTS ?= withtests
NODE_DIRECTORY := node_modules
PRINT_INPUT := *.yaml *.png WEB-INF
PRINT_OUTPUT_BASE := /srv/tomcat/tomcat1/webapps/print-chsdi3-$(APACHE_BASE_PATH)
PRINT_OUTPUT := $(PRINT_OUTPUT_BASE).war
PRINT_TEMP_DIR := /var/cache/print
PYTHON_FILES := $(shell find chsdi/* -path chsdi/static -prune -o -type f -name "*.py" -print)
SHORTENER_ALLOWED_DOMAINS := admin.ch, swisstopo.ch, bgdi.ch
SHORTENER_ALLOWED_HOSTS :=
TEMPLATE_FILES := $(shell find -type f -name "*.in" -print)
USERNAME := $(shell whoami)
WSGI_APP := $(CURRENT_DIRECTORY)/apache/application.wsgi
ZADARA_DIR := /var/local/cartoweb/downloads/

# Commands
AUTOPEP8_CMD := $(INSTALL_DIRECTORY)/bin/autopep8
FLAKE8_CMD := $(INSTALL_DIRECTORY)/bin/flake8
MAKO_CMD := $(INSTALL_DIRECTORY)/bin/mako-render
NOSE_CMD := $(INSTALL_DIRECTORY)/bin/nosetests
PIP_CMD := $(INSTALL_DIRECTORY)/bin/pip
PSERVE_CMD := $(INSTALL_DIRECTORY)/bin/pserve
PYTHON_CMD := $(INSTALL_DIRECTORY)/bin/python
SPHINX_CMD := $(INSTALL_DIRECTORY)/bin/sphinx-build

# Linting rules
PEP8_IGNORE := "E128,E221,E241,E251,E272,E501,E711,E731"

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
GDAL_VERSION ?= 1.9.0
PYTHON_VERSION := $(shell python --version 2>&1 | cut -d ' ' -f 2 | cut -d '.' -f 1,2)
PYTHONPATH ?= .venv/lib/python${PYTHON_VERSION}/site-packages:/usr/lib64/python${PYTHON_VERSION}/site-packages

.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Possible targets:"
	@echo "- all                Build the app"
	@echo "- user               Build the user specific version of the app"
	@echo "- serve              Serve the application with pserve"
	@echo "- test               Launch the tests (no e2e tests)"
	@echo "- teste2e            Launch end-to-end tests"
	@echo "- lint               Run the linter"
	@echo "- autolint           Run the autolinter"
	@echo "- translate          Generate the translation files"
	@echo "- doc                Generate the doc for api3.geo.admin.ch"
	@echo "- deploybranch       Deploy current branch to dev (must be pushed before hand)"
	@echo "- deploybranchint    Deploy current branch to dev and int (must be pushed before hand)"
	@echo "- deploybranchdemo   Deploy current branch to dev and demo (must be pushed before hand)"
	@echo "- deletebranch       List deployed branches or delete a deployed branch (BRANCH_TO_DELETE=...)"
	@echo "- updateapi          Updates geoadmin api source code (ol3 fork)"
	@echo "- printconfig        Set tomcat print env variables"
	@echo "- printwar           Creates the .jar print file (only one per env per default)"
	@echo "- deploydev          Deploys master to dev (SNAPSHOT=true to also create a snapshot)"
	@echo "- deployint          Deploys a snapshot to integration (SNAPSHOT=201512021146)"
	@echo "- deployprod         Deploys a snapshot to production (SNAPSHOT=201512021146)"
	@echo "- clean              Remove generated files"
	@echo "- cleanall           Remove all the build artefacts"
	@echo
	@echo "Variables:"
	@echo "APACHE_ENTRY_PATH:   ${APACHE_ENTRY_PATH}"
	@echo "API_URL:             ${API_URL}"
	@echo "BRANCH_STAGING:      ${BRANCH_STAGING}"
	@echo "DBHOST:              ${DBHOST}"
	@echo "DBSTAGING:           ${DBSTAGING}"
	@echo "GEOADMINHOST:        ${GEOADMINHOST}"
	@echo "GIT_BRANCH:          ${GIT_BRANCH}"
	@echo "SERVER_PORT:         ${SERVER_PORT}"
	@echo "PRINT_WAR:           ${PRINT_WAR}"
	@echo

.PHONY: all
all: setup chsdi/static/css/extended.min.css templates potomo rss lint fixrights

setup: .venv gdal node_modules

templates: apache/wsgi.conf apache/tomcat-print.conf print/WEB-INF/web.xml development.ini production.ini

.PHONY: user
user:
	./scripts/build.sh $(USERNAME)

.PHONY: dev
dev:
	./scripts/build.sh dev

.PHONY: int
int:
	./scripts/build.sh int

.PHONY: prod
prod:
	./scripts/build.sh prod

.PHONY: serve
serve:
	PYTHONPATH=${PYTHONPATH} ${PSERVE_CMD} development.ini --reload

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
	cd chsdi/static/doc && ../../../${SPHINX_CMD} -b html source build

.PHONY:
rss: doc chsdi/static/doc/build/releasenotes/index.html
	@echo "${GREEN}Creating the rss feed from releasenotes${RESET}";
	${PYTHON_CMD} scripts/rssFeedGen.py

.PHONY: translate
translate:
	@echo "${GREEN}Updating translations...${RESET}";
	${PYTHON_CMD} translations/translation2po.py chsdi/locale/;

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

.PHONY: gdal
gdal: .venv
	@if [ ! -d $(INSTALL_DIRECTORY)/build ]; \
	then \
		echo "${GREEN}Installing GDAL...${RESET}"; \
		mkdir -p $(INSTALL_DIRECTORY)/build && \
		${PIP_CMD} install --download $(INSTALL_DIRECTORY)/build GDAL==$(GDAL_VERSION) && \
		cd $(INSTALL_DIRECTORY)/build && \
		tar -xzf GDAL-$(GDAL_VERSION).tar.gz && \
		cd GDAL-$(GDAL_VERSION) && \
		../../../${PYTHON_CMD} setup.py build_ext --gdal-config=/usr/bin/gdal-config-64 --library-dirs=/usr/lib --include-dirs=/usr/include/gdal && \
		../../../${PYTHON_CMD} setup.py install --root / && \
		cd ../../.. && \
		${PYTHON_CMD} -c "from osgeo import gdal; print('GDAL installed'); print(gdal.__version__, gdal.__file__)"; \
	fi

.PHONY: updateapi
updateapi:
	@echo "${GREEN}Updating geoadmin API...${RESET}";
	rm -rf chsdi/static/js/ol3 && \
	cd chsdi/static/js/ && \
	git clone https://github.com/geoadmin/ol3.git && \
	cd chsdi/static/js/ol3 && \
	git remote add upstream https://github.com/openlayers/ol3 && \
	git fetch upstream && \
	npm install && \
	API_URL=$(API_URL) make -f Makefile-ga build-ga && \
	make -f Makefile-ga build-ga chsdi/static/css/ && \
	cp build/ga.css chsdi/static/css/ && \
	cp build/ga*.js chsdi/static/js/ && \
	cp resources/EPSG* chsdi/static/js/

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

.PHONY: deploybranchdemo
deploybranchdemo:
	@echo "${GREEN}Deploying branch $(GIT_BRANCH) to dev and demo...${RESET}";
	./scripts/deploybranch.sh demo

.PHONY: printconfig
printconfig:
	@echo '# File managed by zc.buildout mf-chsdi3'  > /srv/tomcat/tomcat1/bin/setenv-local.sh
	@echo 'export JAVA_XMX="2G"'  >> /srv/tomcat/tomcat1/bin/setenv-local.sh

.PHONY: printwar
printwar: printconfig print/WEB-INF/web.xml.in
	cd print && \
	mkdir temp_$(APP_VERSION) && \
	echo "${GREEN}Updating print war...${RESET}" && \
	cp -f ${BASEWAR} temp_$(APP_VERSION)/print-chsdi3-$(APACHE_BASE_PATH).war && \
	cp -fr ${PRINT_INPUT} temp_$(APP_VERSION)/ && \
	cd temp_$(APP_VERSION) && \
	jar uf print-chsdi3-$(APACHE_BASE_PATH).war ${PRINT_INPUT} && \
	echo "${GREEN}Print war creation was successful.${RESET}" && \
	rm -rf $(PRINT_OUTPUT) $(PRINT_OUTPUT_BASE) && \
	cp -f print-chsdi3-$(APACHE_BASE_PATH).war $(PRINT_OUTPUT) && chmod 666 $(PRINT_OUTPUT) && cd .. && \
	echo "${GREEN}Removing temp directory${RESET}" && \
	rm -rf temp_$(APP_VERSION) && \
	echo "${GREEN}Restarting tomcat...${RESET}" && \
	sudo /etc/init.d/tomcat-tomcat1 restart && \
	echo "${GREEN}It may take a few seconds for $(PRINT_OUTPUT_BASE) directory to appear...${RESET}";

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
deployint:
	scripts/deploysnapshot.sh $(SNAPSHOT) int $(NO_TESTS) $(DEPLOYCONFIG)

.PHONY: deployprod
deployprod:
	scripts/deploysnapshot.sh $(SNAPSHOT) prod $(NO_TESTS) $(DEPLOYCONFIG)

.PHONY: deploydemo
deploydemo:
	scritps/deploysnapshot.sh $(SNAPSHOT) demo

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

apache/tomcat-print.conf.in:
	@echo "${GREEN}Template file apache/tomcat-print.conf.in has changed${RESET}";
apache/tomcat-print.conf: apache/tomcat-print.conf.in
	@echo "${GREEN}Creating apache/tomcat-print.conf...${RESET}";
	${MAKO_CMD} \
		--var "print_war=$(PRINT_WAR)" \
		--var "apache_entry_path=$(APACHE_ENTRY_PATH)" \
		--var "print_temp_dir=$(PRINT_TEMP_DIR)" $< > $@

print/WEB-INF/web.xml.in:
	@echo "${GREEN}Template file print/WEB-INF/web.xml has changed${RESET}"
print/WEB-INF/web.xml: print/WEB-INF/web.xml.in
	@echo "${GREEN}Creating print/WEB-INF/web.xml...${RESET}"
	${MAKO_CMD} \
		--var "print_temp_dir=$(PRINT_TEMP_DIR)" $< > $@

apache/application.wsgi.mako:
	@echo "${GREEN}Template file apache/application.wsgi.mako has changed${RESET}";
apache/application.wsgi: apache/application.wsgi.mako
	@echo "${GREEN}Creating apache/application.wsgi...${RESET}";
	${MAKO_CMD} \
		--var "current_directory=$(CURRENT_DIRECTORY)" \
		--var "apache_base_path=$(APACHE_BASE_PATH)" \
		--var "modwsgi_config=$(MODWSGI_CONFIG)" $< > $@

apache/wsgi.conf.in:
	@echo "${GREEN}Template file apache/wsgi.conf.in has changed${RESET}";
apache/wsgi.conf: apache/wsgi.conf.in apache/application.wsgi
	@echo "${GREEN}Creating apache/wsgi.conf...${RESET}";
	${MAKO_CMD} \
		--var "app_version=$(APP_VERSION)" \
		--var "apache_entry_path=$(APACHE_ENTRY_PATH)" \
		--var "apache_base_path=$(APACHE_BASE_PATH)" \
		--var "robots_file=$(ROBOTS_FILE)" \
		--var "branch_staging=$(BRANCH_STAGING)" \
		--var "git_branch=$(GIT_BRANCH)" \
		--var "current_directory=$(CURRENT_DIRECTORY)" \
		--var "modwsgi_user=$(MODWSGI_USER)" \
		--var "wsgi_threads=$(WSGI_THREADS)" \
		--var "wsgi_app=$(WSGI_APP)" \
		--var "zadara_dir=$(ZADARA_DIR)" \
		--var "print_temp_dir=$(PRINT_TEMP_DIR)" $< > $@

development.ini.in:
	@echo "${GREEN}Template file development.ini.in has changed${RESET}";
development.ini: development.ini.in
	@echo "${GREEN}Creating development.ini....${RESET}";
	${MAKO_CMD} \
		--var "app_version=$(APP_VERSION)" \
		--var "server_port=$(SERVER_PORT)" $< > $@

production.ini.in:
	@echo "${GREEN}Template file production.ini.in has changed${RESET}";
production.ini: production.ini.in
	@echo "${GREEN}Creating production.ini...${RESET}";
	${MAKO_CMD} \
		--var "app_version=$(APP_VERSION)" \
		--var "server_port=$(SERVER_PORT)" \
		--var "apache_entry_path=$(APACHE_ENTRY_PATH)" \
		--var "apache_base_path=$(APACHE_BASE_PATH)" \
		--var "current_directory=$(CURRENT_DIRECTORY)" \
		--var "dbhost=$(DBHOST)" \
		--var "dbport=$(DBPORT)" \
		--var "dbstaging=$(DBSTAGING)" \
		--var "zadara_dir=$(ZADARA_DIR)" \
		--var "api_url=$(API_URL)" \
		--var "geodata_staging=$(GEODATA_STAGING)" \
		--var "sphinxhost=$(SPHINXHOST)" \
		--var "wmshost=$(WMSHOST)" \
		--var "webdav_host=$(WEBDAV_HOST)" \
		--var "mapproxyhost=$(MAPPROXYHOST)" \
		--var "geoadminhost=$(GEOADMINHOST)" \
		--var "host=$(HOST)" \
		--var "print_temp_dir=$(PRINT_TEMP_DIR)" \
		--var "http_proxy=$(HTTP_PROXY)" \
		--var "geoadmin_file_storage_bucket=$(GEOADMIN_FILE_STORAGE_BUCKET)" \
		--var "shortener_allowed_hosts=$(SHORTENER_ALLOWED_HOSTS)" \
		--var "shortener_allowed_domains=$(SHORTENER_ALLOWED_DOMAINS)" $< > $@

requirements.txt:
	@echo "${GREEN}File requirements.txt has changed${RESET}";
.venv: requirements.txt
	@echo "${GREEN}Setting up virtual environement...${RESET}";
	@if [ ! -d $(INSTALL_DIRECTORY) ]; \
	then \
		virtualenv $(INSTALL_DIRECTORY); \
		${PIP_CMD} install -U pip; \
	fi
	${PYTHON_CMD} setup.py develop
	${PIP_CMD} install Pillow==3.1.0

package.json:
	@echo "${GREEN}File package.json has changed${RESET}";
node_modules: package.json
	@echo "${GREEN}Installing node packages...${RESET}";
	npm install

chsdi/static/less/extended.less:
	@echo "${GREEN}File chsdi/static/less/extended.less has changed${RESET}";
chsdi/static/css/extended.min.css: chsdi/static/less/extended.less
	@echo "${GREEN}Generating new css file...${RESET}";
	node_modules/.bin/lessc -ru --clean-css $< $@

fixrights:
	@echo "${GREEN}Fixing rights...${RESET}";
	chgrp -f -R geodata . || :
	chmod -f -R g+srwX . || :

.PHONY: clean
clean:
	rm -rf production.ini
	rm -rf development.ini
	rm -rf apache/wsgi.conf
	rm -rf apache/tomcat-print.conf
	rm -rf print/WEB-INF/web.xml
	rm -rf apache/application.wsgi
	rm -rf rc_branch
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
