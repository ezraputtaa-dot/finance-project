#!/usr/bin/env bash
set -euo pipefail

# Idempotent bootstrap: verify Python and compile project modules.
python3 --version
python3 -m compileall -q .
