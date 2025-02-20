import sys
import logging
import threading
from ultralytics import YOLO

from project.network.checks import retry
from project.application.backend.logger import LogRedirector
from project.configuration.yolo.data_processing import load_data
from project.application.backend.cascade_control import update_launch_settings


def start_training(log_output):
    """
    Инициирует обучение.

    Возвращает:
    None
    """
    threading.Thread(target=train_yolo_model, args=(log_output,), daemon=True).start()


def params_designation(log_widget=""):
    """
    Получает параметры для обучения YOLO из JSON-файла.

    Параметры:
     - log_widget (TextField): поле для логирования

    Возвращает:
    - params (dict): Словарь с параметрами для обучения
    """
    if log_widget != "":
        log_redirector = LogRedirector(log_widget)
        sys.stderr = log_redirector  # Захватываем tqdm и ошибки

        logging.basicConfig(stream=sys.stderr, level=logging.INFO, force=True)  # Перенаправляем logging

    params = {
        "device": 0 if load_data("Тип графического устройства") == 0 else 'cpu',
        "epochs": int(load_data("Количество эпох")),
        "image": int(load_data("Размер изображения")),
        "data_yaml_path": "datasets/data.yaml",
        "name": load_data("Имя тренировочного прогона"),
        "project": load_data("Имя директории проекта"),
        "batch": int(load_data("Разовое количество фотографий")),
        "workers": int(load_data("Количество потоков-работников")),
        "patience": int(load_data("Ожидающие эпохи")),
        "lr0": float(load_data("Скорость обновления весов")),
        "model": YOLO(load_data("Версия YOLO")),
    }

    return params


@retry(num_retries=1, exception_to_check=RuntimeError, sleep_time=1)
def train_yolo_model(log_widget):
    """
    Обучает модель YOLO на пользовательском наборе данных и контроль за флагом запуска.

    Возвращает:
    - None
    """
    params = params_designation(log_widget)
    results = params["model"].train(
        batch=params["batch"],
        workers=params["workers"],
        patience=params["patience"],
        lr0=params["lr0"],
        name=params["name"],
        project=params["project"],
        device=params["device"],
        optimizer='SGD',
        imgsz=params["image"],
        epochs=params["epochs"],
        data=params["data_yaml_path"],
    )
    update_launch_settings()
    print("Обучение завершено. Результаты:", results)
