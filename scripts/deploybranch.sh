#!/bin/bash

T="$(date +%s)"

# Bail out on any error
set -o errexit

BASE_DIR=/var/www/vhosts/mf-chsdi3
GIT_BRANCH=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
CODE_DIR=$BASE_DIR/private/branch/$GIT_BRANCH

if ! [ -f $CODE_DIR/.git/config ];
then
    git clone https://github.com/geoadmin/mf-chsdi3 $CODE_DIR
    cd $CODE_DIR
fi

cd $CODE_DIR
# Remove all local changes and get latest GITBRANCH from remote
git fetch origin && git reset --hard && git checkout $GIT_BRANCH && git reset --hard origin/$GIT_BRANCH
# Clean all in case the branch was deployed previously
make cleanall

# This creates the branch configuration
make setup
make rc_branch DEPLOY_TARGET=dev
source rc_branch
make all
make deploy/deploy-branch.cfg
make deploy/conf/00-branch.conf

# Copy the apache configuration for the branch
cp deploy/conf/00-branch.conf $BASE_DIR/conf/00-$GIT_BRANCH.conf

# Deploy to int if 'int' is specified
if [ $1 -a $1 == 'int' ];
then
    sudo -u deploy deploy -r deploy/deploy-branch.cfg int;
fi

if [ $1 -a $1 == 'demo' ];
then
    sudo -u deploy deploy -r deploy/deploy-branch.cfg demo;
fi


T="$(($(date +%s)-T))"

printf "Deploy time: %02d:%02d:%02d\n" "$((T/3600%24))" "$((T/60%60))" "$((T%60))"

