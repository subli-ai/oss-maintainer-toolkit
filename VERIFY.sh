#!/bin/sh
set -eu
python3 -m pytest
oss-maintainer-toolkit check .
