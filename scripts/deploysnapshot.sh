#!/bin/bash

#bail out on any error
set -o errexit

# Check if snapshot parameter is supplied and there are 2 parameters
if [ "$2" != "int" ] && [ "$2" != "prod" ] && [ "$2" != "demo" ]
then
  echo "Error: Please specify 1) snapshot directoy and 2) target."
  exit 1
fi

T="$(date +%s)"
SNAPSHOTDIR=/var/www/vhosts/mf-chsdi3/private/snapshots/$1
DEPLOYCONFIG=deploy/deploy.cfg
PROJECT_ROOT=$(pwd)
SNAPSHOTDIR_CODE=$SNAPSHOTDIR/chsdi3/code/chsdi3

# Go into snapshot directory to run nose-tests
cd $SNAPSHOTDIR_CODE

# Run nose tests with target cluster db
if [ -z $3 ] || [ $3 != "notests" ]
then
    if [ "$2" == "int" ]
    then
      echo "Running nose tests with integration cluster in $SNAPSHOTDIR"
      scripts/nose_run.sh -i
    fi

    if [ "$2" == "prod" ]
    then
      echo "Running nose tests with production cluster in $SNAPSHOTDIR"
      scripts/nose_run.sh -p
    fi
else
    echo "You have disabled nosetests!"
fi

# cleanup pyc files (orphaned .pyc issues)
find * -name '*.pyc' | xargs rm -f

# Back to working directory for the deploy command
cd ${PROJECT_ROOT}

echo "Using local deploy configuration"
sudo -u deploy deploy -r $DEPLOYCONFIG $2 $SNAPSHOTDIR

T="$(($(date +%s)-T))"

printf "Deploy time: %02d:%02d:%02d:%02d\n" "$((T/86400))" "$((T/3600%24))" "$((T/60%60))" "$((T%60))"

