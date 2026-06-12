import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

PREFERRED_FAMILIES = (
    "Ubuntu",
    "DejaVu Sans",
    "Noto Sans",
    "Liberation Sans",
    "Helvetica Neue",
    "Helvetica",
    "Arial",
)


_font_family = None


def pick_font_family():
    global _font_family
    if _font_family:
        return _font_family

    try:
        available = set(tkfont.families())
    except RuntimeError:
        _font_family = "DejaVu Sans"
        return _font_family

    for family in PREFERRED_FAMILIES:
        if family in available:
            _font_family = family
            return _font_family

    _font_family = "TkDefaultFont"
    return _font_family


def get_fonts():
    family = pick_font_family()
    title_font = tkfont.Font(family=family, size=20, weight="bold")
    button_font = tkfont.Font(family=family, size=12)
    text_font = tkfont.Font(family=family, size=11)
    return title_font, button_font, text_font


def get_question_font():
    return tkfont.Font(family=pick_font_family(), size=11, weight="bold")


def get_option_font():
    return tkfont.Font(family=pick_font_family(), size=10)


def get_menu_button_font():
    return tkfont.Font(family=pick_font_family(), size=15, weight="bold")


def get_colors():
    colors = {
        "primary": "#3498db",
        "secondary": "#2ecc71",
        "accent": "#e74c3c",
        "bg_light": "#ecf0f1",
        "text_dark": "#2c3e50",
    }
    return colors


def setup_ttk_styles(root):
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    style.configure("TLabel", font=get_question_font(), foreground="#2c3e50")
    style.configure("TRadiobutton", font=get_option_font(), foreground="#2c3e50")
    style.configure("TFrame", background="#ecf0f1")
    style.configure("TSeparator", background="#bdc3c7")


def content_wraplength(root, padding=100):
    root.update_idletasks()
    width = root.winfo_width()
    if width <= 1:
        width = 1025
    return max(width - padding, 320)


def create_readonly_text(parent, app, scrollbar):
    text_widget = tk.Text(
        parent,
        yscrollcommand=scrollbar.set,
        wrap=tk.WORD,
        font=app.text_font,
        padx=14,
        pady=12,
        spacing1=4,
        spacing2=2,
        spacing3=6,
        bg="white",
        fg=app.colors["text_dark"],
        relief=tk.FLAT,
        borderwidth=0,
        highlightthickness=0,
        cursor="arrow",
    )
    return text_widget
