import os
import sys


def get_resource_path(relative_path):
    """Получает абсолютный путь к ресурсу, работает как для разработки, так и для сборки PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("TRAINER_BASE", os.path.abspath("."))
    return os.path.join(base_path, relative_path)


def get_file_paths():
    ttx_file = get_resource_path("files/ttx.docx")
    demo_file = get_resource_path("files/IMG_4636.mp4")
    reference_file = get_resource_path("files/reference.txt")
    return ttx_file, demo_file, reference_file
