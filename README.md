# mf-chsdi3

| Branch | Status |
|---|---|
| master | ![Build Status](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiNVluN1lOc05FUUZVa093RXJ6aERCVnpCZTIvM09mZlhMWkR0ekF6WkVDTDBVSWxBOGg0TE43b2ZwWSs1MldBOExqaUl4RlBpZWtXWlhxOURValRlUXdjPSIsIml2UGFyYW1ldGVyU3BlYyI6IjMxQ0dRZlNXVTVIeTA2TE4iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master) |

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
- [Updating Python Packages](#updating-python-packages)
- [OTEL](#otel)
  - [Environment variables](#environment-variables)
- [Varia](#varia)
  - [Lint a JSON file](#lint-a-json-file)
- [Local Smoke test for Open Telemetry](#local-smoke-test-for-open-telemetry)
  - [Make a HTTP Query](#make-a-http-query)

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
summon -p ssm make serve
```

You may want to customize the variables. Copy the file `.env.default` as `.ven.mine`,
change the variables you want and use them with

```bash
summon -p ssm make ENV_FILE=.env.mine serve
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

Then set the `DBHOST` environment variable to `localhost` (you can do this in your own environment file e.g. `.env.mine` and run the make file as follow: `summon -p ssm make ENV_FILE=.env.mine serve`)

or simpler, when you use the ssh_config provided by infra-ansible-bgdi-dev:

```bash
ssh jumphost-pg-geodata-replica
```

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
summon -p ssm make dockerrun
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
summon -p ssm make test
```

Or if you use your own environment file

```bash
summon -p ssm make ENV_FILE=.env.mine test
```

**:warning: If you don't have AWS Access you can disable the S3 tests as follow**

```bash
summon -p ssm make S3_TESTS=0 test
```

## Download WMS image legends

In order to download all images of a layer in the correct format and with the correct dimensions, simply use:

```bash
make legends BODID=ch.layername WMSHOST=wms.geo.admin.ch
```

Alternatively, you can also download a WMS legend for a specific scale.

```bash
make legends BODID=ch.layername WMSHOST=wms.geo.admin.ch WMSSCALELEGEND=1000
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

## Updating Python Packages

All packages used in production are pinned to a major version. Automatically updating these packages
will use the latest minor (or patch) version available. Packages used for development, on the other
hand, are not pinned unless they need to be used with a specific version of a production package
(for example, boto3-stubs for boto3).

To update the packages to the latest minor/compatible versions, run:

```bash
pipenv update --dev
```

To see what major/incompatible releases would be available, run:

```bash
pipenv update --dev --outdated
```

To update packages to a new major release, run:

```bash
pipenv install logging-utilities~=5.0
```

## OTEL

[OpenTelemetry instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/) can be done in many different ways, from fully automated zero-code instrumentation (otel-operator) to purely manual instrumentation.
We use the so called `OTEL programmatical instrumentation` approach where we import the specific instrumentation libraries and initialize them with the instrument() method of each library.

### Environment variables

The following env variables can be used to configure OTEL

| Env Variable                                              | Default               | Description                                                                                                                                          |
| --------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| OTEL_SDK_DISABLED                                         | false                 | If set to "true", OTEL is disabled. See: https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration |
| OTEL_ENABLE_SQLALCHEMY                                    | false                 | If opentelemetry-instrumentation-sqlalchemy should be enabled or not.                                                                                |
| OTEL_ENABLE_REQUESTS                                      | false                 | If opentelemetry-instrumentation-requests should be enabled or not.                                                                                  |
| OTEL_ENABLE_LOGGING                                       | false                 | If opentelemetry-instrumentation-logging should be enabled or not.                                                                                   |
| OTEL_EXPERIMENTAL_RESOURCE_DETECTORS                      |                       | OTEL resource detectors, adding resource attributes to the OTEL output. e.g. `os,process`                                                            |
| OTEL_EXPORTER_OTLP_ENDPOINT                               | http://localhost:4317 | The OTEL Exporter endpoint, e.g. `opentelemetry-kube-stack-gateway-collector.opentelemetry-operator-system:4317`                                     |
| OTEL_EXPORTER_OTLP_HEADERS                                |                       | A list of key=value headers added in outgoing data. https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#header-configuration    |
| OTEL_EXPORTER_OTLP_INSECURE                               | false                 | If exporter ssl certificates should be checked or not.                                                                                               |
| OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_REQUEST  |                       | A comma separated list of request headers added in outgoing data. Regex supported. Use '.*' for all headers                                          |
| OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_RESPONSE |                       | A comma separated list of response headers added in outgoing data. Regex supported. Use '.*' for all headers                                         |
| OTEL_PYTHON_EXCLUDED_URLS                                 |                       | A comma separated list of url's to exclude, e.g. `checker,static/*`                                                                                  |
| OTEL_RESOURCE_ATTRIBUTES                                  |                       | A comma separated list of custom OTEL resource attributes, Must contain at least the service-name `service.name=mf-chsdi3`                           |
| OTEL_TRACES_SAMPLER                                       | parentbased_always_on | Sampler to be used, see https://opentelemetry-python.readthedocs.io/en/latest/sdk/trace.sampling.html#module-opentelemetry.sdk.trace.sampling.       |
| OTEL_TRACES_SAMPLER_ARG                                   |                       | Optional additional arguments for sampler.                                                                                                           |

## Varia

### Lint a JSON file

```bash
export PATH=$(npm bin):$PATH
jsonlint-cli --pretty temp.json > chsdi/static/vectorStyles/ch.meteoschweiz.messwerte-foehn-10min.json
```

## Local Smoke test for Open Telemetry

1. (optional) `aws --profile swisstopo-bgdi-dev sso login`
2. `ssh jumphost-pg-geodata-replica` to setup SSH Tunnel to DB
3. `docker compose up` to run a local Jaeger server
4. `summon -p ssm make dockerrun`

### Make a HTTP Query

Open in a browser or curl:

http://localhost:8009/rest/services/ech/MapServer/identify?layers=all:ch.bav.haltestellen-oev&sr=2056&geometry=2596144.500865812,1192821.252700392&mapExtent=2595220.51,1191795.99,2597416.51,1193957.99&imageDisplay=1098,1081,96&geometryFormat=geojson&geometryType=esriGeometryPoint&limit=10&tolerance=10&returnGeometry=true&lang=en
