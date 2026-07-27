import tkinter as tk
from tkinter import messagebox
from threading import Thread

from config.styles import get_colors, get_fonts
from config.paths import get_file_paths
from ui.main_menu import setup_main_menu
from ui.ttx_view import open_ttx
from ui.demo_view import open_demonstration
from ui.test_view import open_test
from ui.reference_view import open_reference


class AppTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа-тренажёр")
        self.root.geometry("1025x800")
        self.root.resizable(True, True)
        self.root.config(bg="#f0f0f0")

        self.title_font, self.button_font, self.text_font = get_fonts()
        self.colors = get_colors()

        self.ttx_file, self.demo_file, self.reference_file = get_file_paths()

        self.is_playing = False
        self.video_thread = None
        self.video_label = None

        self.setup_main_menu()

    def setup_main_menu(self):
        setup_main_menu(self)

    def open_ttx(self):
        open_ttx(self)

    def open_demonstration(self):
        open_demonstration(self)

    def open_test(self):
        open_test(self)

    def open_reference(self):
        open_reference(self)

    def play_video(self):
        from utils.video_player import play_video_thread

        if not self.is_playing:
            self.is_playing = True
            self.video_thread = Thread(target=lambda: play_video_thread(self), daemon=True)
            self.video_thread.start()

    def pause_video(self):
        self.is_playing = False

    def ask_return_to_menu(self):
        answer = messagebox.askyesno("Выход", "Вернуться в главное меню?")
        if answer:
            self.is_playing = False
            if self.video_thread and self.video_thread.is_alive():
                self.video_thread.join(timeout=1.0)
            self.setup_main_menu()

    def confirm_exit(self):
        self.is_playing = False
        if self.video_thread and self.video_thread.is_alive():
            self.video_thread.join(timeout=1.0)

        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

    def __del__(self):
        self.is_playing = False
        if hasattr(self, "video_thread") and self.video_thread and self.video_thread.is_alive():
            self.video_thread.join(timeout=1.0)
