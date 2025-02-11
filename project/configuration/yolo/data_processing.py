import os
import json

settings_file = "project/configuration/yolo/data/launch_settings.json"
data_folder = os.path.dirname(settings_file)


def save_data(data, label):
    """
    Сохраняет данные в файл.

    Параметры:
    data (str): Данные для сохранения в файл;
    label (str): Указатель для записи данных.

    Возвращает:
    None
    """
    with open(settings_file, "r") as f:
        settings = json.load(f)
        if label == "Тип графического устройства":
            settings["selected_yolo_device"] = data
        elif label == "Количество эпох":
            settings["selected_yolo_epochs"] = data
        elif label == "Размер изображения":
            settings["selected_yolo_resolution"] = data
        elif label == "Версия YOLO":
            settings["selected_yolo_version"] = data
        elif label == "Контрольные точки обучения":
            settings["selected_save_mode"] = data
        elif label == "Частота сохранения контрольных точек":
            settings["selected_save_period"] = data
        elif label == "Кэширование изображений":
            settings["cache_on"] = data
        elif label == "Имя директории проекта":
            settings["name_of_project"] = data
        elif label == "Имя тренировочного прогона":
            settings["name_of_records_directory"] = data
        elif label == "Перезапись существующего названия":
            settings["rewrite_ok"] = data
        elif label == "Начинать ли обучение с предварительно обученной модели":
            settings["selected_pretrained_mode"] = data
        elif label == "Случайное зерно для обучения":
            settings["selected_seed"] = data
        elif label == "Детерминированные алгоритмы":
            settings["deterministic_enabled"] = data
        elif label == "Мега класс":
            settings["mega_clss"] = data
        elif label == "Список классов":
            settings["classes_list"] = data
        elif label == "Прямоугольное обучение":
            settings["rect_on"] = data
        else:
            print("Ошибка типа")
            return
    with open(settings_file, "w") as f:
        json.dump(settings, f, indent=4)


def load_data(label):
    """
    Загружает данные из файла.

    Параметры:
    label (str): Указатель для получения данных.

    Возвращает:
    setting (int, str): параметр для настройки
    """

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    if not os.path.exists(settings_file):
        with open(settings_file, "w") as f:
            json.dump({
                "launch_denial": 0,
                "selected_yolo_device": "gpu",
                "selected_yolo_epochs": 100,
                "selected_yolo_resolution": 320,
                "selected_yolo_version": "yolo11m.pt",
                "selected_save_mode": "True",
                "selected_save_period": -1,
                "cache_on": "False",
                "name_of_project": "None",
                "name_of_records_directory": "None",
                "rewrite_ok": "False",
                "selected_pretrained_mode": "True",
                "selected_seed": 0,
                "deterministic_enabled": "True",
                "mega_clss": "False",
                "classes_list": "None",
                "rect_on": "False"}, f, indent=4)

    with open(settings_file, "r") as f:
        settings = json.load(f)
        if label == "Тип графического устройства":
            setting = settings.get("selected_yolo_device")
        elif label == "Количество эпох":
            setting = settings.get("selected_yolo_epochs")
        elif label == "Размер изображения":
            setting = settings.get("selected_yolo_resolution")
        elif label == "Версия YOLO":
            setting = settings.get("selected_yolo_version")
        elif label == "Контрольные точки обучения":
            setting = settings.get("selected_save_mode")
        elif label == "Частота сохранения контрольных точек":
            setting = settings.get("selected_save_period")
        elif label == "Кэширование изображений":
            setting = settings.get("cache_on")
        elif label == "Имя директории проекта":
            setting = settings.get("name_of_project")
        elif label == "Имя тренировочного прогона":
            setting = settings.get("name_of_records_directory")
        elif label == "Перезапись существующего названия":
            setting = settings.get("rewrite_ok")
        elif label == "Начинать ли обучение с предварительно обученной модели":
            setting = settings.get("selected_pretrained_mode")
        elif label == "Случайное зерно для обучения":
            setting = settings.get("selected_seed")
        elif label == "Детерминированные алгоритмы":
            setting = settings.get("deterministic_enabled")
        elif label == "Мега класс":
            setting = settings.get("mega_clss")
        elif label == "Список классов":
            setting = settings.get("classes_list")
        elif label == "Прямоугольное обучение":
            setting = settings.get("rect_on")
        return setting
