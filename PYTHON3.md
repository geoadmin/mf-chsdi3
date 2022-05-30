Migration to Python3, Docker and Frankfort
==========================================


Currently, we are porting `mf-chsdi3` to `python3`, `docker` and `Frankfurt`

Install
-------

Use only `Makefile.frankfurt`


Install the python virtual environment (still `virtualenv`at this point)

    make -f Makefile.frankfurt setup

Set the require environmental variables with

    export $(cat local.env)
    
Build the Pylons settings files and run the local `waitress`server

    make -f Makefile.frankfurt environ server
    

N.B. Some variables must be set manually, namely `PGUSER`, `PGPWASSPORD`, `OPENTRANS_API_KEY`


Docker build
------------



     make -f Makefile.frankfurt environ dockerbuild dockerrun


Testing
-------

Many tests still fails, but run them with

    make -f Makefile.frankfurt test
