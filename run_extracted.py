#!/usr/bin/env python3
"""Запуск распакованной программы-тренажёра (извлечено из PyInstaller)."""
import marshal
import os
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Программа-тренажёр.exe_extracted")
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src_modules")

os.environ["TRAINER_BASE"] = BASE
os.chdir(BASE)
sys.path.insert(0, SRC)
# Не даём Windows-библиотекам из распаковки (cv2, numpy и т.д.) перекрывать Linux-версии
sys.path = [p for p in sys.path if p not in ("", ".")]

with open(os.path.join(BASE, "main.pyc"), "rb") as f:
    f.read(16)
    code = marshal.load(f)

exec(code, {"__name__": "__main__"})
