import os
import json

from flet_core import Dropdown, TextField

from project.configuration.yolo.data_processing import default_settings, LABEL_TO_KEY

settings_file = "project/configuration/yolo/data/launch_settings.json"
data_folder = os.path.dirname(settings_file)


def check_file_settings():
    """
    Проверяет наличие папки data и настроечного файла, записывает параметры по умолчанию.

    Возвращает:
    launch_denial (int): Флаг того, что запуск произведен впервые
    """
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    if not os.path.exists(settings_file):
        with open(settings_file, "w") as f:
            json.dump({
                "batch": 1,
                "workers": 4,
                "patience": 5,
                "lr0": 0.0001,
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


def reset_settings(controls, settings):
    """
    Проверка корректности параметров при штатном выключении программы.

    Параметры:
    textfield (TextField): Поля настройки со вписыванием параметров
    dropdown (Dropdown): Поля с выпадающем списком
    settings (Tab): Вкладка настроек

    Возвращает:
    None
    """
    for panel in controls:
        for control in panel.controls:
            if type(control) is Dropdown:
                label = LABEL_TO_KEY.get(control.label)
                control.value = type(control.value)(default_settings.get(label))
            if type(control) is TextField:
                label = LABEL_TO_KEY.get(control.label)
                control.value = type(control.value)(default_settings.get(label))
    settings.update()
