#! /bin/bash

set -e

pygmentize -f html -l python -o $1.html $1.py
