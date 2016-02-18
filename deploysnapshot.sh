#!/bin/bash

T="$(date +%s)"

#bail out on any error
set -o errexit

# Check if snapshot parameter is supplied and there are 2 parameters
if [ "$2" != "int" ] && [ "$2" != "prod" ] && [ "$2" != "demo" ]
then
  echo "Error: Please specify 1) snapshot directoy and 2) target."
  exit 1
fi

SNAPSHOTDIR=/var/www/vhosts/mf-chsdi3/private/snapshots/$1

cwd=$(pwd)

# Go into snapshot directory to run nose-tests
cd $SNAPSHOTDIR/chsdi3/code/chsdi3

if [ "$2" == "int" ]
then
  if [ -z $3 ] || [ $3 != "notests" ]
  then
    echo "Running nose tests with integration cluster in $SNAPSHOTDIR"
    ./nose_run.sh -i
  fi
  buildout/bin/buildout -c buildout_int.cfg
elif [ "$2" == "prod" ]
then
  if [ -z $3 ] || [ $3 != "notests" ]
  then
    echo "Running nose tests with production cluster in $SNAPSHOTDIR"
    ./nose_run.sh -p
  fi
  buildout/bin/buildout -c buildout_prod.cfg
fi

if [ -z $3 == "notests" ]
then
  echo "You have disabled the tests"
fi

# back to working directory for the deploy command
cd $cwd
sudo -u deploy deploy -r deploy/deploy.cfg $2 $SNAPSHOTDIR

T="$(($(date +%s)-T))"

printf "Deploy time: %02d:%02d:%02d:%02d\n" "$((T/86400))" "$((T/3600%24))" "$((T/60%60))" "$((T%60))"

