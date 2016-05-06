#!/bin/bash

PATH=.venv/bin:"$PATH"

git secrets --commit_msg_hook -- "$@"
