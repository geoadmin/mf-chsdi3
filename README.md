# mf-chsdi3

| Branch | Status |
|---|---|
| master | ![Build Status](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiUytMYkh3RStzRFBjQ0JVaDRubUFRU2UvUEEyeWVaZTNtaDNncWNKbmt3RFhTaTV1UmM0WGUza204dGszRnpFTFhWK1VNY1Vtd0hSb3l4N0g5azZYcHJZPSIsIml2UGFyYW1ldGVyU3BlYyI6IktVWkNjdUZRUWl5SVg3OWMiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master) |

## Table of contents

- [Table of contents](#table-of-contents)
- [Description](#description)
- [Install](#install)
- [External Ressources Dependencies](#external-ressources-dependencies)
  - [Postgresql Port Forwarding](#postgresql-port-forwarding)
  - [S3 Vector Bucket Access](#s3-vector-bucket-access)
- [Docker](#docker)
  - [Docker build locally](#docker-build-locally)
  - [Docker run locally](#docker-run-locally)
  - [Push the locally built docker image to ECR](#push-the-locally-built-docker-image-to-ecr)
- [Unit Testing](#unit-testing)
  - [Prerequisites](#prerequisites)
  - [Starting the tests](#starting-the-tests)
- [Download WMS image legends](#download-wms-image-legends)
- [Python Code Styling](#python-code-styling)
- [Varia](#varia)
  - [Lint a JSON file](#lint-a-json-file)

## Description

Next generation services [https://api3.geo.admin.ch](http://api3.geo.admin.ch) for [https://map.geo.admin.ch](https://map.geo.admin.ch)
In mid August 2022 the project has been migrated to `python3`, `docker` and `eu-central-1`.

## Install

The required environment variables are set in `.env.default`. They can be
adapted or you can use a copy of `.env.default`, e.g. `.env.mine` and use that
instead.

Install the python virtual environment (still `virtualenv`at this point)

```bash
make setup
```

Build the Pylons settings files and run the local `waitress` server

```bash
summon make serve
```

You may want to customize the variables. Copy the file `.env.default` as `.ven.mine`,
change the variables you want and use them with

```bash
summon make ENV_FILE=.env.mine serve
```

:book: You need some external ressource to run the service, see [External ressources dependencies](#external-ressources-dependencies)

## External Ressources Dependencies

To run the service locally you need to have access to the following external ressources:

- Postgresql database `pg-geodata-replica.bgdi.ch`
- S3 bucket `service-mf-chsdi3-grid-geojsons-dev-swisstopo` (NOTE: this bucket is only required by some of the Identity endpoints)

### Postgresql Port Forwarding

You can use the ssh port forwarding feature to have access to `pg-geodata-replica.bgdi.ch` by using the jump host:

```bash
ssh ssh0a.prod.bgdi.ch -L 5432:pg-geodata-replica.bgdi.ch:5432
```

Then set the `DBHOST` environment variable to `localhost` (you can do this in your own environment file e.g. `.env.mine` and run the make file as follow: `summon make ENV_FILE=.env.mine serve`)

### S3 Vector Bucket Access

To have access to the S3 bucket, you can either set your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variable. **:warning: When using those variables make sure that the command are not saved into history file !**

Alternatively if you are using `zsh` you can use the `aws` plugin (see [oh-my-zsh aws plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/aws)) with the following command:

```bash
acp swisstopo-bgdi-dev
```

This command will automatically use your AWS profile `swisstopo-bgdi-dev` for any AWS connection services.

## Docker

### Docker build locally

```bash
make dockerbuild
```

### Docker run locally

```bash
summon make dockerrun
```

:book: You need some external ressource to run the service, see [External ressources dependencies](#external-ressources-dependencies)

### Push the locally built docker image to ECR

First log in to the AWS ECR registry with:

```bash
make dockerlogin
```

afterwards you can push the locally built image to ECR with:

```bash
make dockerpush
```

## Unit Testing

### Prerequisites

- PostgreSQL DB `pg-geodata-replica.bgdi.ch` must be reachable
- Access to AWS services
  - Read access to S3 bucket `service-mf-chsdi3-grid-geojsons-dev-swisstopo` (can be disable with `S3_TESTS=0`)

See [External Ressources Dependencies](#external-ressources-dependencies) for more infos on those prerequisites.

### Starting the tests

To run the tests enter

```bash
summon make test
```

Or if you use your own environment file

```bash
summon make ENV_FILE=.env.mine test
```

**:warning: If you don't have AWS Access you can disable the S3 tests as follow**

```bash
summon make S3_TESTS=0 test
```

## Download WMS image legends

In order to download all images of a layer in the correct format and with the correct dimensions, simply use:

```bash
make legends BODID=ch.layername WMSHOST=wms.geo.admi.ch
```

Alternatively, you can also download a WMS legend for a specific scale.

```bash
make legends BODID=ch.layername WMSHOST=wms.geo.admi.ch WMSSCALELEGEND=1000
```

You will need the `optipgn` tool order to download the legends, use `sudo apt install optipng` to install it.

## Python Code Styling
<!--- TODO: to be changed to pylint and yapf, once that has been implemented with https://jira.swisstopo.ch/secure/RapidBoard.jspa?rapidView=444&view=planning&selectedIssue=BGDIINF_SB-2507&issueLimit=100 (if it will be implemented at all)-->
We are currently using the FLAKES 8 convention for Python code.
You can find more information about our code styling here:

- http://www.python.org/dev/peps/pep-0008/
- http://pep8.readthedocs.org/en/latest/index.html

You can find additional information about autopep8 here:

- https://pypi.python.org/pypi/autopep8/

To check the code styling:

```bash
make lint
```

To autocorrect most linting mistakes

```bash
make autolint
```

## Varia

### Lint a JSON file

```bash
export PATH=$(npm bin):$PATH
jsonlint-cli --pretty temp.json > chsdi/static/vectorStyles/ch.meteoschweiz.messwerte-foehn-10min.json
```
