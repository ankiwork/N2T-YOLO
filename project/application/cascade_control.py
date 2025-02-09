import os
import json

settings_file = "project/configuration/yolo/data/launch_settings.json"

def check_file_settings():
    """
    Проверяет наличие настроечного файла и записывает параметры по умолчанию.

    Параметры:
    None

    Возвращает:
    launch_denial (int): Флаг того, что запуск произведен впервые
    """
    if not os.path.exists(settings_file):
        with open(settings_file, "w") as f:
            json.dump({"launch_denial": 0,
                       "selected_yolo_device": "gpu",
                       "selected_yolo_epochs": 100,
                       "selected_yolo_resolution": 320,
                       "selected_yolo_version": "yolo11m.pt"}, f, indent=4)

    with open(settings_file, "r") as f:
        settings = json.load(f)

    return settings.get("launch_denial")

def update_launch_settings():
    """
    Обновляет флаг запуска.

    Параметры:
    None

    Возвращает:
    None
    """
    with open(settings_file, "r") as f:
        settings = json.load(f)
        if settings["launch_denial"] == 1:
            settings["launch_denial"] = 0
        else:
            settings["launch_denial"] = 1
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)


def cleanup():
    """
    Проверка корректности параметров при штатном выключении программы.

    Параметры:
    None

    Возвращает:
    None
    """
    update_launch_settings()
