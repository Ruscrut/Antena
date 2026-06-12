import os
import tkinter as tk
from tkinter import messagebox

from config.styles import setup_ttk_styles


def open_demonstration(app):
    if not os.path.exists(app.demo_file):
        messagebox.showerror("Ошибка", f"Файл {app.demo_file} не найден")
        return

    app.is_playing = False
    if app.video_thread and app.video_thread.is_alive():
        app.video_thread.join(1.0)

    for widget in app.root.winfo_children():
        widget.destroy()

    setup_ttk_styles(app.root)

    main_frame = tk.Frame(
        app.root,
        bg=app.colors["bg_light"],
        padx=20,
        pady=20,
    )
    main_frame.pack(fill=tk.BOTH, expand=True)

    title_label = tk.Label(
        main_frame,
        text="Демонстрация",
        font=app.title_font,
        fg=app.colors["primary"],
        bg=app.colors["bg_light"],
    )
    title_label.pack(pady=10)

    video_container = tk.Frame(main_frame, bg=app.colors["bg_light"])
    video_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    video_frame = tk.Frame(
        video_container,
        bg="black",
        bd=2,
        relief=tk.SUNKEN,
        height=350,
    )
    video_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    video_frame.pack_propagate(False)

    app.video_label = tk.Label(video_frame, bg="black")
    app.video_label.pack(fill=tk.BOTH, expand=True)

    control_frame = tk.Frame(video_container, bg=app.colors["bg_light"])
    control_frame.pack(fill=tk.X, pady=10)

    play_btn = tk.Button(
        control_frame,
        text="Воспроизвести",
        command=app.play_video,
        padx=15,
        font=app.button_font,
        bg=app.colors["secondary"],
        fg="white",
        activebackground="#27ae60",
    )
    play_btn.pack(side=tk.LEFT, padx=10)

    pause_btn = tk.Button(
        control_frame,
        text="Пауза",
        command=app.pause_video,
        padx=15,
        font=app.button_font,
        bg=app.colors["primary"],
        fg="white",
        activebackground="#2980b9",
    )
    pause_btn.pack(side=tk.LEFT, padx=10)

    exit_frame = tk.Frame(main_frame, bg=app.colors["bg_light"])
    exit_frame.pack(fill=tk.X, pady=10)

    exit_btn = tk.Button(
        exit_frame,
        text="Выход",
        command=app.ask_return_to_menu,
        padx=15,
        font=app.button_font,
        bg=app.colors["accent"],
        fg="white",
        activebackground="#c0392b",
        relief=tk.RAISED,
        bd=2,
    )
    exit_btn.pack(pady=15)
