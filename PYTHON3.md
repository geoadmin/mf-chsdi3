# Migration to Python3, Docker and Frankfort

Currently, we are porting `mf-chsdi3` to `python3`, `docker` and `Frankfurt`

- [Install](#install)
- [External Ressources Dependencies](#external-ressources-dependencies)
  - [Postgresql Port Forwarding](#postgresql-port-forwarding)
  - [S3 Vector Bucket Access](#s3-vector-bucket-access)
- [Docker](#docker)
  - [Docker build](#docker-build)
  - [Docker run](#docker-run)
- [Unit Testing](#unit-testing)
  - [Prerequisites](#prerequisites)
  - [Starting the tests](#starting-the-tests)
- [Download WMS image legends](#download-wms-image-legends)

## Install

Use only `Makefile.frankfurt`

The required environment variables are set in `.env.default`. They can be
adapted or you can use a copy of `.env.default`, e.g. `.env.mine` and use that
instead.

Install the python virtual environment (still `virtualenv`at this point)

```bash
make -f Makefile.frankfurt setup
```

Build the Pylons settings files and run the local `waitress` server

```bash
summon make -f Makefile.frankfurt build serve
```

You may want to customize the variables. Copy the file `.env.default` as `.ven.mine`,
change the variables you want and use them with

```bash
summon make -f Makefile.frankfurt ENV_FILE=.env.mine build serve
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

Then set the `DBHOST` environment variable to `localhost` (you can do this in your own environment file e.g. `.env.mine` and run the make file as follow: `summon make -f Makefile.frankfurt ENV_FILE=.env.mine serve`)

### S3 Vector Bucket Access

To have access to the S3 bucket, you can either set your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variable. **:warning: When using those variables make sure that the command are not saved into history file !**

Alternatively if you are using `zsh` you can use the `aws` plugin (see [oh-my-zsh aws plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/aws)) with the following command:

```bash
acp swisstopo-bgdi-dev
```

This command will automatically use your AWS profile `swisstopo-bgdi-dev` for any AWS connection services.

## Docker

### Docker build

```bash
make -f Makefile.frankfurt dockerbuild
```

### Docker run

```bash
summon make -f Makefile.frankfurt dockerrun
```

:book: You need some external ressource to run the service, see [External ressources dependencies](#external-ressources-dependencies)

## Unit Testing

### Prerequisites

- PostgreSQL DB `pg-geodata-replica.bgdi.ch` must be reachable
- Access to AWS services
  - Read access to S3 bucket `service-mf-chsdi3-grid-geojsons-dev-swisstopo` (can be disable with `S3_TESTS=0`)

See [External Ressources Dependencies](#external-ressources-dependencies) for more infos on those prerequisites.

### Starting the tests

To run the tests enter

```bash
summon make -f Makefile.frankfurt test
```

Or if you use your own environment file

```bash
summon make -f Makefile.frankfurt ENV_FILE=.env.mine test
```

**:warning: If you don't have AWS Access you can disable the S3 tests as follow**

```bash
summon make -f Makefile.frankfurt S3_TESTS=0 test
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
