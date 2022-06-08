Migration to Python3, Docker and Frankfort
==========================================


Currently, we are porting `mf-chsdi3` to `python3`, `docker` and `Frankfurt`

Install
-------

Use only `Makefile.frankfurt`


The required environment variables are set in `.env.default`. They can be
adapted or you can use a copy of `.env.default`, e.g. `env.mine` and use that
instead.

```bash
set -o allexport; source .env.default (or .env.mine); set +o allexport  
export ENV_FILE=.env.local (or .env.mine)
```

Install the python virtual environment (still `virtualenv`at this point)

    make -f Makefile.frankfurt setup

 
Build the Pylons settings files and run the local `waitress`server

    make -f Makefile.frankfurt environ serve
    
You may want to customize the variables. Copy the file `.env.default` as `.ven.mine`,
change the variables you want and use them with

    ENV_FILE=.env.mine make -f Makefile.frankfurt environ serve
    

N.B. Some variables must be set manually, namely `PGUSER`, `PGPWASSPORD`, `OPENTRANS_API_KEY`


Docker build
------------


     make -f Makefile.frankfurt environ dockerbuild dockerrun
     
Use your custome set of variables with

    ENV_FILE=.env.mine  make -f Makefile.frankfurt environ dockerbuild dockerrun
    

Testing
-------

Many tests still fails, but run them with

    make -f Makefile.frankfurt test
