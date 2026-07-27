#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

WINPY_DIR=".winpy"
WINPY_ZIP="python-3.11.9-embed-amd64.zip"
WINPY_URL="https://www.python.org/ftp/python/3.11.9/${WINPY_ZIP}"
GET_PIP="https://bootstrap.pypa.io/pip/get-pip.py"

if ! command -v wine64 >/dev/null 2>&1; then
  echo "wine64 не установлен. Установите: sudo apt install wine64"
  exit 1
fi

mkdir -p "$WINPY_DIR"
if [ ! -f "$WINPY_DIR/python.exe" ]; then
  curl -fsSL "$WINPY_URL" -o "/tmp/${WINPY_ZIP}"
  unzip -qo "/tmp/${WINPY_ZIP}" -d "$WINPY_DIR"
  cat > "$WINPY_DIR/python311._pth" <<'EOF'
python311.zip
.
Lib/site-packages
import site
EOF
  curl -fsSL "$GET_PIP" -o "/tmp/get-pip.py"
  wine64 "$WINPY_DIR/python.exe" /tmp/get-pip.py
fi

wine64 "$WINPY_DIR/python.exe" -m pip install --upgrade pip pyinstaller opencv-python pillow python-docx lxml
wine64 "$WINPY_DIR/python.exe" -m PyInstaller --clean --noconfirm trainer_win.spec

if [ -f dist/Programma-trenazher.exe ]; then
  cp dist/Programma-trenazher.exe "dist/Программа-тренажёр.exe"
fi
