Migration to Python3, Docker and Frankfort
==========================================

Currently, we are porting `mf-chsdi3` to `python3`, `docker` and `Frankfurt`

- [Install](#install)
- [Docker build](#docker-build)
- [Docker run](#docker-run)
- [Testing](#testing)

Install
-------

Use only `Makefile.frankfurt`

The required environment variables are set in `.env.default`. They can be
adapted or you can use a copy of `.env.default`, e.g. `.env.mine` and use that
instead.

```bash
set -o allexport; source .env.default (or .env.mine); set +o allexport  
export ENV_FILE=.env.local (or .env.mine)
```

Install the python virtual environment (still `virtualenv`at this point)

```bash
make -f Makefile.frankfurt setup
```

Build the Pylons settings files and run the local `waitress` server

```bash
summon make -f Makefile.frankfurt environ serve
```

You may want to customize the variables. Copy the file `.env.default` as `.ven.mine`,
change the variables you want and use them with

```bash
summon make -f Makefile.frankfurt ENV_FILE=.env.mine environ serve
```

Docker build
------------

```bash
    make -f Makefile.frankfurt dockerbuild
```

Docker run
----------

```bash
summon make -f Makefile.frankfurt dockerrun
```

NOTE: You need access to the database `pg-geodata-replica.bgdi.ch`. For this you can use the SSH
LocalForward functionality with our jumphost and then modify the `DBHOST` to `localhost`

1. Open an SSH connection with port forwarding

    ```bash
    ssh ssh0a.prod.bgdi.ch -L 5432:pg-geodata-replica.bgdi.ch:5432
    ```

2. Starts the container localy

    ```bash
    summon make -f Makefile.frankfurt ENV_FILE=.env.mine dockerrun
    ```

Testing
-------

Many tests still fails, but run them with

```bash
make -f Makefile.frankfurt test
```
