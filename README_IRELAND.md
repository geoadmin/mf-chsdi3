mf-chsdi3
=========

Next generation services [https://api3.geo.admin.ch](http://api3.geo.admin.ch) for [https://map.geo.admin.ch](https://map.geo.admin.ch)

**AWS CodeBuild Status**

Python3 ![Build Status](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiMFAzY3lvZVQ4eFRjSk9DWE1xNWpqQVUrL3pFb0VVQmpyRG9HY0ZtV0tSVXU3djMzQ0dvMDhMaG1qa2k5YkV6V1huRjRuNXljTnZZazdnc3pQNVpmVmdZPSIsIml2UGFyYW1ldGVyU3BlYyI6InFJOXZ3azE5NzJoZ2U2bXYiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

Python2 ![Build Status](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiTGN0cGVaT0s4OG9CMCtMeW14elhmMzBVWEF3U3F1b3A2a01BbktuNWJyOUVOMUxiUXB1SmFwK2diV0JkOXdvT3VIbmJjMkVjYU02N1pTZmFPRUtXdXFZPSIsIml2UGFyYW1ldGVyU3BlYyI6IjZ0ZmgzUFY2dnYwUm9QcHYiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

# Version

As 2022, the project is slowing transitioning to `python3` and `docker`. So basically, there two way of running this project:

## Legacy vhost

Using the `Makefile`, this is running within an apache2 `vhost` and with `python2`, which still is the default.
You may test python3 setting `USE_PYTHON3=1`

## New world

With `python3`, `docker` in `eu-central-1`. Use `Makefile.frankfurt`. SE the `PYTHON3.md` file.


# Installing (legacy)

Checkout the source code:

    git clone https://github.com/geoadmin/mf-chsdi3.git

or when you're using ssh key (see https://help.github.com/articles/generating-ssh-keys):

    git clone git@github.com:geoadmin/mf-chsdi3.git

Add _.pgpass_ to your environment

    cd
    touch .pgpass
    chmod 600 .pgpass

Open _.pgpass_ and Add

    pg.bgdi.ch:5432:*:${username}:${pass}

Make sure PGUSER and PGPASS is set in your _.bashrc_ (for nosetests, potranslate and sphinx)

    export PGUSER=${username} // postgres user (won't be relevant soon)
    export PGPASS=${pass}

Note: on `vpc-mf1-dev`, AWS credentials are set by an *instance rule*. On other instances, you'll have to instance 
manually the credentials in `$HOME/.aws/credentials`


Create a developer specific build configuration:

    touch rc_user_<username>

Add the port number in the newly created user rc file. You should at least edit your dev port. For instance:

    export SERVER_PORT=9000

Add the API key to retrieve departure information from https://opentransportdata.swiss into the users rc file or directly in the .bashrc (`gopass`). For instance:

    export OPENTRANS_API_KEY=dasffdjfjfjfjf566776jfjfjfj22243eac841ce7c9426355b

Every variables you export in rc_user_<username> will override the default ones in rc_dev and rc_user.

Where "username" is your specific rc configuration. To create the specific build:

    make -f Makefile.ireland user

If you do this on `vpc-mf1-dev1`, you need to make sure that a correct configuration exists under

    /var/www/vhosts/mf-chsdi3/conf

that points to your working directory. If all is well (`sudo apache2ctl graceful`), you can reach your pages at:

    http://mf-chsdi3.dev.bgdi.ch/<username>/

## Git hooks

Three `git hooks` are installed automatically when `make -f Makefile.ireland user` is called.

All the hooks check that we don't accidently publish sensitive AWS keys to
github - in the files as well as in the commit messages. We also execute

    make -f Makefile.ireland lint

in the pre-commit hook.

Other checks can be added freely to any hook.

### `pre-commit` hook

Called before committing changes locally. The commands in the `scripts/pre-commit.sh` script are executed.

### `commit-msg` hook

Called before comitting changes locally and checks the commit message. The commands in the `scripts/commit-msg.sh` script are executed.

### `prepare-commit-msg` hook

Called before comitting changes locally and checks pre-commit messages (usually from --fast-forward merges. The commands in the `scripts/prepare-commit-msg.sh` are executed.

# Deploying to dev, int, and prod

Do the following commands **inside your working directory**. Here's how a standard
deploy process is done.

    make -f Makefile.ireland deploydev SNAPSHOT=true

This updates the source in /var/www... to the latest master branch from github,
creates a snapshot and runs nosetests against the test db. The snapshot directory
will be shown when the script is done. *Note*: you can omit the `-s` parameter if
you don't want to create a snapshot e.g. for intermediate releases on dev main.

Once a snapshot has been created, you are able to deploy this snapshot to a
desired target. For integration, do

    make -f Makefile.ireland deployint SNAPSHOT=201512011411

This will run the full nose tests **from inside the 201512011411 snapshot directory** against the **integration db cluster**. Only if these tests are successfull, the snapshot is deployed to the integration cluster.

    make -f Makefile.ireland deployprod SNAPSHOT=201512011411

You can disable the running of the nosetests against the target backends by adding
`notests` parameter to the snapshot command. This is handy in an emergency (when
deploying an old known-to-work snapshot) or when you have to re-deploy
a snapshot that you know has passed the tests for the given backend.
To disable the tests, use the following command:

    make -f Makefile.ireland deployint SNAPSHOT=201512011411 NO_TESTS=notests

Use `notests` parameter with care, as it removes a level of tests.

Per default the deploy command uses the deploy configuration of the snapshot directory.
If you want to use the deploy configuration of directory from which you are executing this command, you can use:

    make -f Makefile.ireland deployint SNAPSHOT=201512011411

## Deploying a branch

Call the `make -f Makefile.ireland deploybranch` command **in your working directory** to deploy your current
branch to test (Use `make -f Makefile.ireland deploybranchint` to also deploy it to integration).
The code for deployment, however, does not come from your working directory,
but does get cloned (first time) or pulled (if done once) **directly from github**.
So you'll likely use this command **after** you push your branch to github.

The first time you use the command will take some time to execute.

The code of the deployed branch is in a specific directory
`/var/www/vhosts/mf-geoadmin3/private/branch` on both test and integration.
The command adds a branch specific configuration to
`/var/www/vhosts/mf-geoadmin3/conf`. This way, the deployed branch
behaves exactly the same as any user specific deploy.

Sample path:
http://mf-chsdi3.int.bgdi.ch/gjn_deploybranch/ (Don't forget the slash at the end)

## Deleting a branch

To list all the deployed branch:

    make -f Makefile.ireland deletebranch

To delete a given branch:

    make -f Makefile.ireland deletebranch BRANCH_TO_DELETE=my_deployed_branch

## Get correct back-link to geoadmin3
Per default the back-link to geoadmin3 points to the main instance. If you
want to change that, adapt the `geoadminhost` variable in the
`buildout_branch.cfg.in` input file and commit it in *your branch*.

# Testing (legacy)

## Run nosetests manual on different environments
We are able to run our integration tests against different staging environments

**For this to work, you need to adapt your personal ~/.pgpass file. It has to
include access information for all clusters (add pgcluster0i and pgcluster0)**

To run against prod environment:

    scripts/nose_run.sh -p

To run against int environment:

    scripts/nose_run.sh -i

To run against dev/test environment:

    scripts/nose_run.sh

To run against your private environment:

    make -f Makefile.ireland test

To execute all tests, including _wmts_ and _varnish_ ones, which are deactivated by default:

    scripts/nose_run.sh -a

## Deactivate some tests

You may deactivate tests requiring access to 'AWS S3' or the 'Sphinx server', by 
setting the following environmental variables to `0`

    SPHINX_TESTS=0 S3_TESTS=0 make -f Makefile.ireland test

### Resources for testing

:bomb: Resources are in `eu-central-1` for testing, otherwise in `eu-west-1`

#### PostgreSQL
The PostgreSQL cluster with all vector data. This cannot be deactivate, as the project wont start without

#### Sphinx server

The `search service` needs the `Sphinx search server` cluster, running on separate instances. These tests may
be skipped with:

    SPHINX_TESTS=0  make -f Makefile.ireland test

#### AWS S3

S3 is used for the identify service and the feature grid (windatlas). The bucket is `mf-chsdi3-bgdi-grid-based-data`.
To ski the tests that depends on S3, sets the `S3_TESTS` variables must be set to `false`:

    S3_TESTS=0 make -f Makefile.ireland test

# Checker

Apache/WSGI checker

    curl -I http://api3.geo.admin.ch/checker


## Download WMS image legends

In order to download all images of a layer in the correct format and with the correct dimensions, simply use:

```bash
make -f Makefile.ireland legends BODID=ch.layername
```

Alternatively, you can also download a WMS legend for a specific scale.

```bash
make -f Makefile.ireland legends BODID=ch.layername WMSSCALELEGEND=1000
```

Make sure, you're using the desired `echo $WMSHOST` project variable (`source rc_xxx` or `export WMSHOST=xxx`)

# Python Code Styling

We are currently using the FLAKES 8 convention for Python code.
You can find more information about our code styling here:

    http://www.python.org/dev/peps/pep-0008/
    http://pep8.readthedocs.org/en/latest/index.html

You can find additional information about autopep8 here:

    https://pypi.python.org/pypi/autopep8/

To check the code styling:

```bash
make -f Makefile.ireland lint
```

To autocorrect most linting mistakes

```bash
make -f Makefile.ireland autolint
```

# Varia

## Lint a JSON file

```bash
export PATH=$(npm bin):$PATH
jsonlint-cli --pretty temp.json > chsdi/static/vectorStyles/ch.meteoschweiz.messwerte-foehn-10min.json
```

## Create legends

Install dependencies:

```bash
sudo apt-get install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++
```

Run the script

```
node scripts/createlegends.js ch.meteoschweiz.messwerte-niederschlagn
```