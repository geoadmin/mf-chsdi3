#!/bin/bash

# Adapt your ~/.pgpass file for this to work

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

conf_to_use="buildout_nose_dev.cfg"

nosetests_options="-e .*e2e.*"

while getopts "ipa" opt ; do
  case $opt in
  i) echo "Case i"
     ;;
  p) conf_to_use="buildout_nose_prod.cfg"
     ;;
  a) nosetests_options=" "
     ;;
  esac
done

shift $((OPTIND-1))
[ "$1" = "--" ] && shift

exit $rc

