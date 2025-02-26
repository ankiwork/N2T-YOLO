import sys
import logging
import threading
import json
import os

from ultralytics.utils import LOGGER
from project.application.backend.logger import LogRedirector
from project.configuration.yolo.data_processing import load_data


def get_datasets_path():
    """
    Ищет путь до папки с файлами для обучения YOLO

    Возвращает:
    - datasets_path (str): путь до папки с файлами
    """
    # Получаем абсолютный путь к текущему файлу (checks.py)
    current_file = os.path.abspath(__file__)

    # Поднимаемся на три уровня вверх, чтобы попасть в корень проекта
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))

    # Формируем путь к папке datasets
    datasets_path = os.path.join(project_root, "datasets")

    return datasets_path


path_to_ultralytics = (os.environ['APPDATA'] + "\\Ultralytics\\settings.json")
with open(path_to_ultralytics, "r", encoding="utf-8") as f:
    dataset_path = json.load(f)
    if dataset_path["datasets_dir"] != get_datasets_path():
        with open(path_to_ultralytics, "w", encoding="utf-8") as file:
            dataset_path["datasets_dir"] = get_datasets_path()
            json.dump(dataset_path, file, indent=0)

    from ultralytics import YOLO


def start_training(log_widget):
    """
    Инициирует обучение.

    Параметры:
     - log_widget (TextField): поле для логирования

    Возвращает:
    None
    """
    threading.Thread(target=train_yolo_model, args=(log_widget,), daemon=True).start()


def params_designation(log_widget=""):
    """
    Получает параметры для обучения YOLO из JSON-файла.

    Параметры:
     - log_widget (TextField): поле для логирования

    Возвращает:
    - params (dict): Словарь с параметрами для обучения
    """

    # Set up the logger
    if log_widget != "":
        logger = logging.getLogger('ultralytics')
        log_redirector = LogRedirector(log_widget)
        sys.stderr = log_redirector  # Захватываем tqdm и ошибки
        logger.handlers[0].stream = log_redirector
        logging.basicConfig(stream=logger.handlers[0].stream, level=logging.INFO, force=True)  # Перенаправляем logging

    params = {
        "device": 0 if load_data("Тип графического устройства") == 0 else 'cpu',
        "epochs": int(load_data("Количество эпох")),
        "image": int(load_data("Размер изображения")),
        "data_yaml_path": str(load_data("Путь до датасета")),
        "name": load_data("Имя тренировочного прогона"),
        "project": load_data("Имя директории проекта"),
        "batch": int(load_data("Разовое количество фотографий")),
        "workers": int(load_data("Количество потоков-работников")),
        "patience": int(load_data("Ожидающие эпохи")),
        "lr0": float(load_data("Скорость обновления весов")),
        "model": YOLO(load_data("Версия YOLO")),
    }

    return params


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

    print("Обучение завершено. Результаты:", results)
