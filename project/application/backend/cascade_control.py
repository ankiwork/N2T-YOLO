import os
import json
from flet_core import Dropdown, TextField

from project.configuration.yolo.data_processing import default_settings, LABEL_TO_KEY, settings_file

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
        with open(settings_file, "w", encoding="utf-8") as f:
            json.dump(default_settings, f, indent=4)

    with open(settings_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
        return settings["launch_denial"]


def update_file_settings():
    """
    Вспомогательная функция контроля флага

    Возвращает:
    None
    """
    with open(settings_file, "r", encoding="utf-8") as f:
        settings = json.load(f)
        settings["launch_denial"] = 1 - settings["launch_denial"]
    with open(settings_file, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)


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

    with open(settings_file, "w", encoding="utf-8") as f:
        json.dump(default_settings, f, indent=4)

    settings.update()
