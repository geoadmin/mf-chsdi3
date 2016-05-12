#!/bin/bash

make lint
if [[ $? != 0 ]]; then
  echo "$(tput setaf 1) Nothing has been commited because of styling issues, please fix it according to the comments above $(tput sgr0)"
  exit 1
fi

PATH=.venv/bin:"$PATH"

git secrets --pre_commit_hook -- "$@"
