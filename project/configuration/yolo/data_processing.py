import os
import json

settings_file = "project/configuration/yolo/data/launch_settings.json"
data_folder = os.path.dirname(settings_file)

default_settings = {
    "launch_denial": 0,
    "batch": 1,
    "workers": 4,
    "patience": 5,
    "lr0": 0.0001,
    "selected_yolo_device": "gpu",
    "selected_yolo_epochs": 100,
    "selected_yolo_resolution": 320,
    "selected_yolo_version": "yolo11m.pt",
    "selected_save_mode": "True",
    "selected_save_period": -1,
    "cache_on": "False",
    "name_of_project": "runs",
    "name_of_records_directory": "train",
    "rewrite_ok": "False",
    "selected_pretrained_mode": "True",
    "selected_seed": 0,
    "deterministic_enabled": "True",
    "mega_clss": "False",
    "classes_list": "None",
    "rect_on": "False"
}

LABEL_TO_KEY = {
    "Разовое количество фотографий": "batch",
    "Количество потоков-работников": "workers",
    "Ожидающие эпохи": "patience",
    "Скорость обновления весов": "lr0",
    "Тип графического устройства": "selected_yolo_device",
    "Количество эпох": "selected_yolo_epochs",
    "Размер изображения": "selected_yolo_resolution",
    "Версия YOLO": "selected_yolo_version",
    "Контрольные точки обучения": "selected_save_mode",
    "Частота сохранения контрольных точек": "selected_save_period",
    "Кэширование изображений": "cache_on",
    "Имя директории проекта": "name_of_project",
    "Имя тренировочного прогона": "name_of_records_directory",
    "Перезапись существующего названия": "rewrite_ok",
    "Начинать ли обучение с предварительно обученной модели": "selected_pretrained_mode",
    "Случайное зерно для обучения": "selected_seed",
    "Детерминированные алгоритмы": "deterministic_enabled",
    "Мега класс": "mega_clss",
    "Список классов": "classes_list",
    "Прямоугольное обучение": "rect_on",
}


def is_number(value):
    """
    Проверяет, является ли строка числом (int или float)

    Параметры:
    value : неопределенная строка

    Возвращает:
    value
    """

    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value  # Оставляем как есть, если это не число


def save_data(data, label):
    """
    Сохраняет данные в JSON-файл.

    Параметры:
    data (str): Данные для сохранения;
    label (str): Ключ для сохранения данных.

    Возвращает:
    None
    """
    key = LABEL_TO_KEY.get(label)
    if key is None:
        print("Ошибка типа")
        return

    try:
        with open(settings_file, "r", encoding="utf-8") as f:
            settings = json.load(f)

        settings[key] = is_number(data)

        with open(settings_file, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка при обработке JSON: {e}")


def initialize_settings():
    """Создает файл настроек, если он отсутствует."""
    os.makedirs(os.path.dirname(settings_file), exist_ok=True)
    if not os.path.exists(settings_file):
        with open(settings_file, "w", encoding="utf-8") as f:
            json.dump(default_settings, f, indent=4, ensure_ascii=False)


def load_data(label):
    """
    Загружает данные из JSON-файла.

    Параметры:
    label (str): Ключ для получения данных.

    Возвращает:
    setting (int, str): Значение параметра или None в случае ошибки.
    """
    initialize_settings()

    key = LABEL_TO_KEY.get(label)
    if key is None:
        print("Ошибка типа")
        return None

    try:
        with open(settings_file, "r", encoding="utf-8") as f:
            settings = json.load(f)
        return settings.get(key, None)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка при загрузке JSON: {e}")
        return None
