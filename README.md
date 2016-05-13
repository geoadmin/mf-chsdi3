mf-chsdi3
=========

next generation of [http://api3.geo.admin.ch](http://api3.geo.admin.ch)

Jenkins Build Status: [![Jenkins Build Status](https://jenkins.ci.bgdi.ch/buildStatus/icon?job=chsdi3)](https://jenkins.prod.bgdi.ch/job/chsdi3/)

# Getting started

Checkout the source code:

    git clone https://github.com/geoadmin/mf-chsdi3.git

or when you're using ssh key (see https://help.github.com/articles/generating-ssh-keys):

    git clone git@github.com:geoadmin/mf-chsdi3.git

Add .pgpass to your environment

    cd
    touch .pgpass
    chmod 600 .pgpass

Open .pgpass and Add

    pg.bgdi.ch:5432:*:${username}:${pass}
    pg-sandbox.bgdi.ch:5432:*:${username}:${pass}

Make sure PGUSER and PGPASS is set in your .bashrc (for nosetests, potranslate and sphinx)

    export PGUSER=${username} // postgres user (won't be relevant soon)
    export PGPASS=${pass}

Add .boto to your environment

    cd
    touch .boto
    chmod 600 .boto

Open .boto and Add (`/etc/boto.cfg` for main)

    [Credentials]
    aws_access_key_id = ${keyid}
    aws_secret_access_key = ${accesskey}

[Nagios Check for Dynamodb Dumps](https://dashboard.bgdi.ch/cgi-bin/nagios3/extinfo.cgi?type=2&host=ip-10-220-4-46.eu-west-1.compute.internal&service=DynamoDB+backup)

Create a developer specific build configuration:

    touch rc_user_<username>

Add the port number in the newly created user rc file. You should at least edit your dev port. For instance:

    export SERVER_PORT=9000

Every variables you export in rc_user_<username> will override the default ones in rc_dev and rc_user.

Where "username" is your specific rc configuration. To create the specific build:

    make user

If you do this on mf1t, you need to make sure that a correct configuration exists under
    
    /var/www/vhosts/mf-chsdi3/conf

that points to your working directory. If all is well, you can reach your pages at:

    http://mf-chsdi3.dev.bgdi.ch/<username>/

## Deploying to dev, int, prod and demo

Do the following commands **inside your working directory**. Here's how a standard
deploy process is done.

`make deploydev SNAPSHOT=true`

This updates the source in /var/www... to the latest master branch from github,
creates a snapshot and runs nosetests against the test db. The snapshot directory
will be shown when the script is done. *Note*: you can omit the `-s` parameter if
you don't want to create a snapshot e.g. for intermediate releases on dev main.

Once a snapshot has been created, you are able to deploy this snapshot to a
desired target. For integration, do

`make deployint SNAPSHOT=201512011411`

This will run the full nose tests **from inside the 201512011411 snapshot directory** against the **integration db cluster**. Only if these tests are successfull, the snapshot is deployed to the integration cluster.

`make deployprod SNAPSHOT=201512011411`

This will do the corresponding thing for prod (tests will be run **against prod backends**)
The same is valid for demo too:

`make deploydemo SNAPSHOT=201512011411`

You can disable the running of the nosetests against the target backends by adding
`notests` parameter to the snapshot command. This is handy in an emergency (when
deploying an old known-to-work snapshot) or when you have to re-deploy
a snapshot that you know has passed the tests for the given backend.
To disable the tests, use the following command:

`make deployint SNAPSHOT=201512011411 NO_TESTS=notests`

Use `notests` parameter with care, as it removes a level of tests.

Per default the deploy command uses the deploy configuration of the snapshot directory.
If you want to use the deploy configuration of directory from which you are executing this command, you can use:

`make deployint SNAPSHOT=201512011411 DEPLOYCONFIG=from_current_directory`

## Deploying a branch

Call the `make deploybranch` command **in your working directory** to deploy your current
branch to test (Use `make deploybranchint` to also deploy it to integration).
The code for deployment, however, does not come from your working directory,
but does get cloned (first time) or pulled (if done once) **directly from github**.
So you'll likely use this command **after** you push your branch to github.

The first time you use the command will take some time to execute.

The code of the deployed branch is in a specific directory 
`/var/www/vhosts/mf-geoadmin3/private/branch` on both test and integration.
The command adds a branch specific configuration to
`/var/www/vhosts/mf-geoadmin3/conf`. This way, the deployed branch
behaves exactly the same as any user specific deploy.
A deploy to a "demo" instance is possible too (simply use ./deploybranch.sh demo).

Sample path:
http://mf-chsdi3.int.bgdi.ch/gjn_deploybranch/ (Don't forget the slash at the end)

## Deleting a branch

To list all the deployed branch:
`make deletebranch`

To delete a given branch:
`make deletebranch BRANCH_TO_DELETE=my_deployed_branch`

## Get correct back-link to geoadmin3
Per default the back-link to geoadmin3 points to the main instance. If you
want to change that, adapt the `geoadminhost` variable in the
`buildout_branch.cfg.in` input file and commit it in *your branch*.

## Run nosetests manual on different environments
We are able to run our integration tests against different staging environments

**For this to work, you need to adapt your personal ~/.pgpass file. It has to
include access information for all clusters (add pgcluster0i and pgcluster0)**

To run against prod environment:
`scripts/nose_run.sh -p`

To run against int environment:
`scripts/nose_run.sh -i`

To run against dev/test environment:
`scripts/nose_run.sh`

To run against your private environment:
`make test`

To execute all tests, including _mapproxy_ and _varnish_ ones, which are deactivated by default:
`scripts/nose_run.sh -a`

## Printing

Per default, printing is handled by one single war file on an instances. This war is installed and handled by the 'main' installation.

If you need to work on printing and use your own war, you have to add the following to your personal configuration (rc_user_xxx file):

```
export PRINT_WAR=ltxxx
```

In order to create the shared war use:

```
make printwar APACHE_BASE_PATH=main
```

## Python Code Styling

We are currently using the FLAKES 8 convention for Python code.
You can find more information about our code styling here:

    http://www.python.org/dev/peps/pep-0008/
    http://pep8.readthedocs.org/en/latest/index.html

You can find additional information about autopep8 here:

    https://pypi.python.org/pypi/autopep8/

To check the code styling:

  ```bash
make lint
  ```

To autocorrect most linting mistakes

  ```bash
make autolint
  ```

## Git hooks

3 git hooks are installed automatically when `make user` is called.

All the hooks check that we don't accidently publish sensitive AWS keys to
github - in the files as well as in the commit messages. We also execute
`make lint` in the pre-commit hook.

Other checks can be added freely to any hook.

### `pre-commit` hook

Called before committing changes locally. The commands in the `scripts/pre-commit.sh` script are executed.

### `commit-msg` hook

Called before comitting changes locally and checks the commit message. The commands in the `scripts/commit-msg.sh` script are executed.

### `prepare-commit-msg` hook

Called before comitting changes locally and checks pre-commit messages (usually from --fast-forward merges. The commands in the `scripts/prepare-commit-msg.sh` are executed.
