#!/bin/bash

PYTHON_FILES=`find ../chsdi/* ../tests/* -path ../chsdi/static -prune -o -path ../chsdi/lib/sphinxapi -prune -o -path ../tests/e2e -prune -o -type f -name "*.py" -print`
2to3-3.7 -w -n $PYTHON_FILES