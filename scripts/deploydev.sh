#!/bin/bash

T="$(date +%s)"

# set correct umask to assure proper rights after build
umask 0002

# set some variables
UUID=$(uuidgen)
ROOTDIR=/var/www/vhosts/mf-chsdi3/private
DEPLOYDIR=$ROOTDIR/chsdi
TEMPDIR=$ROOTDIR/chsdi_temp_$UUID
SNAPSHOT=`date '+%Y%m%d%H%M'`
SNAPSHOTDIR=$ROOTDIR/snapshots/$SNAPSHOT

# parse parameter (if -n is specified, no snapshot will be created)
GITBRANCH=master
CREATE_SNAPSHOT='false'
if [ "$1" == "-s" ]
then
  CREATE_SNAPSHOT='true'
  if [ -n "$2" ]
  then
    GITBRANCH=$2
  fi
fi

# Backup current project
if mv -f $DEPLOYDIR $TEMPDIR; then
  echo "Project backup in $TEMPDIR."
else
  echo "Could not backup the project."
fi

if cd $ROOTDIR; then
  git clone https://github.com/geoadmin/mf-chsdi3.git $DEPLOYDIR
else
  echo "Could not change directory. Restoring previous project." 1>&2
  rm -rf $DEPLOYDIR
  mv -f $TEMPDIR $DEPLOYDIR
  exit 1
fi

# Create a fresh clone of the project
if cd $DEPLOYDIR; then
  # remove all local changes and get latest GITBRANCH from remote
  git fetch origin && git reset --hard && git checkout $GITBRANCH && git reset --hard origin/$GITBRANCH
else
  echo "Could not change directory. Restoring previous project." 1>&2
  rm -rf $DEPLOYDIR
  mv -f $TEMPDIR $DEPLOYDIR
  exit 1
fi

# Build the project
source rc_dev
make all

exit_code=$?

if [ "$exit_code" -gt "0" ]
then
  echo "Failed to build the app. Restoring previous project." 1>&2
  rm -rf $DEPLOYDIR
  mv -f $TEMPDIR $DEPLOYDIR
  exit $exit_code
else
  echo "Build is successfull. Deleting old project."
  rm -rf $TEMPDIR
fi

# restart apache
sudo apache2ctl graceful

echo "Deployed branch $GITBRANCH to dev main."

# create a snapshot
if [ $CREATE_SNAPSHOT == 'true' ]; then
  sudo -u deploy deploy -c deploy/deploy.cfg $SNAPSHOTDIR
  echo "Snapshot of branch $GITBRANCH created at $SNAPSHOTDIR"
  cd $SNAPSHOTDIR/chsdi3/code/chsdi3/
  git describe --tags --abbrev=0 > .venv/last-release
  git log -1 --pretty=format:"%h - %an, %ar : %s" > .venv/last-commit-ref
  git rev-parse --symbolic-full-name --abbrev-ref HEAD > .venv/deployed-git-branch
  rm -rf .git*
else
  echo "NO Snapshot created. Specify '-s' parameter got create snapshot."
fi

T="$(($(date +%s)-T))"

printf "Deploy time: %02d:%02d:%02d\n" "$((T/3600%24))" "$((T/60%60))" "$((T%60))"
if [ $CREATE_SNAPSHOT == 'true' ]; then
  printf "Snapshot timestamp: $SNAPSHOT\n"
fi
