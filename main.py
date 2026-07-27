import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "src_modules"))

import tkinter as tk
from tkinter import messagebox

from app_trainer import AppTrainer


if __name__ == "__main__":
    root = tk.Tk()

    def on_close():
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            root.quit()

    root.protocol("WM_DELETE_WINDOW", on_close)

    app = AppTrainer(root)
    root.mainloop()
