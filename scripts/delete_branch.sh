#!/bin/bash

set -e

TARGET=$1
BRANCH=$2

BASE=/var/www/vhosts/mf-chsdi3
BRANCH_DIR=$BASE/private/branch
CONF="$BASE/conf/00-$BRANCH.conf"
BASEDIR="$BRANCH_DIR/$BRANCH"

# Read target ips
source <(grep "$TARGET =" deploy/deploy.cfg | sed 's/ *//g')
IFS=', ' read -r -a TARGET_IPS <<< "${!TARGET}"

if [ ${#TARGET_IPS[@]} == 0 ]; then
    TARGET_IPS=('')
fi

if [ $# -ne 2 ]; then
    echo """No branch name given.
        If you are using through make you need to add a parameter BRANCH_TO_DELETE:
            make deletebranch  BRANCH_TO_DELETE=[branch_name_to_delete]
            make deletebranchdev  BRANCH_TO_DELETE=[branch_name_to_delete]
            make deletebranchint  BRANCH_TO_DELETE=[branch_name_to_delete]
        If you are using the script directly:
            ./scripts/delete_branch.sh [dev|int] [branch_name_to_delete]"""

    for TARGET_IP in "${TARGET_IPS[@]}"; do
        if [ $TARGET_IP ]; then
            echo "Possible values on $TARGET_IP:"
            BRANCHES=$(ssh $USER@$TARGET_IP "ls $BRANCH_DIR")
        else
            echo "Possible values on dev:"
            BRANCHES=$(ls $BRANCH_DIR)
        fi
        for b in $BRANCHES; do
            echo "        $b"
        done
    done
    exit 0
fi

if [ $TARGET == "int" ]; then
    echo "Deleting branch ${BRANCH} on int"

    for TARGET_IP in "${TARGET_IPS[@]}"; do
        echo "    Delete conf file $CONF"
        RESULTS=$(ssh $USER@$TARGET_IP "rm -f $CONF")
        if [ $? != 0 ]; then
            echo $RESULTS
            exit $?
        fi
        echo "    Delete branch folder $BASEDIR"
        RESULTS=$(ssh $USER@$TARGET_IP "rm -rf $BASEDIR")
        if [ $? != 0 ]; then
            echo $RESULTS
            exit $?
        fi
        echo "Branch $BRANCH deleted on $TARGET_IP"
    done
    exit 0
fi

echo "Deleting branch $BRANCH on dev"
echo "    Delete conf file $CONF"
rm -f  $CONF
echo "    Delete branch folder $BASEDIR"
rm -rf $BASEDIR
echo "Branch $BRANCH deleted on dev"
echo "Please, restart apache"
exit 0
