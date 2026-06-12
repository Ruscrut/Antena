import os
import time

import cv2
from PIL import Image, ImageTk
from tkinter import messagebox


def play_video_thread(app):
    """Фоновый поток для воспроизведения видео"""
    try:
        if not os.path.exists(app.demo_file):
            app.root.after(
                0,
                lambda: messagebox.showerror("Ошибка", f"Видеофайл {app.demo_file} не найден"),
            )
            app.is_playing = False
            return

        cap = cv2.VideoCapture(app.demo_file)
        if not cap.isOpened():
            app.root.after(
                0,
                lambda: messagebox.showerror("Ошибка", "Не удалось открыть видеофайл"),
            )
            app.is_playing = False
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_delay = 1 / fps if fps else 1 / 30

        app.root.update_idletasks()

        while app.is_playing:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, _ = frame_rgb.shape

            label_width = app.video_label.winfo_width()
            label_height = app.video_label.winfo_height()

            if label_width <= 1 or label_height <= 1:
                label_width = width
                label_height = height

            aspect_ratio = width / height
            new_width = label_width
            new_height = int(new_width / aspect_ratio)

            if new_height > label_height:
                new_height = label_height
                new_width = int(new_height * aspect_ratio)

            resized_frame = cv2.resize(frame_rgb, (new_width, new_height))
            image = Image.fromarray(resized_frame)
            photo = ImageTk.PhotoImage(image=image)

            # Обновление GUI только из главного потока tkinter
            app.root.after(0, _show_frame, app, photo)

            time.sleep(frame_delay)

        cap.release()
    except Exception as exc:
        error_message = str(exc)

        def show_error(msg=error_message):
            messagebox.showerror("Ошибка", f"Ошибка воспроизведения видео: {msg}")

        app.root.after(0, show_error)
        app.is_playing = False


def _show_frame(app, photo):
    app.video_label.config(image=photo)
    app.video_label.image = photo
