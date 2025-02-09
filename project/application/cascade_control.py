import os
import json


settings_file = "project/configuration/yolo/data/launch_settings.json"

def check_file_settings():
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


def save_settings(data, label):
    with open(settings_file, "w") as f:
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
        json.dump(settings, f, indent=4)

def update_launch_settings():
    with open(settings_file, "r") as f:
        settings = json.load(f)
        if settings["launch_denial"] == 1:
            settings["launch_denial"] = 0
        else:
            settings["launch_denial"] = 1
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)


def cleanup():
    update_launch_settings()
