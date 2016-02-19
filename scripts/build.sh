#!/bin/bash

currentdir=$(pwd)
path=${currentdir%/*}
pathlen=${#path}
parentdirname=$(echo ${currentdir:$pathlen})

if [ $parentdirname = '/scripts' ]
then
  cd ..
fi

if [ -z $1 ]
then
  echo "No target provided"
  echo "Possible targets are:"
  echo "- dev"
  echo "- int"
  echo "- prod"
  echo "- a defined user configuration"
  exit 2
fi 

if [ $1 = "dev" ]
then
  make clean
  source rc_dev
elif [ $1 = "int" ]
then
  make clean
  source rc_int
elif [ $1 = "prod" ]
then
  make clean
  source rc_prod
else
  if [ -f rc_user_$1 ]
  then
    source rc_user_$1
  else
    echo "No file with the name rc_user_$1 could be found"
    echo "Please create a configuration file"
    exit 2
  fi
fi

make all
