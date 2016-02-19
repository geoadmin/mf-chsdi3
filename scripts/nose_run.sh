#!/bin/bash

# Adapt your ~/.pgpass file for this to work

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

while getopts "ipa" opt; do
  case "$opt" in
  i) nosetests_options="-e .*e2e.*"
     make clean
     source rc_int
     make all
     ;;
  p) nosetests_options="-e .*e2e.*"
     make clean
     source rc_prod
     make all
     ;;
  a) nosetests_options=" "
     ;;
  esac
done

shift $((OPTIND-1))
[ "$1" = "--" ] && shift

.venv/bin/nosetests $nosetests_options chsdi/tests

rc=$?

exit $rc
