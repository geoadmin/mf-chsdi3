#!/bin/bash

PATH=.venv/bin:"$PATH"

git secrets --pre_commit_hook -- "$@"
