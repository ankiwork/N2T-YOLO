import os
import sys
import json
import logging
import threading
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


def train_yolo_model(log_widget):
    """
    Обучает модель YOLO на пользовательском наборе данных и контроль за флагом запуска.

    Возвращает:
    - None
    """
    log_redirector = LogRedirector(log_widget)
    sys.stderr = log_redirector  # Захватываем tqdm и ошибки

    logging.basicConfig(stream=sys.stderr, level=logging.INFO, force=True)  # Перенаправляем logging

    device = 0 if (load_data("Тип графического устройства")) == 0 else 'cpu'

    epochs = load_data("Количество эпох")

    image = load_data("Размер изображения")

    data_yaml_path = "datasets/data.yaml"

    name = load_data("Имя тренировочного прогона")

    batch = load_data("Разовое количество фотографий")

    workers = load_data("Количество потоков-работников")

    patience = load_data("Ожидающие эпохи")

    lr0 = load_data("Скорость обновления весов")

    model = load_data("Версия YOLO")

    model = YOLO(model)

    path_to_ultralytics = (os.environ['APPDATA'] + "\\Ultralytics\\settings.json")

    with open(path_to_ultralytics, "r", encoding="utf-8") as f:
        dataset_path = json.load(f)
        if dataset_path["datasets_dir"] != "C:\\Users\\Artyom\\Desktop\\N2T-YOLO\\datasets":
            with open(path_to_ultralytics, "w", encoding="utf-8") as f:
                dataset_path["datasets_dir"] = "C:\\Users\\Artyom\\Desktop\\N2T-YOLO\\datasets"
                json.dump(dataset_path, f, indent=0)
    try:
        results = model.train(
            batch=int(batch),              # Количество изображений, обрабатываемых за один раз
            workers=int(workers),            # Количество потоков-работников для загрузки данных
            patience=int(patience),           # Эпохи ожидания без заметного улучшения
            lr0=float(lr0),           # Определяет, насколько быстро модель будет обновлять свои веса
            name=name,          # Имя для текущего запуска обучения
            device=device,        # Устройство для выполнения обучения
            optimizer='SGD',      # Оптимизатор, который следует использовать для обучения
            imgsz=int(image),     # Размер входного изображения
            epochs=int(epochs),   # Количество эпох обучения
            data=data_yaml_path,  # Путь к файлу конфигурации набора данных
        )
    except RuntimeError:
        pass

    update_launch_settings()
    print("Обучение завершено. Результаты:", results)
