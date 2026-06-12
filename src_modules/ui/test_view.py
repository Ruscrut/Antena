import tkinter as tk
from tkinter import messagebox, ttk

from config.styles import content_wraplength, get_option_font, get_question_font, setup_ttk_styles


def _make_option_row(parent, answer_var, option_text, value, wraplength):
    row = ttk.Frame(parent)
    row.pack(anchor="w", padx=20, pady=3, fill="x")

    radio = ttk.Radiobutton(row, variable=answer_var, value=value)
    radio.pack(side=tk.LEFT, anchor="n", padx=(0, 8))

    option_label = ttk.Label(
        row,
        text=option_text,
        font=get_option_font(),
        wraplength=wraplength,
        justify=tk.LEFT,
    )
    option_label.pack(side=tk.LEFT, fill="x", expand=True)

    def select_option(_event=None, selected=value):
        answer_var.set(selected)

    option_label.bind("<Button-1>", select_option)
    return radio, option_label


def open_test(app):
    for widget in app.root.winfo_children():
        widget.destroy()

    setup_ttk_styles(app.root)
    question_font = get_question_font()

    main_frame = tk.Frame(
        app.root,
        bg=app.colors["bg_light"],
        padx=20,
        pady=20,
    )
    main_frame.pack(fill=tk.BOTH, expand=True)

    title_label = tk.Label(
        main_frame,
        text="Тест",
        font=app.title_font,
        fg=app.colors["primary"],
        bg=app.colors["bg_light"],
    )
    title_label.pack(pady=10)

    canvas = tk.Canvas(main_frame, bg=app.colors["bg_light"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    question_labels = []
    option_labels = []

    def _on_frame_configure(_event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def _on_canvas_configure(event):
        canvas.itemconfig(canvas_window, width=max(event.width - 4, 200))
        wrap = max(event.width - 60, 240)
        option_wrap = max(wrap - 48, 180)
        for label in question_labels:
            label.configure(wraplength=wrap)
        for label in option_labels:
            label.configure(wraplength=option_wrap)

    scrollable_frame.bind("<Configure>", _on_frame_configure)
    canvas.bind("<Configure>", _on_canvas_configure)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True, padx=10)
    scrollbar.pack(side="right", fill="y")

    questions = [
        {
            "text": "1. Состав штатной антенной системы РПУ Р-361М3:",
            "options": [
                "А) ВН 2х13/9; VH 4x80/20; ОБ-150/2.7",
                "Б) ВН 2х13/9; VH 4x80/20; приёмо-передающая 5Б11",
                "В) ОБ-150/2.7; приёмо-передающая 4Б11-02; VH 4x80/20",
            ],
            "correct": 1,
        },
        {
            "text": "2. Диапазон частот антенны VH 4x80/20:",
            "options": [
                "А) 1.5-30 МГц",
                "Б) 1.5-17 МГц",
                "В) 1.5-29.99999 МГц",
            ],
            "correct": 0,
        },
        {
            "text": "3. Площадь развертывания аппаратной Р-361М3:",
            "options": [
                "А) 180х120",
                "Б) 240х160",
                "В) 200х200",
            ],
            "correct": 2,
        },
        {
            "text": "4. Коэффициент стоячей волны приёмо-передающей антенны 5Б11:",
            "options": [
                "А) ≤2",
                "Б) ≤1.8",
                "В) ≥2",
            ],
            "correct": 1,
        },
        {
            "text": "5. Коэффициент усиления приёмо-передающей антенны 5Б11:",
            "options": [
                "А) 14.5-15.5",
                "Б) 10",
                "В) <10",
            ],
            "correct": 0,
        },
        {
            "text": "6. Коэффициент бегущей волны приёмо-передающей антенны 5Б11:",
            "options": [
                "А) <1",
                "Б) >2",
                "В) ≤0.6",
            ],
            "correct": 2,
        },
        {
            "text": "7. Дальность связи приёмо-передающей антенны 5Б11:",
            "options": [
                "А) 100-120 км",
                "Б) 40-50 км",
                "В) 80-90 км",
            ],
            "correct": 1,
        },
    ]

    user_answers = []
    initial_wrap = content_wraplength(app.root, padding=120)
    option_wrap = max(initial_wrap - 48, 180)

    for i, question in enumerate(questions):
        question_frame = ttk.Frame(scrollable_frame, padding=10)
        question_frame.pack(fill="x", pady=5)

        question_label = ttk.Label(
            question_frame,
            text=question["text"],
            font=question_font,
            wraplength=initial_wrap,
            justify=tk.LEFT,
        )
        question_label.pack(anchor="w", pady=(0, 5))
        question_labels.append(question_label)

        answer_var = tk.IntVar(value=-1)
        user_answers.append(answer_var)

        for j, option in enumerate(question["options"]):
            _, option_label = _make_option_row(
                question_frame,
                answer_var,
                option,
                j,
                option_wrap,
            )
            option_labels.append(option_label)

        if i < len(questions) - 1:
            ttk.Separator(scrollable_frame, orient="horizontal").pack(fill="x", pady=10)

    def check_answers():
        all_correct = True

        for i, answer_var in enumerate(user_answers):
            if answer_var.get() == -1:
                messagebox.showwarning(
                    "Предупреждение",
                    f"Вы не ответили на вопрос {i + 1}!",
                )
                return

        for answer_var, question in zip(user_answers, questions):
            if answer_var.get() != question["correct"]:
                all_correct = False
                break

        if all_correct:
            messagebox.showinfo(
                "Поздравляем!",
                "Вы правильно ответили на все вопросы!",
            )
        else:
            messagebox.showerror(
                "Ошибка",
                "К сожалению, у вас есть ошибки в ответах.",
            )

        app.setup_main_menu()

    button_frame = ttk.Frame(main_frame, padding=10)
    button_frame.pack(fill="x", pady=15)

    submit_btn = tk.Button(
        button_frame,
        text="Проверить результаты",
        command=check_answers,
        padx=20,
        font=app.button_font,
        bg=app.colors["secondary"],
        fg="white",
        activebackground="#27ae60",
        relief=tk.RAISED,
        bd=2,
    )
    submit_btn.pack(side=tk.LEFT, padx=10)

    cancel_btn = tk.Button(
        button_frame,
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
    cancel_btn.pack(side=tk.RIGHT, padx=10)

    app.root.update_idletasks()
    canvas_width = canvas.winfo_width()
    if canvas_width > 1:
        _on_canvas_configure(type("Event", (), {"width": canvas_width})())
