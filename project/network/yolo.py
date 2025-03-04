import os
import json
import threading

from project.configuration.yolo.data_processing import load_data, settings_file
from project.application.backend.logger import logger_initialisation


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
    with open(settings_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
        path = settings["dataset_path"]
        path = (path.rsplit('\\data.yaml', 1)[0])
    # Формируем путь к папке datasets
    datasets_path = os.path.join(project_root, path)

    path_to_ultralytics = (os.environ['APPDATA'] + "\\Ultralytics\\settings.json")

    with open(path_to_ultralytics, "r", encoding="utf-8") as f:
        dataset_path = json.load(f)
        if dataset_path["datasets_dir"] != datasets_path:
            with open(path_to_ultralytics, "w", encoding="utf-8") as file:
                dataset_path["datasets_dir"] = datasets_path
                json.dump(dataset_path, file, indent=0)


def start_training(log_widget):
    """
    Инициирует обучение.

    Параметры:
     - log_widget (TextField): поле для логирования

    Возвращает:
    None
    """
    threading.Thread(target=train_yolo_model, args=(log_widget,), daemon=True).start()


def params_designation():
    """
    Получает параметры для обучения YOLO из JSON-файла.

    Параметры:
     - log_widget (TextField): поле для логирования

    Возвращает:
    - params (dict): Словарь с параметрами для обучения
    """
    from ultralytics import YOLO
    params = {
        "device": 0 if load_data("Тип графического устройства") == "gpu" else 'cpu',
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

    get_datasets_path()

    params = params_designation()
    logger_initialisation(log_widget)

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
