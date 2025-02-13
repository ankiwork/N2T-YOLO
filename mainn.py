import sys
import threading
import logging
from ultralytics import YOLO
import flet as ft
import io
import re


class LogRedirector(io.TextIOBase):
    """Класс для перенаправления вывода в Flet UI."""

    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.lock = threading.Lock()

    def write(self, message):
        match = re.search(r"(\d+/\d+).*?:\s*(\d+%)\|.*?\|\s*(\d+/\d+ \[.*?])", message)
        if match:
            epoch_info = match.group(1)  # Например, "1/100"
            percent_complete = match.group(2)  # Прогресс "3%"
            tqdm_progress = match.group(3)  # Часть "6/210 [00:12<05:44,  1.69s/it]"

            filtered_message = f"Эпоха: {epoch_info} - Прогресс: {percent_complete} - {tqdm_progress}"

            with self.lock:
                self.text_widget.value = ""  # Очищаем перед выводом
                self.text_widget.value = filtered_message + "\n"
                self.text_widget.update()

    def flush(self):
        pass  # Ничего не делаем, но метод нужен


def train_yolo_model(log_widget):
    """
    Запускает обучение модели YOLO и направляет логи в UI.
    """

    log_redirector = LogRedirector(log_widget)
    sys.stdout = log_redirector
    sys.stderr = log_redirector  # Захватываем tqdm и ошибки

    logging.basicConfig(stream=sys.stdout, level=logging.INFO, force=True)  # Перенаправляем logging

    # Загрузка предобученной модели
    model = "yolo11m.pt"
    model = YOLO(model)
    data_yaml_path = "datasets/data.yaml"
    # Запуск обучения
    results = model.train(
        batch=1,
        workers=4,
        patience=5,
        lr0=0.0001,
        device="cpu",
        optimizer='SGD',
        imgsz=320,
        epochs=100,
        data=data_yaml_path,
    )

    return results


def main(page: ft.Page):
    page.title = "Логгирование YOLO Training"

    log_output = ft.TextField(
        multiline=True,
        read_only=True,
        width=700,
        height=400
    )

    def start_training(e):
        threading.Thread(target=train_yolo_model, args=(log_output,), daemon=True).start()

    start_button = ft.ElevatedButton("Начать обучение", on_click=start_training)

    page.add(start_button, log_output)


ft.app(target=main)
