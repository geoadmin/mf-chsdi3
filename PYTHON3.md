Migration to Python3
====================


Currently, we are porting `mf-chsdi3` to `python3` and `docker`

Install
-------

For practical reason, `Makefile` will download and compile its
own version of Python 3.6 and store it in the `local` directory.


To install the `venv`:

    USE_PYTHON3=1 make cleanall user

For all `make` target, use the same `USE_PYTHON3=1` variable

    USE_PYTHON3=1 make test

or

    USE_PYTHON3=1 make serve

Docker build
------------


Testing
-------

The project `mf-chsdi3` needs a working PostgreSQL connection but will however
always start and hang forever.

The `docker-entrypoint-sh` script is testing the PostgreSQL connectivity

    docker-compose up 
    Recreating mf-chsdi3_chsdi3_1 ... done
    Attaching to mf-chsdi3_chsdi3_1
    chsdi3_1  | INSTALLDIR=/var/www/vhosts/mf-chsdi3/private/chsdi
    chsdi3_1  | pg.bgdi.ch:5432 - no response
    mf-chsdi3_chsdi3_1 exited with code 2

and fail if no database is found.
