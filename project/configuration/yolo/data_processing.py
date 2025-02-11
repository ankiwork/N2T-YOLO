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
        return setting
