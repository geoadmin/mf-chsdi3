#!/bin/bash

# Script to deploy the mf-chsdi3 project in a separate directory on vpc-mf1-dev1
# https://mf-chsdi3.dev.bgdi.ch/<branch name>
#
# By default, the current branch is deployed, but it may be changed by setting
# the variable GIT_BRANCH. The project is in all case downloaded from GitHub.


T="$(date +%s)"

# Bail out on any error
set -o errexit

[ -z "${GIT_BRANCH}"  ] && GIT_BRANCH=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD) 

BASE_DIR=/var/www/vhosts/mf-chsdi3
CODE_DIR=$BASE_DIR/private/branch/$GIT_BRANCH

echo "==================================================================="
echo "Deploying chsdi3 branch <${GIT_BRANCH}> to <dev> "
echo "==================================================================="

if ! [ -f $CODE_DIR/.git/config ];
then
    git clone https://github.com/geoadmin/mf-chsdi3 $CODE_DIR
fi

cd $CODE_DIR
# Remove all local changes and get latest GITBRANCH from remote
git fetch origin && git reset --hard && git checkout $GIT_BRANCH && git reset --hard origin/$GIT_BRANCH && git clean -fxd .
# Clean all in case the branch was deployed previously
make cleanall

# This creates the branch configuration
echo "======================================="
echo "Creating configs in <${GIT_BRANCH}>"
echo "======================================="

make setup
make rc_branch DEPLOY_TARGET=dev GIT_BRANCH=$GIT_BRANCH
source rc_branch
make all
make deploy/deploy-branch.cfg
make deploy/conf/00-branch.conf

# Copy the apache configuration for the branch
cp deploy/conf/00-branch.conf $BASE_DIR/conf/00-$GIT_BRANCH.conf

# Restart apache on dev
sudo apache2ctl graceful

# Deploy to int if 'int' is specified
if [ $1 -a $1 == 'int' ];
then
    echo "==================================================================="
    echo "Deploying chsdi3 branch <${GIT_BRANCH}> to <dev> "
    echo "==================================================================="

    sudo -u deploy deploy -r deploy/deploy-branch.cfg int;
fi

if [ $1 -a $1 == 'demo' ];
then
    sudo -u deploy deploy -r deploy/deploy-branch.cfg demo;
fi


T="$(($(date +%s)-T))"

printf "Deploy time: %02d:%02d:%02d\n" "$((T/3600%24))" "$((T/60%60))" "$((T%60))"

