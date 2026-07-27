#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PY="$HOME/miniconda3/envs/py311/bin/python"
"$PY" -m PyInstaller --clean --noconfirm trainer.spec
