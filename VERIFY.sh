#!/bin/sh
set -eu
python3 -m pip install --no-build-isolation -e ".[test]"
python3 -m pytest
oss-maintainer-toolkit check .
