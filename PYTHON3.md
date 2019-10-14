Migration to Python3
====================


Currently, we are porting `mf-chsdi3` to Python3.

For practical reason, `Makefile` will download and compile its
own version of Python 3.6 and store it in the `local` directory.


To install the `venv`:

    USE_PYTHON3=1 make cleanall user

For all `make` target, use the same `USE_PYTHON3=1` variable

    USE_PYTHON3=1 make test

or

    USE_PYTHON3=1 make serve

