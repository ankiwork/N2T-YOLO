import os
import sys
import time
import json
import logging
import threading
from functools import wraps
from ultralytics import YOLO


from project.configuration.yolo.data_processing import load_data
from project.application.backend.cascade_control import update_launch_settings
from project.application.backend.logger import LogRedirector


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


def retry(num_retries, exception_to_check, sleep_time=0):
    """
    Декоратор, повторяющий выполнение функции обучения, если было вызвано исключение RuntimeError
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_retries+1):
                try:
                    path_to_ultralytics = (os.environ['APPDATA'] + "\\Ultralytics\\settings.json")
                    with open(path_to_ultralytics, "r", encoding="utf-8") as f:
                        dataset_path = json.load(f)
                        if dataset_path["datasets_dir"] != "C:\\Users\\Artyom\\Desktop\\N2T-YOLO\\datasets":
                            with open(path_to_ultralytics, "w", encoding="utf-8") as f:
                                dataset_path["datasets_dir"] = "C:\\Users\\Artyom\\Desktop\\N2T-YOLO\\datasets"
                                json.dump(dataset_path, f, indent=0)
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f"{func.__name__} raised {e.__class__.__name__}. Retrying...")
                    if i < num_retries:
                        time.sleep(sleep_time)
            # Raise the exception if the function was not successful after the specified number of retries
            raise exception_to_check
        return wrapper
    return decorate


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
