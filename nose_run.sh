#!/bin/bash

# Adapt your ~/.pgpass file for this to work

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

cluster_to_use="pgcluster0t"

while getopts "ip" opt; do
  case "$opt" in
  i) cluster_to_use="pgcluster0i"
     ;;
  p) cluster_to_use="pgcluster0"
     ;;
  esac
done

shift $((OPTIND-1))
[ "$1" = "--" ] && shift

cp -f production.ini production.ini.bup

sed -i "s/pgcluster0t/$cluster_to_use/g" production.ini && buildout/bin/nosetests

rc=$?

mv -f production.ini.bup production.ini

exit $rc

