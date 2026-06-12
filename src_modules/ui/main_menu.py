import tkinter as tk

from config.styles import content_wraplength, get_menu_button_font, setup_ttk_styles


def setup_main_menu(app):
    for widget in app.root.winfo_children():
        widget.destroy()

    setup_ttk_styles(app.root)
    menu_font = get_menu_button_font()
    wraplength = content_wraplength(app.root, padding=80)

    main_frame = tk.Frame(
        app.root,
        bg=app.colors["bg_light"],
        padx=30,
        pady=30,
    )
    main_frame.pack(fill=tk.BOTH, expand=True)

    title_frame = tk.Frame(main_frame, bg=app.colors["bg_light"])
    title_frame.pack(fill=tk.X, pady=20)

    title_label = tk.Label(
        title_frame,
        text="ПРОГРАММА-ТРЕНАЖЁР",
        font=app.title_font,
        fg=app.colors["primary"],
        bg=app.colors["bg_light"],
        wraplength=wraplength,
        justify=tk.CENTER,
    )
    title_label.pack()

    subtitle = tk.Label(
        title_frame,
        text="Выберите раздел для работы",
        font=app.button_font,
        fg=app.colors["text_dark"],
        bg=app.colors["bg_light"],
        wraplength=wraplength,
        justify=tk.CENTER,
    )
    subtitle.pack(pady=10)

    button_frame = tk.Frame(main_frame, bg=app.colors["bg_light"], pady=20)
    button_frame.pack()

    buttons = [
        ("ТТХ", app.open_ttx, app.colors["primary"]),
        ("Демонстрация", app.open_demonstration, app.colors["primary"]),
        ("Тест", app.open_test, app.colors["primary"]),
        ("Справка", app.open_reference, app.colors["primary"]),
        ("Выход", app.confirm_exit, app.colors["accent"]),
    ]

    for text, command, color in buttons:
        btn = tk.Button(
            button_frame,
            text=text,
            command=command,
            width=34,
            font=menu_font,
            padx=12,
            pady=10,
            bg=color,
            fg="white",
            activebackground="#34495e",
            activeforeground="white",
            relief=tk.RAISED,
            bd=3,
        )
        btn.pack(pady=14, ipadx=6, ipady=4)
