#!/bin/bash

PATH=.venv/bin:"$PATH"

git secrets --prepare_commit_msg_hook -- "$@"
